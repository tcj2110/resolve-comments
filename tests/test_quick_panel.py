import sublime
import sys
from unittest import TestCase

version = sublime.version()


class TestQuickPanel(TestCase):

    def setUp(self):
        self.view = sublime.active_window().new_file()
        s = sublime.load_settings("Preferences.sublime-settings")
        s.set("close_windows_when_empty", False)

    def tearDown(self):
        if self.view:
            self.view.set_scratch(True)
            self.view.window().focus_view(self.view)
            self.view.window().run_command("close_file")

    # Tests Quick Panel visibility in Sublime Plugin User Interface

    def test_quick_panel_st3(self):
        self.view.run_command("insert_panel")
        self.assertEqual(self.view.window().panels(),
                         ['console',
                          'find',
                          'find_in_files',
                          'output.find_results',
                          'replace'])


testpanel = sys.modules["git_comments.base"]

# Tests whether populated panel data is accurate


class TestPanelData(TestCase):
    def mock_panel_list(self):
        mock_panel_list = [
            ['Set up db schema and created models', ''],
            ['Setup database', '']]
        return mock_panel_list

    def test_panel_data_st3(self):
        panel_data = testpanel.load_quick_panel_data(
            'Nanosoft1*', 'raphaeljunior')
        self.assertListEqual(panel_data, self.mock_panel_list())
