from diskspace import bytes_to_readable, subprocess_check_output, 
from diskspace import print_tree, calculate_percentage, du_command, percentage_args

import unittest
import os
import StringIO
import subprocess
import mock
import io
import sys


class DiskspaceTest(unittest.TestCase):

    def setUp(self):
        self.file_tree = {'/home/teste': {'print_size': '2.00Kb',
                                          'children': [], 'size': 4}}
        self.file_tree_node = {'print_size': '2.00Kb',
                               'children': [], 'size': 4}
        self.path = '/home/teste'
        self.largest_size = 6
        self.total_size = 4

    def bytes_to_readable_test(self):
        blocks = 224
        result = "112.00Kb"
        self.assertEqual(bytes_to_readable(blocks), result)

    def subprocess_check_output_test(self):
        command = 'du'
        du_result = subprocess.check_output(command)
        result = subprocess_check_output(command)
        self.assertEqual(du_result, result)

    def calculate_percentage_test(self):
        percentage = calculate_percentage(self.file_tree_node, self.total_size)
        self.assertTrue(percentage == 100)

    def print_tree_test(self):
        cap = StringIO.StringIO()
        sys.stdout = cap

        print_tree(self.file_tree, self.file_tree_node, self.path,
                   self.largest_size, self.total_size)
        result = "2.00Kb  100%  /home/teste\n"
        sys.stdout = sys.__stdout__
        self.assertEqual(result, cap.getvalue())

if __name__ == '__main__':
    unittest.main()
  