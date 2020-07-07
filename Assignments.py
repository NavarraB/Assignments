#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Assignment - 1 (if-statements)
passname = input('Welcome. Enter your first name please: ')
if passname.lower() == 'navarra':
    print('Hello Navarra! The password is: QA12')
else:
    print('Hello {}! See you later.'.format(passname.capitalize()))


# In[ ]:


# Assignment - 2 (if-statements)
cigar = input('Are you a cigarette addict older than 75 years old? ')
disease = input('Do you have a severe chronic disease? ')
immune = input('Is your immune system too weak? ')
if cigar.lower() in ('yes', 'yep', 'right', 'yea', 'yeap', 'unfortunately'):
    cigar = True
else:
    cigar = False
if disease.lower() in ('yes', 'yep', 'right', 'yea', 'yeap', 'unfortunately'):
    disease = True
else:
    disease = False
if immune.lower() in ('yes', 'yep', 'right', 'yea', 'yeap', 'unfortunately'):
    immune = True
else:
    immune = False
if cigar or disease or immune:
    print('You are in risky group')
else:
    print('You are not in risky group')

