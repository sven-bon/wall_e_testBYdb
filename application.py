#encoding=utf-8

import urllib,urllib2
from walle.monitor import Monitor
from walle.config import Config
from result2db import Result2DB
if __name__ == '__main__':
    # 演示结果处理器可以配置
    #setattr(Config,'testdir','testcases')
    #setattr(Config,'testResult_dir','D:\\jeffkit-wall-e-52c70c8\\testcase\\testcase\\rs')
    #Config.__setattr__('testdir','testcases')
    
    class Handler:
        pass
    rh = Handler()
    rh.hl = Result2DB()
    setattr(rh,'handle',lambda x:rh.hl.insert(x))
    
    Monitor(config=Config,result_handler=rh).run()

