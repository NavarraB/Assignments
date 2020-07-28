#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('hello ubuntu')


# In[28]:


def front_back(word):
    b = word[-1]
    if len(word) < 2:
        return word
    else:
        return word.replace(word[-1], word[0], 1).replace(word[0], b, 1)
front_back('clarusway')


# In[24]:


a = 'aaazzz'
print(a.replace(a[0], 'b', 1).replace(a[-1], 'c', 1))


# In[33]:


sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]


# In[43]:


for ii in range(9):
    if ii in (0, 3, 6):
        print(15 * '- ')
    for i in range(9):
        if i in(2, 5, 8):
            print(sudoku[ii][i], '| ', end = '')
        else:
            print(sudoku[ii][i], ' ', end = '')
    print()
print(15 * '- ')


# In[6]:


print(15 * '- ')
for i in range(9):
    if i in(2, 5, 8):
        print(sudoku[0][i], '| ', end = '')
    else:
        print(sudoku[0][i], ' ', end = '')
print()
for i in range(9):
    if i in(2, 5, 8):
        print(sudoku[1][i], '| ', end = '')
    else:
        print(sudoku[1][i], ' ', end = '')
print()
for i in range(9):
    if i in(2, 5, 8):
        print(sudoku[2][i], '| ', end = '')
    else:
        print(sudoku[2][i], ' ', end = '')
print()
print(15 * '- ')
for i in range(9):
    if i in(2, 5, 8):
        print(sudoku[3][i], '| ', end = '')
    else:
        print(sudoku[3][i], ' ', end = '')
print()
for i in range(9):
    if i in(2, 5, 8):
        print(sudoku[4][i], '| ', end = '')
    else:
        print(sudoku[4][i], ' ', end = '')
print()
for i in range(9):
    if i in(2, 5, 8):
        print(sudoku[5][i], '| ', end = '')
    else:
        print(sudoku[5][i], ' ', end = '')
print()
print(15 * '- ')


# In[3]:


for i in range(1,5):
    print(i, end = '')
    for ii in range(6,10):
        print(ii, end = '')

