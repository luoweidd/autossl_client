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
from urllib.request import urlretrieve
import re



class nginxconfig:

    SEAL_PROOF_BACK_END = "http://127.0.0.1:8090"


    def __init__(self):
        _configparsers = configparser()
        _nginx_conf = _configparsers.confparser()
        self.nginx_config_path = _nginx_conf["nginx"]["nginxpath"]
        self.sysbase = systemtools()
        self.nginx_certificate = _nginx_conf["nginx"]["certificate_catalogue"]
        self.sysbase.dir_path_check(self.nginx_certificate)
        self.log = Logbase.logger

    def getnginxfilepathlist(self):
        lists = []
        nginxcofig_path = self.nginx_config_path.split(',')
        for i in nginxcofig_path:
            self.log.info("this dir : %s"%i)
            pathlist = self.sysbase.get_dir_list(i)
            for j in pathlist:
                if re.match(r'^.*\.conf',j):
                    lists.append('%s%s%s'%(i,self.sysbase.osdircutflag(),j))
        return lists

    def domian_find_nignx_conf(self,old_domian):
        file_path_list = self.getnginxfilepathlist()
        for i in file_path_list:
            file_txt = self.sysbase.readlinefile(i)
            if file_txt != 'error':
                file_txt_r_n_c = self.remove_notes_comments(file_txt)
                file_dict = self.nginxconfiganalysis(file_txt_r_n_c)
                if file_dict["server_1"][3]["server_name"] == '%s;'%old_domian and file_dict["server_2"][3]["server_name"] == '%s;'%old_domian:
                    return [file_dict,i]
        else:
            return 'error: Not matched'

    def proxy_pass_find_nignx_conf(self,proxy_pass):
        file_path_list = self.getnginxfilepathlist()
        for i in file_path_list:
            file_txt = self.sysbase.readtxtfile(self.nginx_config_path + self.sysbase.osdircutflag() + i)
            if file_txt != 'error':
                file_txt_r_n_c = self.remove_notes_comments(file_txt)
                file_dict = self.nginxconfiganalysis(file_txt_r_n_c)
                if file_dict["server_2"][18]["proxy_pass"] == proxy_pass:
                    return [file_dict, i]
        else:
            return 'error: Not matched'

    def downlaodcert(self,dirname,filename,down_url):
        try:
            if re.match('^\*\.',dirname) or re.match('^\.',dirname):
                dirname = self.sysbase.getDomain(dirname)
            file_save_path = '%s%s%s%s'%(self.nginx_certificate,self.sysbase.osdircutflag(),dirname,self.sysbase.osdircutflag())
            self.sysbase.dir_path_check(file_save_path)
            file_path = '%s%s'%(file_save_path,filename)
            urlretrieve(down_url,file_path)
            return file_path
        except Exception as e:
            if e is object:
                for i in e:
                    print(i)
            else:
                print(e)

    def certificate_write(self,dirname,filename,certificate):
        try:
            file_path = self.nginx_certificate+self.sysbase.osdircutflag()+dirname+self.sysbase.osdircutflag()+filename
            self.sysbase.dir_path_check(file_path)
            self.sysbase.new_write_file(file_path,certificate)
            return file_path
        except Exception as e:
            if e is object:
                for i in e:
                    self.log.error(i)
            else:
                self.log.error(e)

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
            if e is object:
                for i in e:
                    self.log.error(i)
            else:
                self.log.error( 'Conversion error，error info：%s'%e)
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

    def add_Anti_seal_conf(self,domain,pem,key,proxy_pass=None):
        '''
        Add the nginx service configuration of the anti-blocking site.
        :param domain:
        :param pem:
        :param key:
        :return:
        '''
        if proxy_pass is None:
            proxy_pass = self.SEAL_PROOF_BACK_END
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
            proxy_pass %s;
                }
        access_log /var/log/nginx/%s_access.log;
    }
            '''%(domain,domain,pem,key,proxy_pass,self.sysbase.getDomain(domain))
        return config_info