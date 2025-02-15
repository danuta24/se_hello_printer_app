import unittest
import json
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output(self):
        test_data={"imie": "Danusia", "msg": "Hello World!"}
        rv = self.app.get('/?output=json')
        js = json.loads(rv.data)
        self.assertEqual(test_data["imie"], js["imie"])
        self.assertEqual(test_data["msg"], js["msg"])

    def test_msg_with_xml_output(self):
        rv = self.app.get('/?output=xml')
        s = b'<greetings><imie>Danusia</imie> <msg>Hello World!</msg></greetings>'
        self.assertEqual(s, rv.data)

#<imie>Danusia</imie><msg>Hello World!</msg>',rv.data)
#Zmiany
