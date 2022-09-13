
#在类前加装饰器【@ddt.ddt】表示当前类是一个数据驱动测试类
#ddt常用模块：
#     @ddt(申明当前类使用ddt框架),
#     @data(用于传参)，
#     @unpack(将参数解包，一般针对元组和列表)，
#     @data_file(ddt读取yaml/json文件)


# coding = utf-8
import unittest
import ddt

@ddt.ddt
class DataTest(unittest.TestCase):
    def setUp(self):
        print('这个是setUp')
    def tearDown(self):
        print('这个是tearDown')
    @ddt.data(
        [1,2],
        ['3','4'],
        ['5','6']
    )
    @ddt.unpack
    def test_add(self,a,b):
        print(a+b)

if __name__ == '__main__':
    unittest.main()