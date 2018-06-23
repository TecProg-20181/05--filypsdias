from diskspace import *
from diskspace import print_tree, calculate_percentage, duCommand, percentage_args

import unittest
import os
import StringIO
import subprocess
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

    def test_test_bytes_to_readable(self):
        fullblocks = 224
        result = "112.00Kb"
        self.assertEqual(bytes_to_readable(fullblocks), result)

    def test_subprocess_check_output(self):
        command = 'du'
        du_result = subprocess.check_output(command)
        result = subprocess_check_output(command)
        self.assertEqual(du_result, result)

    def test_print_tree(self):
        caps = StringIO.StringIO()
        sys.stdout = caps

        print_tree(self.file_tree, self.file_tree_node, self.path,
                   self.largest_size, self.total_size)
        result = "2.00Kb  100%  /home/teste\n"
        sys.stdout = sys.__stdout__
        self.assertEqual(result, caps.getvalue())

    def test_args_tree_view(self):
        fulldepth = 0
        path = self.path.split("/")[-1]
        result = '{}{}'.format('   '*fulldepth, os.path.basename(self.path))
        self.assertEqual(result, path)

    def test_calculate_percentage(self):
        percentage = calculate_percentage(self.file_tree_node, self.total_size)
        self.assertTrue(percentage == 100)

    def test_duCommand_default(self):
        abs_directory = self.path
        cmd = duCommand(-1, abs_directory)
        result = "du  " + self.path
        self.assertEqual(result, cmd)

    def test_duCommand(self):
        abs_directory = self.path
        fulldepth = 1
        cmd = duCommand(fulldepth, abs_directory)
        result = "du -d {} {}".format(fulldepth, self.path)
        self.assertEqual(result, cmd)
    
    def test_show_space_list(self):
        caps = StringIO.StringIO()
        sys.stdout = caps
        print_space_list(self.largest_size, self.file_tree,
                         self.path, self.total_size)
        result = "  Size   (%)  File\n2.00Kb  100%  {}\n".format(self.path)
        sys.stdout = sys.__stdout__
        self.assertEqual(result, caps.getvalue())


if __name__ == '__main__':
    unittest.main()
  