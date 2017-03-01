import sublime
import sublime_plugin


class UppercaseCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                st = self.view.substr(region)
                st = st.upper()
                self.view.replace(edit, region, st)
