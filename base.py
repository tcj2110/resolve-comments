# import sublime
# travis test
import sublime_plugin


class InsertPanelCommand(sublime_plugin.TextCommand):
    # Checks user input on panel

    # Panel Row clicked generates HTML popup on screen
    def gen_comment(self, text):
        title_str = text
        point = self.view.text_point(30, 5)
        html_str = '<b>' + title_str + \
            '</b><br><a href="test">Click Me</a> <style>color=red</style>'
        self.view.show_popup(html_str, on_navigate=print, location=point)

    # Handles panel click logic
    def on_click(self, index):

            # Esc key don't do anything
            # If cancel is pressed return -1

        if index == -1:
            return -1

        self.view.run_command("insert_my_text",
                              {"args": {'text': self.data[index]}})
        self.gen_comment(self.data[index])

    # Entrypoint

    def run(self, edit):
        # Populating panel with names of group members
        self.data = ["Arsalaan", "Raphael", "Kevin", "Trevor"]
        self.view.window().show_quick_panel(self.data, self.on_click, 1, 2)
        return self.data
