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


# In[ ]:


# Assignment - 3 (Is it Armstrong Number?)
given_num = input('Please enter a number: ')
given_numset = set(given_num)
forbid_set1 = set('-')
forbid_set2 = set(',.')
while bool(given_numset & forbid_set1) or bool(given_numset & forbid_set2) or given_num.isnumeric() != True: 
    if bool(given_numset & forbid_set1):
        given_num = input('Please enter a positive number: ')
        given_numset = set(given_num)
    elif bool(given_numset & forbid_set2):
        given_num = input('Please enter a integer number: ')
        given_numset = set(given_num)
    elif given_num.isnumeric() != True:
        given_num = input('Do not use any entries other than numeric values. Please enter a number: ')
        given_numset = set(given_num)
given_arm_num1 = int(given_num)
given_arm_num2 = 0
for x in given_num:
    int(x) ** len(given_num)
    given_arm_num2 += (int(x) ** len(given_num))
if given_arm_num1 == given_arm_num2:
    print('{} is an Armstrong number'.format(given_arm_num1))
else:
    print('{} is not an Armstrong number'.format(given_arm_num1))

