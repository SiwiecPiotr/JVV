#!/usr/bin/env python
import os, re, openpyxl, io
# import streamlit as st
menu = True

#regex = re.compile(r'([€]\s*)(\d+,\d+)')
regex = re.compile(r'([€]?\s*)(\d+[,.]\d+)')
letters ={
    "A":1,
    "B":2,
    "C":3,
    "D":4,
    "E":5,
    "F":6,
    "G":7,
    "H":8,
    "I":9,
    "J":10,
    "K":11,
    "L":12,
    "M":13,
    "N":14,
    "O":15,
    "P":16
}
def a_to_1(letter):
    return letters[letter]
def switcheroo(word1, word2, sheet):
    for i in range(1, sheet.max_column+1):
        for j in range(1, sheet.max_row+1):
            if sheet.cell(row=j, column=i).value == word1:
                sheet.cell(row=j, column=i).value = word2

def snipsnip(word):
    while True:
        if word[0] == "€" or word[0] ==" ":
            word = word[1:]
        else:
            break
    return word

def findncalc(column_nr, percentage:float, sheet):
    tp = percentage*0.01+1
    for i in range(1, sheet.max_row+1):
        slice = str(sheet.cell(row = i, column = column_nr).value)
        found_match = regex.finditer(slice)
        for match in found_match:
            temp = float(snipsnip(match.group()).replace(",","."))
            temp = round(temp*tp, 2)
            slice = slice.replace(match.group(), "€"+str(temp))
            sheet.cell(row = i, column = column_nr).value = slice


def dummy():
    pass