#!/usr/bin/env python
# coding: utf-8

# In[ ]:


passname = input('Welcome. Enter your first name please: ')
if passname.lower() == 'navarra':
    print('Hello Navarra! The password is: QA12')
else:
    print('Hello {}! See you later.'.format(passname.capitalize()))

