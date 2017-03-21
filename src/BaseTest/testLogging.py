import logging

# 日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，当然也可以自己定义日志级别。
# 通过logging.basicConfig函数对日志的输出格式及方式做相关配置
# 参考 http://www.cnblogs.com/dkblog/archive/2011/08/26/2155018.html
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='w')   #可以改写到配置文件中

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
