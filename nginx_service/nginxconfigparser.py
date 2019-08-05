#!/usr/bin/python3
# _*_coding:utf8_*_

'''
 * Created with IntelliJ Pycharm.
 * Description:  
 * Project : autossl_client
 * Ide tools : PyCharm
 * File name : nginxconfigparser.py
 * Author <a href="mailto:3245554@qq.com">罗卫</a>
 * User: devops
 * Date: 2019/7/25
 * Time: 下午5:33
'''

from sysbase.confparser import configparser
from sysbase.logproduction import Logbase
from sysbase.basetools import systemtools


class nginxconfig:

    def __init__(self):
        _configparsers = configparser()
        _nginx_conf = _configparsers.confparser()
        self.nginx_config_path = _nginx_conf["nginx"]["nginxpath"]
        self.nginx_certificate = _nginx_conf["nginx"]["certificate_catalogue"]
        self.log = Logbase.logger
        self.sysbase = systemtools()

    def getnginxfilepathlist(self):
        lists = []
        for i in self.nginx_config_path:
            pathlist = self.sysbase.get_dir_list(i)
            lists += pathlist
        return lists

    def certificate_dir_chcek(self):
       return self.sysbase.dir_path_check(self.nginx_certificate)

    def certificate_write(self,filename,certificate):
        return self.sysbase.new_write_file(self.nginx_certificate+self.sysbase.osdircutflag()+filename,certificate)

    def getconfigtxt(self,file_path):
        return self.sysbase.readtxtfile(file_path)

    def remove_notes_comments(self,txtfile):
        '''
        Delete configuration file comments.
        :param conf_file_date_obj:
        :return: no comments data
        '''
        data = []
        for i in txtfile:
            import re
            if re.search('#',i) == None:
                data.append(i)
        return data

    def nginxconfiganalysis(self,txtfile):
        '''
        Nginx configuration file data is parsed into dictionary objects.
        :param data_buffer: Bufer after excluding comments
        :return: dict or error
        '''
        try:
            import re
            nodes = {}
            node_name = 'server'
            node_conut = 0
            for i in txtfile:
                i_n = i.replace('\n', '')
                i_ = i_n.strip(' ')
                if re.match('^%s$'%node_name, i_) or re.match('^%s {'%node_name, i_):
                    node = []
                    node.append(i_)
                    node_conut += 1
                    node_ = '%s_%d' % (node_name, node_conut)
                elif re.match('{', i_):
                    node.append(i_)
                    continue
                elif re.match('}', i_):
                    node.append(i_)
                    nodes.update({node_: node})
                    continue
                else:
                    node.append(i_)

            conf = {}
            for j in nodes:
                server = []
                for p in nodes[j]:
                    h = p.split(' ')
                    blank_count = h.count('')
                    if blank_count >= 1:
                        for n in range(0, blank_count):
                            h.remove('')
                    conf_dict = {}
                    if h == [] or h == None:
                        continue
                    elif len(h) > 2 and re.match('^location', h[0]) == None:
                        conf_dict.update({h[0]: h[1::]})
                        server.append(conf_dict)
                    elif len(h) > 1 and len(h) <= 2:
                        conf_dict.update({h[0]: h[1]})
                        server.append(conf_dict)
                    elif re.match('^location', h[0]):
                        string = ''
                        for e in h:
                            string += ' %s' % e
                        server.append(string)
                    else:
                        server.append(h[0])
                conf.update({j: server})
            return conf
        except Exception as e:
            self.log.error( 'Conversion error，error info：%s'%e.__context__)
            return None

    def nginx_config_write_buffer_fomat(self, config_object_data):
        '''
        nginx configtion write config file
        :param config_object_data: file buffer
        :return: ok or error
        '''
        try:
            string_buffer = ''
            for i in config_object_data:
                for j in config_object_data[i]:
                    if type(j) == dict:
                        for n in j:
                            tmp = ''
                            if type(j[n]) == list:
                                for k in j[n]:
                                    tmp += ' %s' % k
                                string_buffer += '    %s %s\n' % (n, tmp)
                            else:
                                string_buffer += '    %s %s\n' % (n, j[n])
                    else:
                        string_buffer += '%s\n' % j
            return string_buffer
        except Exception as e:
            self.log.error( 'Wirte error,error info:%s' % e)
            return None

    def add_Anti_seal_conf(self,domain,pem,key,proxy_pass):
        '''
        Add the nginx service configuration of the anti-blocking site.
        :param domain:
        :param pem:
        :param key:
        :return:
        '''
        config_info = '''server
    {
            listen 80;
            server_name %s;
            rewrite ^(.*)$ https://$host$1 permanent;
    }
    server
    {
        listen 443 ssl;
        server_name %s;
        ssl on;
        ssl_certificate   %s;
        ssl_certificate_key  %s;
        ssl_session_timeout 5m;
        ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        ssl_prefer_server_ciphers on;
        location / {
            proxy_redirect off;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            %s;
                }
        access_log /var/log/nginx/%s_access.log;
    }
            '''%(domain,domain,pem,key,domain,proxy_pass)
        return config_info,domain