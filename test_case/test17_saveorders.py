# coding:utf-8

import unittest
import json
import urllib
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

userId = 514
token = 'DYfff3f213280a47d884ce983d8ed67a87'


class LOCALEBUY(unittest.TestCase):
    """用户保存订单"""
    def setUp(self):
        # self.base_url = 'http://test.api20write.hellodfs.com/users/514/orders'
        self.base_url = 'http://api20write.hellodfs.com/users/514/orders'
        payload = {
            'token': 'DYfff3f213280a47d884ce983d8ed67a87',
            'productdetail': '{"productdetail":[{"id":204,"num":2,"price":154},{"id":6120,"num":2,"price":109.82}]}',
            'flightid': '',
            'skipsc': '1'
        }
        self.params = payload

    def tearDown(self):
        pass

    def test17_saveorders(self):
        test_result = 'C:\\WORK\\workspace\\python\\LOCALEBUY\\report\\'
        filename = test_result + "\\" + 'result.txt'
        f = open(filename, 'a')
        self.params = urllib.urlencode(self.params)
        self.params = self.params.encode('ascii')
        r = urllib2.Request(self.base_url, self.params)
        r.add_header = ('Content-Type', 'application/x-www-form-urlencoded')
        text = urllib2.urlopen(r)
        hjson = json.loads(text.read().encode('utf8'))
        try:
            self.assertIn(u'code', hjson) and self.assertIn('0', hjson)
        except AssertionError:
            print hjson

        f.write("case17:用户保存订单"+'\n'+'\n'+str(hjson)+'\n'+'\n'+'\n')
        f.close()

if __name__ == "__main__":
    unittest.main()
