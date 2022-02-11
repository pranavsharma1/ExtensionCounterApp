import json
import unittest
from os import path
from app import log_reader
from app import extension_counter
from app.extension_counter import ExtensionCounter
from app.log_reader import LogFileReader


class TestApp(unittest.TestCase):
    ''' A class representing all the the unit tests.'''


    base_path = path.abspath(path.curdir)

    def test_read_file_success(self, basePath=base_path):
        ''' Test when file is read, records are json records are stored as a list'''
        listJson = LogFileReader.read_log_file(self, basePath + '/data/sampleValidData.json')

        self.assertIsInstance(listJson, list)
        self.assertEqual(len(listJson), 7)

    def test_read_file_fail(self, basePath=base_path):
        '''Test that it does not read a file that does not exist'''

        path = basePath + '/data/sampleNegativeData.json'
        fr = LogFileReader.read_log_file(self, path)
        self.assertIsNone(fr)

    def test_extension_counter_success(self, basePath=base_path):
        ''' Test that extension counter calculates the accurate count of extension read in the input log file'''

        listJson = LogFileReader.read_log_file(self, basePath + '/data/sampleValidData.json')
        self.assertEqual(ExtensionCounter.get_extension_count(self, listJson),
                         {'ext': 2, 'pdf': 1, 'exe': 1, 'pdf': 1, 'py': 1, 'ts': 1})

    def test_extension_counter_no_input_file_fail(self, basePath=base_path):
        '''Test the file does couunt extensions for a file that does not exist'''

        path = basePath + '/data/sampleNegativeData.json'
        fr = LogFileReader.read_log_file(self,path)
        self.assertRaises(TypeError, ExtensionCounter.get_extension_count, fr)

    def test_nm_key_fail(self, basePath=base_path):
        '''Test that the 'nm' key is not missing from the json record'''

        path = basePath + '/data/sampleMissingKeyData.json'
        fr = LogFileReader.read_log_file(self, path)
        self.assertRaises(KeyError, ExtensionCounter.get_extension_count,self, fr)

    def test_invalid_json_element(self, basePath=base_path):
        '''Test that the record has a valid json'''

        path = basePath + '/data/sampleInvalidData.json'
        fr = LogFileReader.read_log_file(self, path)
        self.assertRaises(json.decoder.JSONDecodeError, ExtensionCounter.get_extension_count,self, fr)


unittest.main()
