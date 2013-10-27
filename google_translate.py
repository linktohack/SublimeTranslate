import sublime, sublime_plugin
from GoogleTranslate.google_translate_python.translate import Translator


class TranslateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			translation = translator.translate(self.view.substr(region))
			self.view.replace(edit, region, translation)
