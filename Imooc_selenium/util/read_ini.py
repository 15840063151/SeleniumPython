
# 读取配置文件(LocalElement.ini)  返回格式： id>register_email

# coding = utf-8

#class ReagIni(): 
#    cf = configparser.ConfigParser()
#    cf.read(r"F:\selenium_python\Imooc_selenium\config\LocalElement.ini")
#    print(cf.get('RegisterElement','user_email'))

import configparser
class ReadIni():
    def __init__(self,key,file_name=None,node=None):
        self.key = key
        if file_name == None:
            self.file_name = "F:\selenium_python\Imooc_selenium\config\LocalElement.ini"
        else:
            self.file_name = file_name
        if node == None:
            self.node = "RegisterElement"
        else:
            self.node = node

    def get_value(self):
        cf = configparser.ConfigParser()
        cf.read(self.file_name,encoding='utf-8')
        value = cf.get(self.node,self.key)
        return value


if __name__ == "__main__":
    read_init = ReadIni("user_name")
    read_init.get_value()





# class ReadIni():

#     def __init__(self,file_name=None,node=None):
#         if file_name == None:
#             file_name = "F:/selenium_python/Imooc_selenium/config/LocalElement.ini"
#         self.cf = self.load_ini(file_name)
#         if node == None:
#             self.node = "RegisterElement"
#         else:
#             self.node = node
#     # 加载文件
#     def load_ini(self,file_name):
#         cf = configparser.ConfigParser()
#         cf.read(file_name)
#         return cf
#     # 获取value值
#     def get_value(self,key):
#         data = self.cf.get(self.node,key)
#         return data


# if __name__ == '__main__':
#     read_init = ReagIni()
#     print(read_init.get_value('user_name'))