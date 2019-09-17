from unittest import TestCase
import app


class TestDecode(TestCase):

    def test_decode(self):
        token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9' \
                '.eyJsb2NhdGlvbiI6IkxlZWRzIiwiYXBwSUQiOiJjMDI0ZTg1Y2VmOGYwZmM5MjhjM2YwZWY4NWQ3YWQwMCJ9.y5w4khCBL' \
                '-iBkSyjgLfmMcGImc7UdCmSAXaK5ZmyG6M '
        key = 'm.m@tesco.com'
        result = app.decode(token, key)
        print(result['location'])
        self.assertEqual(result['location'], "Leeds")
