import sublime, sublime_plugin
from GoogleTranslate.google_translate_python.translate import Translator


class TranslateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        settings = sublime.load_settings('GoogleTranslate.sublime-settings')
        from_lang =  settings.get('from_lang', '')
        to_lang =  settings.get('to_lang', '')
        translator = Translator(from_lang=from_lang, to_lang=to_lang)
        
        for region in self.view.sel():
            translation = translator.translate(self.view.substr(region))
            self.view.replace(edit, region, translation)
