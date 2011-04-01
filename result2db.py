#encoding=utf-8
import pymssql
import sys
common_sample_attribute = {}
def init():
    common_sample_attribute['id'] = 'sample_id'
    common_sample_attribute['type'] = 'type'
    common_sample_attribute['method'] = 'method'
    common_sample_attribute['status'] = 'status'
    common_sample_attribute['start_time'] = 'start_time'
    common_sample_attribute['end_time'] = 'end_time'
    common_sample_attribute['status'] = 'status'
    common_sample_attribute['timeout'] = 'timeout'
    common_sample_attribute['log'] = 'log'
init()
class Result2DB:
    #通用的sample属性
    #common_sample_attribute = {'id':'sample_id','type':'type','method':'method','status':'status','log':'log'}
    def __init__(self,config=None):
        if not getattr(self,'conn',None):
            if not config:
	        d = {'host':'127.0.0.1:1433','user':'sa','password':'sa','database':'test'}
                self.conn = pymssql.connect(**d)
	    elif config.__class__ is dict:
	        self.conn = _mssql.connect(**config)
	    elif config.__class__ in [tuple,list]:
	        self.conn = _mssql.connect(*config)
	#self.conn.debug_queries = True
        self.conn.autocommit(False)

    def insert(self,result):
        try: 
            test_id = self.test_insert(result)
	    print result.sections
	    for rs in result.sections:
	  
	        if rs.nodetype in [u'sample','sample']:
	            sample_id = self.sample_common_insert(rs,test_id)
                    self.sample_attr_insert(rs,sample_id)
	        else:
		    print '==================insert assert====================='
	            self.assert_insert(rs,test_id)
	    
	    self.conn.commit()
        except:
	    print sys.exc_info() 
	    #print sys.exc_info()
	    print '===============error========================'
	    import traceback
	    for filename, lineno, function, msg in traceback.extract_tb(sys.exc_info()[2]):
	        print '%s line %s in %s function [%s]'%(filename,lineno,function,msg)
	    print '===============error========================'
	    self.conn.rollback()
	finally:
	    self.conn.close()

    def test_insert(self,result):
        cur = self.conn.cursor()
        #name,staus,start_time,end_time = result.nodename,result.status,result.start_time,result.end_time
        params = ()
	params += (result.nodename,)
        params += (result.status,)
        params += (result.start_time.__str__()[:-3],)
	params += (result.end_time.__str__()[:-3],)

        print params
	print len(params)
	sql = 'insert into tb_test values('
	for i in range(len(params)):
	    sql +='%s,'
	sql = sql[:-1]
	sql += ')'
	print sql
	#cur.execute('insert into tb_test values(%s)',params)
        cur.execute(sql,params)
        test_id = cur.lastrowid
	print 'the last test inserted identify is ',test_id
	cur.close()
	return test_id

    def sample_common_insert(self,rs,test_id):
        #params = (rs._sample.id,rs._sample.type,rs._sample.method,rs._sample.timeout,rs.log,rs.start_time,rs.end_time,rs.status,test_id)
        cur = self.conn.cursor()
	params = ()
        params += (rs._sample.id,)
        params += (rs._sample.type,)
        params += (rs._sample.method,)
        params += (rs._sample.timeout,)
	if rs.log:params += (1,)
        else:params += (0,)
        params += (rs.start_time.__str__()[:-3],)
        params += (rs.end_time.__str__()[:-3],)
        params += (rs.status,)
        params += (int(test_id),)
	sql = 'insert into tb_sample values('
	for i in range(len(params)):
	    sql += '%s,'
	sql = sql[:-1]
	sql += ')'
	print sql
	print params
	cur.execute(sql,params)
        #cur.execute('insert into tb_sample values (%s)',params)

	sample_id = cur.lastrowid
	#返回最后一次插入的标识符
	print 'the last sample inserted identify is ',sample_id
	cur.close()
	return sample_id
    
    def assert_insert(self,rs,test_id):
        cur = self.conn.cursor()
        params = ()
        params += (rs._assert.type,)
        params += (rs.status,)
        params += (int(test_id),)
	sql = 'insert into tb_assert values('
	for i in range(len(params)):
	    sql +='%s,'
	sql = sql[:-1]
	sql += ')'
	print sql
	cur.execute(sql,params)
        #cur.execute('insert into tb_sample values (%s)',params)
	cur.close()

   
    def sample_attr_insert(self,rs,sample_id):
        cur = self.conn.cursor()
        for (k,v) in rs._sample.__dict__.items():
	    if not common_sample_attribute.has_key(k):
	        if '_' not in k and v.__class__ in [str,int,float,unicode]:
		    sql = 'insert into tb_sample_attribute values (%s,%s,%s)'
                    params = (int(sample_id),)
                    params += (k,)
                    params += (v,)
	            cur.execute(sql,params) 
	cur.close()
        
