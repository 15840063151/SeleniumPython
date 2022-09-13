
# case必须以test开始

# setUp：表示前置条件，它在每一个用例执行之前必须会执行一次
# setUp可以理解为我们需要自动化测试时，需要打开网页窗口，输入对应测试地址，这一些属于前置条件
# tearDown：表示释放资源，它在每次用例执行完之后会执行一次
# tearDown可以理解为我们测试完毕后，需要关闭浏览器

#setUpClass()：所有的测试方法运行前运行，为单元测试做前期准备，但必须使用@classmethod装饰器进行修饰，整个测试过程中只执行一次
#tearDownClass()：所有的测试方法运行结束后运行，为单元测试做后期清理工作，但必须使用@classmethod装饰器进行修饰，整个测试过程中只执行一次。


# coding = utf-8
import unittest

class FirstCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('所有case执行之前的前置')

    @classmethod
    def tearDownClass(cls):
        print('所有case执行之后的后置')

    def setUp(self):
        print("每一条case的前置条件")

    @unittest.skip('不执行')    
    def tearDown(self):
        print("每一条case的后置条件")

    def test_first(self):
        print('这事第一个case')
    def test_second(self):
        print('这是第二个case')

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()       #创建一个测试套件
    suite.addTest(FirstCase('test_second'))
    suite.addTest(FirstCase('test_first'))
    unittest.TextTestRunner().run(suite)

# 构建测试套件的方法之一，通过unittest.TestSuite()类直接构建，或者通过TestSuite实例的addTests、addTest方法构建
# TextTestRunner ——> 1）作用，执行suite中的测试用例 2）使用方法：--先实例化TextTestRunner()实例对象； --调用对象的run方法； --只要把suite作为参数传递到run方法；

# case默认执行顺序：unittest执行测试用例，默认是根据ASCII码的顺序加载测试用例，数字与字母的顺序为：0-9，A-Z，a-z。
# 同过addTest() 的顺行进行执行

# @unittest.skip('reason') ,强制跳转,不执行

