
import json
import sys
import unittest

sys.path.append('/Users/Raj/Documents/GitHub/web-dev /FOSE/jsonapi/src/jsonapi')
import jsonapi


class TestGetAreaRectangle(unittest.TestCase):

    def test_encode_range_number(self) :
                  
                  abc = range(1, 2, 3)
                  encoded_range = json.dumps(abc, cls = jsonapi.MyEncoder)
                  self.assertEqual(encoded_range, '{"start": 1, "stop": 2, "step": 3, "__extended_json_type__": "range"}')



    def test_decode_range_number(self)  :
                 abc = range(1, 2, 3)
                 encoded_range = json.dumps(abc, cls = jsonapi.MyEncoder)
                 decoded_range = json.loads(encoded_range, cls =jsonapi.MyDecoder)
                 assert decoded_range == abc
    

    def test_encode_complex_number(self) :
            clmpx = complex(1,2)
            encoded_complex = json.dumps(clmpx, cls = jsonapi.MyEncoder)
            self.assertEqual(encoded_complex, '{"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}')

    def test_decode_cmplx_number(self) :
            clmpx = complex(1,2)
            encoded_cmplx = json.dumps(clmpx, cls = jsonapi.MyEncoder)
            decoded_cmplx = json.loads(encoded_cmplx, cls = jsonapi.MyDecoder)
            assert decoded_cmplx == clmpx

unittest.main()