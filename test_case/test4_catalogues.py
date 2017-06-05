# coding:utf-8

import unittest
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

userId = 514
token = 'DYfff3f213280a47d884ce983d8ed67a87'


class LOCALEBUY(unittest.TestCase):
    """获取指定的分类方案的整棵分类树"""
    def setUp(self):
        # self.base_url = 'http://test.api20read.hellodfs.com/catalogues'
        self.base_url = 'http://api20read.hellodfs.com/catalogues'

    def tearDown(self):
        pass

    def test4_catalogues(self):
        test_result = 'C:\\WORK\\workspace\\python\\LOCALEBUY\\report\\'
        filename = test_result + "\\" + 'result.txt'
        f = open(filename, 'a')
        r = requests.get(self.base_url)
        code = r.status_code
        try:
            self.assertEqual(code, 200)
        except AssertionError:
            print code

        text = r.text
        try:
            self.assertIn(u'成功', text)
        except AssertionError:
            print text

        hjson = json.loads(r.text.encode('utf-8'))
        try:
            self.assertIn(u'code', hjson)
        except AssertionError:
            print hjson

        # f.write(str(code)+'\n')
        f.write("case4:获取指定的分类方案的整棵分类树"+'\n'+'\n'+str(text)+'\n'+'\n'+'\n')
        # f.write(str(hjson)+'\n')
        f.close()

if __name__ == "__main__":
    unittest.main()
