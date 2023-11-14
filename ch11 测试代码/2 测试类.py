# Yu Junming
# 14/11/2023
# chapter 11 测试代码  2 测试类
# 《Python编程从入门到实践》


# 几个断言方法
# assertEqual(a, b)     assertNotEqual(a, b)
# assertTrue(x)     assertFalse(x)
# assertIn(item, list)      assertNotIn(item, list)

import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试。"""

    def setUp(self):
        """创建一个调查对象和一组答案，给测试方法使用。"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Chinese', 'Japanese']

    def test_store_single_response(self):
        """测试单个答案会被妥善地保存。"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地保存。"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()

