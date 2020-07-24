#!/usr/bin/env python3

import os,sys
from pprint import pprint

from googletrans import Translator

translator = Translator()
pprint(translator.translate('안녕하세요.').text)

pprint(translator.translate('안녕하세요.', dest='zh-TW').text)

pprint(translator.translate('veritas lux mea', src='la'))
