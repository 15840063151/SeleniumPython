


# coding = utf-8
import unittest

class SecondCase(unittest.TestCase):

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

    def test_three(self):
        print('这事第三个case')
    def test_four(self):
        print('这是第四个case')

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()       #创建一个测试套件
    suite.addTest(SecondCase('test_three'))
    suite.addTest(SecondCase('test_four'))
    unittest.TextTestRunner().run(suite)