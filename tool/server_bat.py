import winrm

from tool.get_log import GetLogger

log = GetLogger.get_log()


class WinRM:
    def __init__(self, ip='192.168.128.128', username='bian', password='123456'):
        self.win = winrm.Session(
            'http://' + ip + ':5985/wsman',
            auth=(username, password)
        )
        log.info(f"连接远程计算机，ip{ip},用户名{username},密码{password}")

    def reboot(self):
        self.win.run_cmd('shutdown -r')  # 使用run_cmd()函数执行命令

    def shutdown(self):
        self.win.run_cmd('shutdown -s')

    def get_info_result(self, cmd):
        out_info = self.win.run_cmd(cmd).std_out.decode(encoding='UTF-8')
        err_info = self.win.run_cmd(cmd).std_err.decode(encoding='UTF-8')
        status_info = self.win.run_cmd(cmd).status_code
        print('out_info:', out_info)
        print('error_info:', err_info)
        print('status_code:', status_info)
        return out_info, err_info, status_info

    def run_bat_file(self):
        log.info(f"执行命令：文件clear_session.bat，清理服务器缓存")
        result = self.win.run_cmd(r'C:\Users\bian\Desktop\clear_session.bat')
        # print('清理服务器缓存成功')
        print('out_info:', result.std_out.decode(encoding='UTF-8'))
        print('error_info:', result.std_err.decode(encoding='UTF-8'))
        print('status_code:', result.status_code)


if __name__ == '__main__':
    WinRM().run_bat_file()
