

# 单元测试时编写的测试用例就是继承TestCase类来实现具体的测试用例。
# 每个继承TestCase的子类里面实现的具体方法（以test开头的方法）都有一条用例

# unittest--unittest.defaultTestLoader()的方法(智能获取文件下面的case去跑的方法) 
# discover(self, start_dir, pattern='test*.py', top_level_dir=None):  1）start_dir：路径   2）pattern='test*.py' 匹配规则：需要匹配什么类型的py文件
# defaultTestLoader()类，通过该类下面的discover()方法可自动根据测试目录start_dir匹配查找测试用例文件（test*.py），并将查找到的测试用例组装到测试套件

# os.getcwd() 方法用于返回当前工作目录
# os.path.join()函数：连接两个或更多的路径名组件

# coding = utf-8
import unittest
import os
class RunCase(unittest.TestCase):
    def test_case_first(self):
        case_path = os.path.join(os.getcwd(),'case')
        suit = unittest.defaultTestLoader.discover(case_path,'unittest_*.py')
        unittest.TextTestRunner().run(suit)

if __name__ == '__main__':
    unittest.main()
