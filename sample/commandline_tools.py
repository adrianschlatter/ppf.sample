# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 12:42:16 2017

@author: adrian
"""

from argparse import ArgumentParser


def echo():
    parser = ArgumentParser()
    parser.add_argument("word", help="word to be echoed")
    args = parser.parse_args()

    print(args.word)
