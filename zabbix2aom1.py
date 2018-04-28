# -*- coding: utf-8 -*-  
import urllib2
import json
import sys
import traceback
import time
class zabbix2aom(object):
    
    def __init__(self):
        self.url='http://yw.51xtong.com/pps/api/'
        self.task={'task':'warntask','data':eval(str(sys.argv[1].replace('\n','\\n')))}
        self.data=self.task
        
    def run(self):
        self.post()
	
    def post(self,**kwage):
        headers = {'Content-Type': 'application/json'}
        request = urllib2.Request(url=self.url, headers=headers, data=json.dumps(self.data))
        response = urllib2.urlopen(request,timeout = 3)  
        print(response.read())  
        
def main():
    try:
        r=zabbix2aom()
        r.run()
    except Exception as info: 
        error=traceback.format_exc()
        print(error)
        with open('/etc/zabbix/alertscripts/msg1.log','a')as myfile:
            myfile.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+'\n')
            myfile.write(error+'\n')

if __name__ == '__main__':
    main()
