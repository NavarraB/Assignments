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


# In[ ]:


# Assignment - 4 (Is it a Prime Number?)
pnumber = input('Give me a number: ')
while pnumber.isdecimal() != True:
    print('Positive integer number please')
    pnumber = input('Give me a number: ')
pnumber = int(pnumber)
a = 0
for i in range(1,(pnumber+1)):
    if pnumber % i == 0:
        a += 1
if pnumber in (0, 1):
    print(pnumber, 'is not a prime number')
else:
    if a > 2:
        print(pnumber, 'is not a prime number')
    else:
        print(pnumber, 'is a prime number')


# In[ ]:


# Assignment - 5 (Fibonacci Numbers)
fibonacci = []
x = 1
y = 0
while x < 56:
    if len(fibonacci) < 1:
        fibonacci.append(x)
    fibonacci.append(x)
    x += fibonacci[y]
    y += 1
print(fibonacci)


# In[ ]:


# Assignment - 6 (Prime Numbers)
n = input('Enter a limit number: ')
while n.isdecimal() != True:
    print('Give me a integer number')
    n = input('Enter a limit number: ')
n = int(n)
nlist = []
for i in range (2, n+1):
    a = 0
    for x in range (1, i+1):
        if i % x == 0:
            a += 1
    if a == 2:
        nlist.append(i)
print(nlist)

