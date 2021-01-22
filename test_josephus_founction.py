import unittest
from josephus_function import josephus_function

class JosephusFunctionTestCase(unittest.TestCase):
    """测试约瑟夫函数"""

    def test_josephus_function_normal_input(self):
        """能够正确处理人数为10，开始位置为4，步长为4的输入吗？"""
        result = josephus_function(10,4,4)
        self.assertEqual(result,([7,1,5,10,6,3,2,4,9],8))
    
    def test_josephus_function_nonnormal_input_1(self):
        """能够正确处理输入参数中有0的异常吗"""
        result = josephus_function(0,10,1)
        self.assertEqual(result,"请输入不为零的参数")
    
    def test_josephus_function_nonnormal_input_2(self):
        """能够处理输入参数中含有字符的异常吗"""
        result = josephus_function(10,"四",4)
        self.assertEqual(result,"请输入阿拉伯数字（整数）")

    def test_josephus_function_nonnormal_input_3(self):
        """能够处理输入参数中含有负数的异常吗"""
        result = josephus_function(10,-4,4)
        self.assertEqual(result,"请输入正整数")

    def test_josephus_function_nonnormal_input_4(self):
        """能够处理输入参数中含有小数的异常吗"""
        result = josephus_function(10,6.0,5)
        self.assertEqual(result,"请输入阿拉伯数字（整数）")


unittest.main()