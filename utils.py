# -*- coding: utf-8 -*- 
import web
import string
import os.path

cyrillic_letters = "абвгдежзийклмнопртуфхцшщъьюя"

def url(*args):
    """Returns the an URL made from the home with all parts in *args added as path components"""
    home = web.ctx.home.replace('/code.cgi', '')
    return os.path.join(*([home] + list(args)))
    
def option(label, value=None, selected=None):
    """Returns HTML code for an option tag"""
    if value is None: value = label
    if value == selected:
        selected = 'selected="selected"'
    else:
        selected = ''
    if value:
        value = "value='%s'" % value
    else:
        value = ''
    return '<option %(selected)s %(value)s>%(label)s</option>\n' % locals()

def cyr_from_lat_all(word):
    """Returns a list of all possible transliterations of a word"""
    word = word.lower()
    map = (
    ('sht', u'щ'),
    ('ia', u'иа', u'ия'),
    ('ya', u'я'),
    ('yu', u'ю'),
    ('zh', u'ж', u'зх'),
    ('ts', u'ц', u'тс'),
    ('sh', u'ш', u'сх'),
    ('ch', u'ч'),
    #
    ('a', u'а', u'ъ'),
    ('b', u'б'),
    ('c', u'ц'),
    ('d', u'д'),
    ('e', u'е'),
    ('f', u'ф'),
    ('g', u'г'),
    ('h', u'х'),
    ('i', u'и'),
    ('j', u'ж', u'й'),
    ('k', u'к'),
    ('l', u'л'),
    ('m', u'м'),
    ('n', u'н'),
    ('o', u'о'),
    ('p', u'п'),
    ('q', u'я'),
    ('r', u'р'),
    ('s', u'с'),
    ('t', u'т'),
    ('u', u'у'),
    ('v', u'в'),
    ('w', u'в'),
    ('x', u'кс'),
    ('y', u'ъ', u'й'),
    ('z', u'з'),
    )
    transliterations = []
    def rec(word, transliteration):
        if word == '':
            transliterations.append(transliteration)
            return
        if word[0] in string.whitespace:
            rec(word[1:], transliteration + word[0])
            return
        for entry in map:
            if word.startswith(entry[0]):
                for cyr in entry[1:]:
                    rec(word[len(entry[0]):], transliteration + cyr)
    rec(word, u'')
    return transliterations
    
def intersection_by_key(s1, s2, key):
    """Returns the intersection of two sets, but the comparison is done by the function key applied to each element"""
    dicts = [dict([(key(elem), elem) for elem in s]) for s in (s1, s2)]
    dicts_key_sets = [set(d.keys()) for d in dicts]
    return set([dicts[0][k] for k in dicts_key_sets[0] & dicts_key_sets[1]])
    
def has_cyrillic_letters(s):
    return bool(set(s) & set(cyrillic_letters))