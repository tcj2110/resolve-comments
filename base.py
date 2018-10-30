# import sublime
#travis test
import sublime_plugin


class InsertPanelCommand(sublime_plugin.TextCommand):
    # Checks user input on panel
    def on_click(self, index):

            # Esc key don't do anything
            # If cancel is pressed return -1

        if index == -1:
            return -1

        self.view.run_command("insert_my_text",
                              {"args": {'text': self.data[index]}})

    def run(self, edit):
        # Populating panel with names of group members
        self.data = ["Arsalaan", "Raphael", "Kevin", "Trevor"]
        self.view.window().show_quick_panel(self.data, self.on_click, 1, 2)
        return self.data


class InsertText(sublime_plugin.TextCommand):
    def run(self, edit, args):
        self.view.insert(edit, self.view.sel()[0].begin(), args['text'])
