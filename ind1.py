#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

if __name__ == '__main__':
    file = 'Text.txt'
    with open('Text.txt', 'r', encoding='utf-8-sig') as f:
        sentences = f.read().split('. ')

    print(min(sentences, key=lambda x: re.subn(r'[,.;@#?!&$]+', '', x)[1]))
