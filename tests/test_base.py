import unittest
from base import ExampleCommand
import sublime_plugin

class TestBase(unittest.TestCase):
    def test_example_command(self):
        example = ExampleCommand(sublime_plugin.Text)
        example.run("edit")