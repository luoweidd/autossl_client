#!/usr/bin/python3
# _*_coding:utf8_*_

'''
 * Created with IntelliJ Pycharm.
 * Description:  
 * Project : autossl_client
 * Ide tools : PyCharm
 * File name : nginxoperation.py
 * Author <a href="mailto:3245554@qq.com">罗卫</a>
 * User: devops
 * Date: 2019/7/25
 * Time: 下午5:34
'''

from sysbase.logproduction import Logbase
from nginx_service.nginxconfigparser import nginxconfig
from sysbase.basetools import systemtools

class nginxperation:

    nginxopt = nginxconfig()
    basesys = systemtools()
    log = Logbase.logger

    def nignx_ssl_update(self,data):
        update_status = self.update_conf(data)
        if update_status == True:
            nginx_config_status = self.nginx_conf_check()
            if nginx_config_status is tuple:
                for i in nginx_config_status:
                    self.log.info('reload nginx config status:%s' % str(i))
            else:
                self.log.info('reload nginx config status:%s' % str(nginx_config_status))
            if nginx_config_status[0] == 0:
                nginx_server_status = self.restart_nginx_to_effective()
                if nginx_config_status is tuple:
                    for i in nginx_server_status:
                        self.log.info('reload nginx config status:%s' % str(i))
                else:
                    self.log.info('reload nginx config status:%s' % str(nginx_server_status))
                return {"msg":nginx_server_status}
            return {"error":'Configuration check failed. Please inform the administrator to check the configuration file and the system.'}
        return {"error":update_status}

    def nignx_ssl_new(self,data):
        update_status = self.new_confg(data)
        if update_status == True:
            nginx_config_status = self.nginx_conf_check()
            if nginx_config_status is tuple:
                for i in nginx_config_status:
                    self.log.info('reload nginx config status:%s' % str(i))
            else:
                self.log.info('reload nginx config status:%s' % str(nginx_config_status))
            if nginx_config_status[0] == 0:
                nginx_server_status = self.restart_nginx_to_effective()
                if nginx_config_status is tuple:
                    for i in nginx_server_status:
                        self.log.info('reload nginx config status:%s' % str(i))
                else:
                    self.log.info('reload nginx config status:%s' % str(nginx_server_status))
                return {"msg":nginx_server_status}
            return {"error":'Configuration check failed. Please inform the administrator to check the configuration file and the system.'}
        return {"error":update_status}

    def update_conf(self,data):
        try:
            ca_key_path = self.nginxopt.downlaodcert(data["domain"],'certificate.pem',data["ca_key_down_link"])
            privte_key_path = self.nginxopt.downlaodcert(data["domain"],'privte.key',data["privte_key_down_link"])
            ningx_conf_obj = self.nginxopt.domian_find_nignx_conf(data["old_domain"])
            if ningx_conf_obj != 'error: Not matched':
                res = self.Domain_Differentiation(data, ningx_conf_obj[0], ningx_conf_obj[1],ca_key_path, privte_key_path)
                return res
            else:
                return self.new_confg(data)
        except Exception as e:
            if e is object:
                for i in e:
                    self.log.error(i)
            else:
                self.log.error(e)
            return "Writing data error"

    def Domain_Differentiation(self,data,dict_nginx_conf,conf_path,new_pem,new_key):
        if dict_nginx_conf != None:
            dict_nginx_conf['server_2'][5]["ssl_certificate"] = '%s;' % new_pem
            dict_nginx_conf['server_2'][6]["ssl_certificate_key"] = '%s;' % new_key
            dict_nginx_conf['server_1'][3]["server_name"] = '%s;' % data["domain"]
            dict_nginx_conf["server_2"][3]['server_name'] = '%s;' % data["domain"]
            new_conf_data = self.nginxopt.nginx_config_write_buffer_fomat(dict_nginx_conf)
            update_res = self.basesys.new_write_file(conf_path, new_conf_data)
            self.log.info('config:%s update:%s'%(conf_path,update_res))
            return update_res
        return "Read error in original configuration"

    def new_confg(self,data):
        try:
            ca_key_path = self.nginxopt.downlaodcert(data["domain"],'certificate.pem',data["ca_key_down_link"])
            privte_key_path = self.nginxopt.downlaodcert(data["domain"],'privte.key',data["privte_key_down_link"])
            new_conf = self.nginxopt.add_Anti_seal_conf(data["domain"], ca_key_path, privte_key_path)
            file_save_path = self.nginxopt.nginx_config_path.split(',')[0]
            filename = '%s.conf' % self.basesys.hex_time_uuid()
            file_path = '%s%s%s' % (file_save_path, self.basesys.osdircutflag(), filename)
            write_status = self.basesys.new_write_file(file_path, new_conf)
            return write_status
        except Exception as e:
            if e is object:
                for i in e:
                    self.log.error(i)
            else:
                self.log.error(e)
            return "Writing data error"

    def nginx_conf_check(self):
        '''
        Execute the system shell command and check the nginx config file.
        :return:
        '''
        command = 'nginx '
        options = '-t'
        cmd = self.basesys.CMD(command,options)
        if cmd != None:
            return cmd
        else:
            return 'ok'

    def restart_nginx_to_effective(self):
        '''
        Execute the system shell command and restart the nginx service.
        :return:
        '''
        command = 'systemctl restart '
        server_name = 'nginx'
        cmd = self.basesys.CMD(command,server_name)
        return cmd