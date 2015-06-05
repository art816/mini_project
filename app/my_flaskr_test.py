
import os
import my_flaskr
import unittest
import tempfile

import sys
sys.path.append('../../NMS')

from nms.core.context import ContextCreator



class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        #self.db_fd, flaskr.app.config[’DATABASE’] = tempfile.mkstemp()
        my_flaskr.app.config['TESTING'] = True
        self.app = my_flaskr.app.test_client()
        context_creator = ContextCreator('buer')
        self.context = context_creator.from_file()

        #flaskr.init_db()
    
    #def tearDown(self):
     #   os.close(self.db_fd)
      #  os.unlink(flaskr.app.config[’DATABASE’])


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

