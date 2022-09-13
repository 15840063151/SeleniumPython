

# conding = utf-8
import logging
import os
import datetime

class UserLog():
    def __init__(self):
        self.logger = logging.getLogger()      #Logger是一个树形层级结构，在使用接口 debug，info，warn，error，critical 之前必须创建 Logger 实例;创建方法: logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)    #设置日志级别为 ERROR  #日志级别等级排序：critical > error > warning > info > debug  例如：logger.setLevel(logging.ERROR) 即只有日志级别大于等于 ERROR 的日志才会输出

        # 控制台输出日志
        #consle = logging.StreamHandler()  #创建了一个流对象; # Handler 处理器类型比较常用的有三个，StreamHandler，FileHandler，NullHandler
        #self.logger.addHandler(consle)         #添加流（往控制台输出的流）   #logger.addHandler(handler_name) # 为 Logger 实例增加一个处理器
        #self.logger.debug("info")

        #文件名字
        base_dir = os.path.dirname(os.path.abspath(__file__))     # os.path.abspath(__file__)作用：获取当前脚本的完整路径;   os.path.dirname(path) 去掉文件名，返回目录
        log_dir = os.path.join(base_dir,"logs")
        log_file = datetime.datetime.now().strftime('%Y-%m-%d')+'.log'
        log_name = log_dir + '/' + log_file

        #文件输出日志
        # file_handle = logging.FileHandler(log_name)
        # formatter = logging.Formatter('%(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s ----> %(message)s ') # 定义日志格式
        # file_handle.setFormatter(formatter)     # 将file_handle赋予日志格式
        # self.logger.addHandler(file_handle)


        self.file_handle = logging.FileHandler(log_name)
        self.file_handle.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s ----> %(message)s ') # 定义日志格式
        self.file_handle.setFormatter(formatter)     # 将file_handle赋予日志格式
        self.logger.addHandler(self.file_handle)

        self.logger.debug('test')
                          
        self.logger.removeFilter(self.file_handle)      #logger.removeHandler(handler_name) # 为 Logger 实例删除一个处理器
        self.file_handle.close() 

    def get_log(self):
        return self.logger
 
        
    def close_handle(self):
        self.logger.removeFilter(self.file_handle)      #logger.removeHandler(handler_name) # 为 Logger 实例删除一个处理器
        self.file_handle.close() 

if __name__ == '__main__':
    user = UserLog()
    log = user.get_log()
    log.debug('test0902')