
import os
import unittest
import tempfile

from nms.core.context import ContextCreator
from my_flaskr import my_flaskr 



class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        my_flaskr.app.config['TESTING'] = True
        self.app = my_flaskr.app.test_client()
        context_creator = ContextCreator('buer')
        self.context = context_creator.from_file()

    def test_empty_list_of_devices(self):
        """"""
        for url in ['/', '/index']:
            rv = self.app.get(url)
            string_with_data = str(rv.data)
            for device in self.context.devices:
                self.assertTrue(device in string_with_data)

    def test_empty_list_of_parameters(self):
        """ """
        for url in ['/', '/index']:
            rv = self.app.get(url)
            string_with_data = str(rv.data)
            for device in self.context.devices:
                for param in self.context.devices[device].params_dict:
                    self.assertTrue(param in string_with_data)
    
if __name__ == '__main__':
    unittest.main()

