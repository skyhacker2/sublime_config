import sublime, sublime_plugin

class TerminalCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.window.run_command("show_panel", {"panel":"input"})