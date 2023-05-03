#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
import re
import os
import sys
import math
import operator
import random
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from collections import Counter
from collections import defaultdict


def get_ngrams(text, n):
    n_grams = ngrams(word_tokenize(text), n)
    return [ ' '.join(grams) for grams in n_grams]

def get_ngrams_count(text, n):
    n_grams = ngrams(word_tokenize(text), n)
    return Counter(n_grams)

def get_ngrams_prob(text, n):
    n_grams = ngrams(word_tokenize(text), n)
    n_grams_count = Counter(n_grams)
    n_grams_prob = defaultdict(float)
    for grams in n_grams_count:
        n_grams_prob[grams] = n_grams_count[grams] / len(n_grams_count)
    return n_grams_prob

def get_ngrams_prob_smoothing(text, n):
    n_grams = ngrams(word_tokenize(text), n)
    n_grams_count = Counter(n_grams)
    n_grams_prob = defaultdict(float)
    for grams in n_grams_count:
        n_grams_prob[grams] = (n_grams_count[grams] + 1) / (len(n_grams_count) + len(set(n_grams_count)))
    return n_grams_prob

def get_ngrams_prob_backoff(text, n):
    n_grams = ngrams(word_tokenize(text), n)
    n_grams_count = Counter(n_grams)
    n_grams_prob = defaultdict(float)
    for grams in n_grams_count:
        n_grams_prob[grams] = (n_grams_count[grams] + 1) / (len(n_grams_count) + len(set(n_grams_count)))
    return n_grams_prob

def get_ngrams_prob_interpolation(text, n):
    n_grams = ngrams(word_tokenize(text), n)
    n_grams_count = Counter(n_grams)
    n_grams_prob = defaultdict(float)
    for grams in n_grams_count:
        n_grams_prob[grams] = (n_grams_count[grams] + 1) / (len(n_grams_count) + len(set(n_grams_count)))
    return n_grams_prob

def get_ngrams_prob_katz(text, n):
    n_grams = ngrams(word_tokenize(text), n)
    n_grams_count = Counter(n_grams)
    n_grams_prob = defaultdict(float)
    for grams in n_grams_count:
        n_grams_prob[grams] = (n_grams_count[grams] + 1) / (len(n_grams_count) + len(set(n_grams_count)))
    return n_grams_prob

def get_ngrams_prob_kneser_ney(text, n):
    n_grams = ngrams(word_tokenize(text), n)
    n_grams_count = Counter(n_grams)
    n_grams_prob = defaultdict(float)
    for grams in n_grams_count:
        n_grams_prob[grams] = (n_grams_count[grams] + 1) / (len(n_grams_count) + len(set(n_grams_count)))
    return n_grams_prob

def get_ngrams_prob_witten_bell(text, n):
    n_grams = ngrams(word_tokenize(text), n)
    n_grams_count = Counter(n_grams)
    n_grams_prob = defaultdict(float)
    for grams in n_grams_count:
        n_grams_prob[grams] = (n_grams_count[grams] + 1) / (len(n_grams_count) + len(set(n_grams_count)))
    return n_grams_prob

def get_ngrams_prob_absolute_discounting(text, n):
    n_grams = ngrams(word_tokenize(text), n)
    n_grams_count = Counter(n_grams)
    n_grams_prob = defaultdict(float)
    for grams in n_grams_count:
        n_grams_prob[grams] = (n_grams_count[grams] + 1) / (len(n_grams_count) + len(set(n_grams_count)))
    return n_grams_prob

def get_ngrams_prob_good_turing(text, n):
    n_grams = ngrams(word_tokenize(text), n)
    n_grams_count = Counter(n_grams)
    n_grams_prob = defaultdict(float)
    for grams in n_grams_count:
        n_grams_prob[grams] = (n_grams_count[grams] + 1) / (len(n_grams_count) + len(set(n_grams_count)))
    return n_grams_prob

def get_ngrams_prob_kneser_ney_smoothing(text, n):
    n_grams = ngrams(word_tokenize(text), n)
    n_grams_count = Counter(n_grams)
    n_grams_prob = defaultdict(float)
    for grams in n_grams_count:
        n_grams_prob[grams] = (n_grams_count[grams] + 1) / (len(n_grams_count) + len(set(n_grams_count)))
    return n_grams_prob

def get_ngrams_prob_kneser_ney_discounting(text, n):
    n_grams = ngrams(word_tokenize(text), n)
    n_grams_count = Counter(n_grams)
    n_grams_prob = defaultdict(float)
    for grams in n_grams_count:
        n_grams_prob[grams] = (n_grams_count[grams] + 1) / (len(n_grams_count) + len(set(n_grams_count)))
    return n_grams_prob

def get_ngrams_prob_kneser_ney_smoothing_discounting(text, n):
    n_grams = ngrams(word_tokenize(text), n)
    n_grams_count = Counter(n_grams)
    n_grams_prob = defaultdict(float)
    for grams in n_grams_count:
        n_grams_prob[grams] = (n_grams_count[grams] + 1) / (len(n_gram)