# -*- coding: utf-8 -*-  
import pymysql
import sys
class zabbix2aom(object):
    
    def __init__(self):
        dbcon={
                'host':'10.68.3.99',
                'port':3306,
                'user':'root',
                'password':'root123',
                'database':'aom',
                'charset':'utf8' ,
                'cursorclass':pymysql.cursors.DictCursor,
                }

        self.db=pymysql.connect(**dbcon)
        self.task=eval(sys.argv[1])
        
    def run(self):
        if self._isExistsWarn(**self.task):
            self.task['userid']=str(self.getUserid(**self.task)['userid'])
            self.createWarn(**self.task)
            self.task['wid']=str(self.getLaseID()['lastid'])
            self.createMsg(**self.task)
            self.task['messid']=str(self.getLaseID()['lastid'])
            self.setWarnMsgId(**self.task)
        else:
            self.setWarnStatus(**self.task)
        self.db.commit()
        self.db.close()
    
    def setWarnMsgId(self,**kwages):
        sql="update pps_warntask set messid=%s where id=%s"%(kwages['messid'],kwages['wid'])
        print(sql)
        self.putData(**{'sql':sql})
    
    def getUserid(self,**kwages):
        sql="select userid from pps_warntype where warntype='%s'"%(kwages['type'])
        print(sql)
        temp=self.getData(**{'sql':sql})
        if len(temp)>0:
            return(temp[0])
        else:
            return({'userid':1})
            
    def _isExistsWarn(self,**kwages):
        sql="select count(*) count from pps_warntask where warnid='%s'"%(kwages['id'])
        print(sql)
        if self.getData(**{'sql':sql})[0]['count']>0:
            return(False)
        else:
            return(True)
    
    def createMsg(self,**kwages):
        sql="insert into pps_message(createtime,activityname,path,userid,status) values(now(),'%s','%s',%s,1)"%(kwages['type']+'预警','/pps/dowarn/?id='+kwages['wid'],kwages['userid'])
        print(sql)
        self.putData(**{'sql':sql})
        
    def createWarn(self,**kwages):
        sql="insert into pps_warntask(warnid,warntype,enviname,warndesc,warnlevel,createtime,status,userid)values(%s,'%s','%s','%s','%s',now(),1,%s)"%(kwages['id'],kwages['type'],kwages['evn'],kwages['msg'],kwages['level'],kwages['userid'])
        print(sql)
        self.putData(**{'sql':sql})    
        
    def setWarnStatus(self,**kwages):
        sql="update pps_warntask set recoverytime=now() where warnid=%s" %(kwages['id'])    
        self.putData(**{'sql':sql})  
        
    def getLaseID(self):
        return(self.getData(**{'sql':'SELECT LAST_INSERT_ID() lastid'})[0])  
        
    def getData(self,**kwages):     
        cur=self.db.cursor()
        cur.execute(kwages['sql'])
        return(cur.fetchall())
        
    def putData(self,**kwages):
        cur=self.db.cursor() 
        cur.execute(kwages['sql'])
    def test(self,):
        with open('/etc/zabbix/alertscripts/msg1.log','a')as myfile:
            myfile.write(sys.argv[1]+'\n')		
			
def main():
    r=zabbix2aom()
    r.run()
	
if __name__ == '__main__':
    main()
