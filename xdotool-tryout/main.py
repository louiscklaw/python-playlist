#!/usr/bin/env python3

import os,sys
from pprint import pprint

from xdo import Xdo

xdo = Xdo()

# win_id = xdo.select_window_with_click()
# print(win_id)
print(xdo.search_windows(winclass='Chrome'.encode(), only_visible=True))

# xdo.enter_text_window(win_id, 'Python rocks!')
