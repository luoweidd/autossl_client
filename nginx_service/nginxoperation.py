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
        if update_status is True:
            conf_check_status = self.nginx_conf_check()
            if conf_check_status[0] == 0:
                nginx_server_status = self.restart_nginx_to_effective()
                self.log.info(nginx_server_status)
                return {"msg":"配置应用成功，并已生效。"}
            else:
                return {"error":conf_check_status}
        else:
            return {"error":update_status}

    def nignx_ssl_new(self,data):
        update_status = self.new_confg(data)
        if update_status is True:
            conf_check_status = self.nginx_conf_check()
            if conf_check_status[0] == 0:
                nginx_server_status = self.restart_nginx_to_effective()
                self.log.info(nginx_server_status)
                return {"msg":"配置应用成功，并已生效。"}
            else:
                return {"error":conf_check_status}
        else:
            return {"error":update_status}

    def update_conf(self,data):
        try:
            ca_key_path = self.nginxopt.certificate_write(data["domain"],'certificate.pem',data["ca_key"])
            privte_key_path = self.nginxopt.certificate_write(data["domain"],'privte.key',data["privte_key"])
            ningx_conf_obj = self.nginxopt.domian_find_nignx_conf(data["old_domain"])
            if ningx_conf_obj != 'error: Not matched':
                ningx_conf_obj['server_2'][5]["ssl_certificate"] = '%s;' % ca_key_path
                ningx_conf_obj['server_2'][6]["ssl_certificate_key"] = '%s;' % privte_key_path
                ningx_conf_obj['server_1'][3]["server_name"] = '*%s;' % data["domian"]
                ningx_conf_obj["server_2"][3]['server_name'] = '*%s;' % data["domian"]
                new_conf = self.nginxopt.nginx_config_write_buffer_fomat(ningx_conf_obj)
                write_status = self.basesys.new_write_file(ningx_conf_obj[1],new_conf)
                if write_status is not False:
                    self.log.info("Configuration Rewrite Successful")
                    return True
            else:
                new_conf = self.nginxopt.add_Anti_seal_conf(data["domain"],ca_key_path,privte_key_path)
                file_path = self.nginxopt.nginx_config_path
                if file_path is tuple:
                    write_status = self.basesys.new_write_file(file_path[0], new_conf)
                else:
                    write_status = self.basesys.new_write_file(file_path,new_conf)
                if write_status is not False:
                    return True
        except Exception as e:
            if e is object:
                for i in e:
                    self.log.error(i)
            else:
                self.log.error(e)
            return "Writing data error"

    def new_confg(self,data):
        try:
            ca_key_path = self.nginxopt.certificate_write(data["domain"],'certificate.pem',data["ca_key"])
            privte_key_path = self.nginxopt.certificate_write(data["domain"],'privte.key',data["privte_key"])
            new_conf = self.nginxopt.add_Anti_seal_conf(data["domain"], ca_key_path, privte_key_path)
            file_path = self.nginxopt.nginx_config_path
            if file_path is tuple:
                write_status = self.basesys.new_write_file(file_path[0], new_conf)
            else:
                write_status = self.basesys.new_write_file(file_path, new_conf)
            if write_status is not False:
                return True
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