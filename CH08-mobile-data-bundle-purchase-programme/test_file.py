# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:53:43 2018

@author: Gebruiker
"""

from simple_bundle_purchase1 import dataBundlePurchase


# Test call to programme:
print ('TEST EXAMPLE 1')
# database input, you will still need to check user pin
result = dataBundlePurchase('1234', 34.55)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')

print ('TEST EXAMPLE 2')
result = dataBundlePurchase('2345', -22.00)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')

print ('TEST EXAMPLE 3')
result = dataBundlePurchase('3456', 17.55)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')

