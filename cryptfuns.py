#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 06:56:26 2020

Dont't roll your own.

functions for cryptopals set1
 
@author: adam
"""

import codecs
import base64
from math import ceil

# change this to return just the base64 object
# use decode and replace in main to test and print.
def hex_to_base64(x):
    """ convert hex to base64 encoding
    for set1:challenge1
    """
    return codecs.encode(codecs.decode(str.encode(x),"hex"),"base64")


def fixed_xor(a,b):
    """ XOR two equal length hexadecimal inputs
    set1: challenge 2
    """
    # get bytes from each hex input.
    tmp = "".join([bytes([x[0]^x[1]]).decode() for x in zip(bytes.fromhex(a),bytes.fromhex(b))])
    return str.encode(tmp).hex()



with open("/home/adam/scripts/cryptopals/english_monograms.txt","r") as f:
    english_character_counts = f.readlines()
    
english_letters = {}
counts = [int(x.split(" ")[1]) for x in english_character_counts]
for x in english_character_counts:
    letter = x.split(" ")[0].lower()
    count = int(x.split(" ")[1].replace("\n",""))
    english_letters[letter] = count/sum(counts)
    
def is_it_english(x):
    tmp = {}
    x = x.replace(" ","")
    for l in x.lower():
        if l in tmp.keys():
            tmp[l] += 1
        else:
            tmp[l] = 1
    if tmp == {}:
        return (2**2)*len(x)
    tmp = {k: v/len(x) for k,v in tmp.items()}
    abs_errs = []
    for k,v in tmp.items():
        if k in english_letters.keys():
            abs_errs.append((english_letters[k] - v)**2)
        else:
            abs_errs.append((2)**2) # penalty term
            
    return sum(abs_errs) / len(x)


def break_single_xor(ciphertext):
    cipherbytes = [x for x in bytes.fromhex(ciphertext)]
    poss_ciphers = {}
    for x in range(128):
        #hexkey = bytes([x]).hex()
        #test_otp = "".join(int(len(ciphertext)/2)*[hexkey])
        #fixed_xor(ciphertext,test_otp)
        plaintext = "".join([bytes([x^y]).decode("utf-8",errors="ignore") for y in cipherbytes])
        poss_ciphers[x] = is_it_english(plaintext)
        #print(x,":",plaintext)
        
    k = sorted(poss_ciphers.items(), key= lambda k: k[1])[0][0]
    return "".join([bytes([k^y]).decode("utf-8",errors="ignore") for y in cipherbytes])

def fixed_xor(a,b):
    """ XOR two equal length hexadecimal inputs
    """
    # get bytes from each hex input.
    tmp = "".join([bytes([x[0]^x[1]]).decode() for x in zip(bytes.fromhex(a),bytes.fromhex(b))])
    return str.encode(tmp).hex()

def enc_repeating_xor(pt,key):
    lkey = "".join([key] * ceil(len(pt) / len(key)))
    lkey = lkey[0:len(pt)]
    # convert both to hex
    pt = codecs.encode(pt.encode(),"hex").decode()
    lkey = codecs.encode(lkey.encode(),"hex").decode()
    # call xor
    ct = fixed_xor(pt,lkey)
    return ct