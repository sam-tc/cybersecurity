# Task 1 - Cryptography

## Challenge

The given challenge text was:

QkFJTntiQTczX1E4Ul9BcmhIQ19YNHlHY0R9

The expected flag format was:

BYTE{...}

## Step 1 - Base64 Decoding

The challenge text appeared to be Base64 encoded.

I decoded it and obtained:

BAIN{bA73_Q8R_ArhHC_X4yGcD}

Since this did not match the expected BYTE{...} format, I concluded that another cipher was involved.

## Step 2 - Cipher Analysis

I tested ROT13, but the result did not match the expected flag format.

I then investigated a Vigenere cipher.

Since the expected prefix was:

BYTE

and the encrypted prefix was:

BAIN

I compared the plaintext and ciphertext prefixes.

Ciphertext: B A I N  
Plaintext:  B Y T E  
Key:        A C P J

This gave the repeating Vigenere key:

ACPJ

The key was therefore derived using the known flag prefix rather than guessed.

## Step 3 - Decryption

I wrote a Python script to automate both the Base64 decoding and Vigenere decryption.

The resulting flag was:

BYTE{bY73_B8I_ApsYC_V4jXcB}

## Tools Used

- macOS Terminal
- Python 3
- Base64
- Vigenere cipher

## What I Learned

This challenge taught me the difference between encoding and encryption.

I learned how to recognize and decode Base64, test and reject an incorrect cipher such as ROT13, understand how a Vigenere cipher works, derive a key using known plaintext, and automate the process using Python.
