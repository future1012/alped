import  unittest

from name_function import  get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能正确处理TengYue这样的名字吗"""
        formatted_name = get_formatted_name('teng','yue')
        self.assertEquals(formatted_name, 'Teng Yue')

unittest.main()