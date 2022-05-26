# lang_translator.py
# Program Description: Automatically translates text from one lanuage into another. This is similar to Google Translate, but does not use a neural network to translate the text. Instead, this program uses the Google Translate
    # Ajax API 'googletrans' to make calls to the methods such as detect and translate the text.
    
# Import the 'googletrans' library.
import googletrans
# Import the 'Translator' module from 'googletrans' library.    
from googletrans import Translator
# Ask the user whether they would like to see the list of available languages for translation before the translation process. 
avail_langs = input('Before translating text, would you like to see a list of available languages (y/n)? ')
# Use an 'if' statement to determine whether the program should print the list of available languages. 
if avail_langs == 'y':
    print(googletrans.LANGUAGES)
# Create an instance of print.
print()
# Enter the text you want to be translated into the variable 'text' below. Make sure that there are three apostrophes (') before and after the text you would like translated. 
source_text = '''xxxxxxxx'''
# Create an instance of the Google Translate API.
translator = Translator()
# Automatically detect the source language of the text.
detect_language = translator.detect(source_text)
print(detect_language)
# Create an instance of print.
print()
# Translate the source language to the destination language. If destination language is NOT specified -- dest(destination language) -- program will automatically translate source text to English.
# NOTE: translate(self, text, dest='en', src='auto', **kwargs)
translated = translator.translate(source_text)
# Display the translated text. 
print(translated.text)
