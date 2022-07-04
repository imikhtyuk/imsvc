import os
from unittest import TestCase
from app import app

class test_case__appservice(TestCase):

    def test____appservice_wrong_url(self):
        os.environ["INPUT_DATA_URL"] = 'http://www.bom.gov.au/fwo/IDN60801/__wrong_path__.json'
        res, code = app.process_data()
        self.assertTrue(res == {'error': 'Error Connecting to BOM.'})
        self.assertTrue(code == 503)

    def test____appservice_nonempty(self):
        os.environ["TEMP_FILTER_THRESHOLD"] = '0'
        res, code = app.process_data()
        self.assertTrue(len(res['response']) > 0)
        self.assertTrue(code == 200)

    def test____appservice_empty(self):
        os.environ["TEMP_FILTER_THRESHOLD"] = '200'
        res, code = app.process_data()
        self.assertTrue(len(res['response']) == 0)
        self.assertTrue(code == 200)

    def test____appservice_filter_order(self):
        os.environ["TEMP_FILTER_THRESHOLD"] = '10'
        res, code = app.process_data()
        self.assertTrue(res['response'][0]['apparent_t'] <= res['response'][-1]['apparent_t'])
