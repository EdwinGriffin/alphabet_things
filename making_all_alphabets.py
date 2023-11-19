import csv
import random

alpha = 'abcdefghijklmnopqrstuvwxyz'

f = open('all_alphabets.csv', 'w', newline='')

def make_an_alphabet(output=''):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    other_alpha = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for i in range(26):
