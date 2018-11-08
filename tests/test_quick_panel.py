import sublime
import sys
from unittest import TestCase

version = sublime.version()


# for testing sublime command
class TestQuickPanel(TestCase):

    def setUp(self):
        self.view = sublime.active_window().new_file()
        # make sure we have a window to work with
        s = sublime.load_settings("Preferences.sublime-settings")
        s.set("close_windows_when_empty", False)

    def tearDown(self):
        if self.view:
            self.view.set_scratch(True)
            self.view.window().focus_view(self.view)
            self.view.window().run_command("close_file")

    # since ST3 uses python 2 and python 2 doesn't support @unittest.skip,
    # we have to do primitive skipping

    def test_quick_panel_st3(self):
        self.view.run_command("insert_panel")
        self.assertEqual(self.view.window().panels(),
                         ['console',
                          'find',
                          'find_in_files',
                          'output.find_results',
                          'replace'])


testpanel = sys.modules["git_comments.main"]
