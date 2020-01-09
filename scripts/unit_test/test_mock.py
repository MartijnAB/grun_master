"""
   unit test program for createfile.py
   usage: python3 -m unittest test_mock.py

"""

__author__ : 'Periklis Gkolias'

import unittest
from unittest import mock
from fs_handler import *


class FileSystemHandlerTest(unittest.TestCase):
    def setUp(self):
        """setUp is run before each test case.
        It is usually used to setup() some common
        values for all test cases"""
        print('setUp: Initialize instance variables')
        self.directory = ''
        self.new_filename = 'dummy_new_filename.txt'
        self.full_path = os.path.join(self.directory,
        self.new_filename)


    def tearDown(self):
        print('tearDown: Reset instance variables')
        self.directory = ''
        self.new_filename = ''


    """The patch() decorator / context manager makes it easy
    to mock classes or objects in a module under test.
    The object you specify will be replaced with a mock
    during the test and restored when the test ends"""
    #Locate the function check_file_exists from fs_handler and
    #as long we are in the scope of the function below(namely fs_handler)
    # whenever check_file_exists is invoked, use a mock object
    #called mock_check_file_exists instead.
    @mock.patch('builtins.open', mock=mock.mock_open)
    @mock.patch('fs_handler.check_file_exists')
    @mock.patch('fs_handler.check_dir_exists')
    def test_create_file_success(self, mock_check_dir_exists, mock_check_file_exists, mock_open_func):
        print('test_create_file_success')
        mock_check_dir_exists.return_value = True
        mock_check_file_exists.return_value = False
        self.assertTrue(create_file(self.directory, self.new_filename))


    @mock.patch('builtins.open', mock=mock.mock_open)
    @mock.patch('fs_handler.check_file_exists')
    @mock.patch('fs_handler.check_dir_exists')
    def test_create_file_failure_dir_no_exists(self, mock_check_dir_exists, mock_check_file_exists, mock_open_func):
        print('test_create_file_failure_dir_no_exists')
        mock_check_dir_exists.return_value = False
        mock_check_file_exists.return_value = False
        self.assertFalse(create_file(self.directory,self.new_filename))


    @mock.patch('builtins.open', mock=mock.mock_open)
    @mock.patch('fs_handler.check_file_exists')
    @mock.patch('fs_handler.check_dir_exists')
    def test_create_file_failure_file_already_exists(self, mock_check_dir_exists, mock_check_file_exists, mock_open_func):
        print('test_create_file_failure_file_already_exists')
        mock_check_dir_exists.return_value = False
        mock_check_file_exists.return_value = False
        self.assertFalse(create_file(self.directory,self.new_filename))


    @mock.patch('fs_handler.os.path.isfile')
    @mock.patch('fs_handler.os.remove')
    def test_delete_file_success(self, mock_os_remove, mock_os_is_file):
        print('test_delete_file_success')
        mock_os_is_file.return_value = True
        delete_file(self.full_path)
        mock_os_remove.assert_called_with(self.full_path)
