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
import re

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
            ca_key_path = self.nginxopt.downlaodcert(data["domain"],data["ca_key_down_link"],'certificate.pem')
            privte_key_path = self.nginxopt.downlaodcert(data["domain"],data["privte_key_down_link"],'privte.key')
            ningx_conf_obj = self.nginxopt.domian_find_nignx_conf(data["old_domain"])
            if ningx_conf_obj != 'error: Not matched':
                self.Domain_Differentiation(data, ningx_conf_obj, ca_key_path, privte_key_path)
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

    def Domain_Differentiation(self,data,dict_nginx_conf,new_pem,new_key):
        if re.match('^\.', data["old_domain"]):
            if dict_nginx_conf != 'error: Not matched' and re.match('\*\.%s;' % data["old_domain"],
            dict_nginx_conf['server_1'][3]["server_name"]) and re.match('\*\.%s;' % data["old_domain"][1::],
            dict_nginx_conf["server_2"][3]['server_name']):
                dict_nginx_conf['server_2'][5]["ssl_certificate"] = '%s;' % new_pem
                dict_nginx_conf['server_2'][6]["ssl_certificate_key"] = '%s;' % new_key
                dict_nginx_conf['server_1'][3]["server_name"] = '*%s;' % data["domian"]
                dict_nginx_conf["server_2"][3]['server_name'] = '*%s;' % data["domian"]
                wirte_res = self.wirteconf(dict_nginx_conf)
                return wirte_res
        else:
            if dict_nginx_conf != None and re.match('%s;' % data["old_domain"],
               dict_nginx_conf['server_1'][3]["server_name"]) and re.match(
               '%s;' % data["old_domain"], dict_nginx_conf["server_2"][3]['server_name']):
                dict_nginx_conf['server_2'][5]["ssl_certificate"] = '%s;' % new_pem
                dict_nginx_conf['server_2'][6]["ssl_certificate_key"] = '%s;' % new_key
                dict_nginx_conf['server_1'][3]["server_name"] = '%s;' % data["domian"]
                dict_nginx_conf["server_2"][3]['server_name'] = '%s;' % data["domian"]
                wirte_res = self.wirteconf(dict_nginx_conf)
                return wirte_res

    def wirteconf(self,dict_nginx_conf):
        new_conf_data = self.nginxopt.nginx_config_write_buffer_fomat(dict_nginx_conf)
        update_res = self.basesys.new_write_file(dict_nginx_conf[1], new_conf_data)
        self.log.error(update_res)
        if update_res == 'ok':
            nginx_config_status = self.nginxopt.nginx_conf_check()
            self.log.error(nginx_config_status)
            if nginx_config_status[0] == 0:
                nginx_server_status = self.nginxopt.restart_nginx_to_effective()
                self.log.info(nginx_server_status)
                return nginx_server_status
            self.log.info('配置检查不通过，请通知管理员检查配置文件，以及系统。错误信息：%s' % nginx_config_status[1])
            return '配置检查不通过，请通知管理员检查配置文件，以及系统。'
        return '更新配置文件错误。'


    def new_confg(self,data):
        try:
            ca_key_path = self.basesys.downlaodcert(data["domain"],data["ca_key_down_link"],'certificate.pem')
            privte_key_path = self.basesys.downlaodcert(data["domain"],data["privte_key_down_link"],'privte.key')
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