# lang_translator.py
# Program Description: Automatically translates text from one lanuage into another. This is similar to Google Translate, but does not use a neural network to translate the text. Instead, this program uses the Google Translate
    # Ajax API 'googletrans' to make calls to the methods such as detect and translate the text.
    
# Also Nicole, since I'm sending you the actual code, I figured I might as well explain the red text. So, the '#' followed by red texts are called 'comments.'
    # Basically, they tell the person reading the code what the code does and anything that might need attention. This is a short little program,
    # so there isn't a lot of code or comments.
    
# Import the 'googletrans' library.
import googletrans
# Import the 'Translator' module from 'googletrans' library.    
from googletrans import Translator
# Ask the user whether they would like to see the list of available languages for translation before the translation process. 
avail_langs = input('Before translating text, would you like to see a list of available languages (y/n)? ')
# Use an 'if' statement to determine whether the program should print the list of available languages. 
if avail_langs == 'y':
    print(googletrans.LANGUAGES)
# Print a groovy little space cause why not lmao.
print()
# Enter the text you want to be translated into the variable 'text' below. Make sure that there are three apostrophes (') before and after the text you would like translated. 
source_text = '''Salut Nicole! Alors ... J'ai codé ce traducteur de langage en Python plus tôt dans la journée pour m'amuser parce que pourquoi pas, non?
Je l'aime jusqu'à présent, même si ce n'est pas aussi pratique que Google Translate (principalement parce que je dois exécuter le code dans l'environnement de codage, pas sur Internet).
Regardez ci-dessus, ce programme évalue également la confiance dans la détection et la traduction de la langue (en gros, à quel point il est sûr d'avoir fait la bonne chose)!
C'est sur une échelle de 0 à 1, 1,0 étant une confiance extrême et absolue. Quoi qu'il en soit, je pensais que c'était une bonne chose que j'ai faite et je voulais juste vous montrer.
Je t'aime tellement.
(au fait, la traduction peut être légèrement décalée, donc si quelque chose ne va pas, ignorez-le hahaha. Je fait encore entraîner le programme)'''
# Create an instance of the Google Translate API.
translator = Translator()
# Automatically detect the source language of the text.
detect_language = translator.detect(source_text)
print(detect_language)
# Print another groovy little space cause why not lmao.
print()
# Translate the source language to the destination language. If destination language is NOT specified -- dest(destination language) -- program will automatically translate source text to English.
# NOTE: translate(self, text, dest='en', src='auto', **kwargs)
translated = translator.translate(source_text)
# Display the translated text. 
print(translated.text)
