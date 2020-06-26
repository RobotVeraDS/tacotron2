""" from https://github.com/keithito/tacotron """
import re
from text import cleaners
from text.symbols import english_symbols, russian_symbols, spanish_symbols


# Mappings from symbol to numeric ID and vice versa:
_english_symbol_to_id = {s: i for i, s in enumerate(english_symbols)}
_english_id_to_symbol = {i: s for i, s in enumerate(english_symbols)}

# Mappings from symbol to numeric ID and vice versa:
_russian_symbol_to_id = {s: i for i, s in enumerate(russian_symbols)}
_russian_id_to_symbol = {i: s for i, s in enumerate(russian_symbols)}

_spanish_symbol_to_id = {s: i for i, s in enumerate(spanish_symbols)}
_spanish_id_to_symbol = {i: s for i, s in enumerate(spanish_symbols)}

# Regular expression matching text enclosed in curly braces:
_curly_re = re.compile(r'(.*?)\{(.+?)\}(.*)')


def text_to_sequence(text, cleaner_names, lang="en"):
  '''Converts a string of text to a sequence of IDs corresponding to the symbols in the text.

    The text can optionally have ARPAbet sequences enclosed in curly braces embedded
    in it. For example, "Turn left on {HH AW1 S S T AH0 N} Street."

    Args:
      text: string to convert to a sequence
      cleaner_names: names of the cleaner functions to run the text through

    Returns:
      List of integers corresponding to the symbols in the text
  '''
  sequence = []

  # Check for curly braces and treat their contents as ARPAbet:
  while len(text):
    m = _curly_re.match(text)
    if not m:
      sequence += _symbols_to_sequence(_clean_text(text, cleaner_names), lang)
      break
    sequence += _symbols_to_sequence(_clean_text(m.group(1), cleaner_names), lang)
    sequence += _arpabet_to_sequence(m.group(2))
    text = m.group(3)

  return sequence


def sequence_to_text(sequence, lang="en"):
  '''Converts a sequence of IDs back to a string'''

  __id_to_symbol = None
  if lang == "en":
    __id_to_symbol = _english_id_to_symbol
  elif lang == "es":
    __id_to_symbol = _spanish_id_to_symbol
  else:
    __id_to_symbol = _russian_id_to_symbol


  result = ''
  for symbol_id in sequence:
    if symbol_id in __id_to_symbol:
      s = __id_to_symbol[symbol_id]
      # Enclose ARPAbet back in curly braces:
      if len(s) > 1 and s[0] == '@':
        s = '{%s}' % s[1:]
      result += s
  return result.replace('}{', ' ')


def _clean_text(text, cleaner_names):
  for name in cleaner_names:
    cleaner = getattr(cleaners, name)
    if not cleaner:
      raise Exception('Unknown cleaner: %s' % name)
    text = cleaner(text)
  return text


def _symbols_to_sequence(symbols, lang="en"):
  __symbol_to_id = None
  if lang == "en":
    __symbol_to_id = _english_symbol_to_id
  elif lang == "es":
    __symbol_to_id = _spanish_symbol_to_id
  else:
    __symbol_to_id = _russian_symbol_to_id

  return [__symbol_to_id[s] for s in symbols if _should_keep_symbol(s, lang)]


def _arpabet_to_sequence(text):
  return _symbols_to_sequence(['@' + s for s in text.split()])


def _should_keep_symbol(s, lang="en"):
  __symbol_to_id = None
  if lang == "en":
    __symbol_to_id = _english_symbol_to_id
  elif lang == "es":
    __symbol_to_id = _spanish_symbol_to_id
  else:
    __symbol_to_id = _russian_symbol_to_id

  return s in __symbol_to_id and s is not '_' and s is not '~'
