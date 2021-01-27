import unittest
from josephus_function import josephus_function


class JosephusFunctionTestCase(unittest.TestCase):
    """测试约瑟夫函数"""

    def test_josephus_function_normal_input(self):
        """能够正确处理人数为10，开始位置为4，步长为4的输入吗？"""
        result = josephus_function(10, 4, 4)
        expect_value = ([7, 1, 5, 10, 6, 3, 2, 4, 9], 8)
        self.assertEqual(result, expect_value)
    
    def test_josephus_function_informal_input_1(self):
        """能够正确处理输入参数中有0的错误吗"""
        result = josephus_function(0, 10, 1)
        expect_value = "请输入正整数参数"
        self.assertEqual(result, expect_value)
    
    def test_josephus_function_informal_input_2(self):
        """能够处理输入参数中含有字符的错误吗"""
        result = josephus_function(10, "四", 4)
        expect_value = "请输入整数参数(阿拉伯数字)"
        self.assertEqual(result, expect_value)

    def test_josephus_function_informal_input_3(self):
        """能够处理输入参数中含有负数的错误吗"""
        result = josephus_function(10, -4, 4)
        expect_value = "请输入正整数参数"
        self.assertEqual(result, expect_value)

    def test_josephus_function_informal_input_4(self):
        """能够处理输入参数中含有小数的错误吗"""
        result = josephus_function(10, 6.0, 5)
        expect_value = "请输入整数参数(阿拉伯数字)"
        self.assertEqual(result, expect_value)


unittest.main
