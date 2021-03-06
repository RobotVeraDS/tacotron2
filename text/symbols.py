""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details. '''
from text import cmudict

_pad        = '_'
_punctuation = '!\'(),.:;? '
_special = '-'
_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
_arpabet = ['@' + s for s in cmudict.valid_symbols]

# Export all symbols:
english_symbols = [_pad] + list(_special) + list(_punctuation) + list(_letters) + _arpabet


# russian

_pad        = '_'
_punctuation = ',.!?- '
#_letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

_commands = '+#$%^&*'

russian_symbols = [_pad] + list(_punctuation) + list(_letters) + list(_commands)

# spanish
_pad        = '_'
_punctuation = '!\'(),.:;?- '
_letters = 'abcdefghijklmnopqrstuvwxyz¡¿áåæèéëíîñóöúü'

_commands = '+#$%^&*'

spanish_symbols = [_pad] + list(_punctuation) + list(_letters) + list(_commands)


# french

_pad        = '_'
_punctuation = '!\'(),.:;?- '
_letters = 'abcdefghijklmnopqrstuvwxyzàâæçèéêëîïôùûœ'
_commands = '+#$%^&*'

french_symbols = [_pad] + list(_punctuation) + list(_letters) + list(_commands)
