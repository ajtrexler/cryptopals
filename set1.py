#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 17:18:35 2020
set 1, challenge 1. 
fun with encoding.

@author: adam
"""
import cryptfuns as cf
import unittest

class testSet1(unittest.TestCase):
    
    def test_challenge1(self):
        input_hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        answer = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        self.assertEqual(cf.hex_to_base64(input_hex).decode().replace("\n",""), answer)    

    def test_challenge2(self):
        plaintext = "1c0111001f010100061a024b53535009181c"
        otp = "686974207468652062756c6c277320657965"

        ciphertext = "746865206b696420646f6e277420706c6179"
        self.assertEqual(cf.fixed_xor(plaintext,otp), ciphertext) # booyah
        
    def test_challenge3(self):
        ciphertext  = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
        self.assertEqual(cf.break_single_xor(ciphertext),"Cooking MC's like a pound of bacon")
    
    def test_challenge4(self):
        with open("/home/adam/scripts/cryptopals/set4.txt","r") as f:
            data = f.readlines()

        outputs = []    
        for ciphertext in data:
            ciphertext = ciphertext.replace("\n","")
            outputs.append(cf.break_single_xor(ciphertext))
        self.assertEqual(sorted([(cf.is_it_english(o),o) for o in outputs])[0][1],"Now that the party is jumping\n")
        
    def test_challenge5(self):
        
        pt = """Burning 'em, if you ain't quick and nimble
        I go crazy when I hear a cymbal"""

        key = "ICE"

        answer = """0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"""
        self.assertEqual(cf.enc_repeating_xor(pt,key) ==  answer)

if __name__ == "__main__":
    unittest.main()
