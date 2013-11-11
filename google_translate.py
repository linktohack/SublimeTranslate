import sublime, sublime_plugin
from GoogleTranslate.google_translate_python.translate import Translator


class TranslateCommand(sublime_plugin.TextCommand):
    def run(self, edit, extend=False, from_lang='', to_lang=''):
        settings = sublime.load_settings('GoogleTranslate.sublime-settings')
        if not extend:
            extend = settings.get('extend', False)
        if from_lang == '':
            from_lang = settings.get('from_lang', '')
        if to_lang == '':
            to_lang = settings.get('to_lang', 'en')

        translator = Translator(from_lang=from_lang, to_lang=to_lang)

        for region in self.view.sel():
            translation = translator.translate(self.view.substr(region))
            if extend:
                self.view.insert(edit, region.end(), '\n' + translation + '\n\n')
            else:
                self.view.replace(edit, region, translation)

# vim:set ts=4 sw=4:
