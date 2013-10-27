import sublime, sublime_plugin
from GoogleTranslate.google_translate_python.translate import Translator
try:
    import urllib2 as request
    from urllib import quote
except:
    from urllib import request
    from urllib.parse import quote

translator = Translator(to_lang='fr')

class TranslateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			translation = translator.translate(self.view.substr(region))
			self.view.replace(edit, region, translation)
