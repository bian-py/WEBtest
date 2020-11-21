import os
import threading

#使用grid之前先将conftest文件释放
for browser in ['ie', 'firefox', 'chrome']:
    cmd = 'pytest --html=./report_html_%s/%s_report.html --b %s ' % (browser, browser,browser)
    print(cmd)
    threading.Thread(target=os.system, args=(cmd,)).start()
