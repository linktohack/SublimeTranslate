## What is this?
The name should make sense :D

## How to install?
Change to your ST's local packages, it should be
`$HOME/.config/sublime-text-3/Packages/` by default and then clone the package

```bash
git clone https://github.com/linktohack/Sublime-GoogleTranslate.git GoogleTranslate
cd GoogleTranslate
git submodule init
git submodule update
```

or clone the submodule manually (if the above code do nothing)

```bash
git clone https://github.com/linktohack/Sublime-GoogleTranslate.git GoogleTranslate
cd GoogleTranslate
git submodule add https://github.com/linktohack/google-translate-python.git google_translate_python
```

## Usage
The default key binding is Ctrl+Alt+T.

Select the text you want to translate and hit the default key et.. voilà!

You can also try the `Command Palette...`, just type `Google`...
## Customize
We have two choices of configuration:

1. Default behavior via settings
Type: `Google` into the `Command Palette...` and open both Preference file.
Copy the value from the Default settings to the custom one and edit to your
like.

2. Via Key binding arguments:
Type `Google` into the `Command Palette...` and open the Default Key binding
file. Copy the value to your custom Key biding and edit to your like.

There is 3 arguments that can be edited in both ways:

* *`from_lang`*: language to be translated from
* *`to_lang`*: language to translate into
* *`extend`*: boolean: If false, the translated text will be placed right at
  the position of the old text (that should look better in most case.)
Otherwise, it will be add after the old text (if you would look carefully in
to both original and translated text.)

 vim: set spell tw=78:
