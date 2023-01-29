#!/usr/bin/env python
# coding: utf-8

# In[1]:


list = [1,2,3,4,5]
list.append(6)
list
list.count(2)
help(list.reverse())
help(list.pop())


# In[2]:


def say_hello():
    print('hello')
say_hello()
def greeting(name):
    print(f'Hello {name}')
greeting('John')
def add_num(num1,num2):
    return num1+num2
add_num(4,5)
result = add_num(4,5)
print(result)


# In[1]:


def print_result(a,b):
    print(a+b)
def return_result(a,b):
    return a+b
print_result(10,5)
def even_check(number):
    return number % 2 == 0
even_check(20)


# In[4]:


def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass  
    return False
check_even_list([1,2,3])
check_even_list([1,3,5])


# In[2]:


def check_even_list(num_list):    
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass 
    return even_numbers
check_even_list([1,2,3,4,5,6])
check_even_list([1,3,5])


# In[3]:


stock_prices = [('AAPL',200),('GOOG',300),('MSFT',400)]
for item in stock_prices:
    print(item)
for stock,price in stock_prices:
    print(stock)
for stock,price in stock_prices:
    print(price)


# In[4]:


work_hours = [('Abby',100),('Billy',400),('Cassie',800)]
def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''   
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return (employee_of_month,current_max)
employee_check(work_hours)


# In[ ]:


example = [1,2,3,4,5]
from random import shuffle
shuffle(example)
example
[3, 1, 4, 5, 2]

mylist = [' ','O',' ']
def shuffle_list(mylist):
    shuffle(mylist)
    
    return mylist
mylist 
[' ', 'O', ' ']
shuffle_list(mylist)
[' ', ' ', 'O']
def player_guess():  
    guess = ''   
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0, 1, or 2:  ")   
    return int(guess)    
player_guess()


# In[ ]:


def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct Guess!')
    else:
        print('Wrong! Better luck next time')
        print(mylist)
mylist = [' ','O',' ']
mixedup_list = shuffle_list(mylist)
guess = player_guess()
check_guess(mixedup_list,guess)


# In[ ]:


def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)
lesser_of_two_evens(2,4)


# In[ ]:


def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]
animal_crackers('Levelheaded Llama')
animal_crackers('Crazy Kangaroo')


# In[ ]:


def makes_twenty(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20
makes_twenty(20,10)


# In[ ]:


def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'
old_macdonald('macdonald')


# In[ ]:


#volume of a sphere
def vol(rad):
    return (4/3)*(3.14)*(rad**3)
vol(2)


# In[ ]:


#number in a given range
def ran_check(num,low,high):
    if num in range(low,high+1):
        print('{} is in the range between {} and {}'.format(num,low,high))
    else:
        print('The number is outside the range.')
ran_check(5,2,7)
ran_check(8, 2, 7)


# In[ ]:


#same with Boolean
def ran_bool(num,low,high):
    return num in range(low,high+1)
ran_bool(3,1,10)
ran_check(8, 2, 7)


# In[ ]:


#number of upper case letters
def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


# In[ ]:


#list with only unique elements
def unique_list(lst):
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])


# In[ ]:


#multiply all the numbers in a list
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
multiply([1,2,3,-4])


# In[ ]:


def palindrome(s):
        s = s.replace(' ','')
        return s == s[::-1]   
palindrome('nurses run')
palindrome('abcba')


# In[ ]:


import string
def ispangram(str1, alphabet=string.ascii_lowercase): 
    alphaset = set(alphabet)  
    str1 = str1.replace(" ",'')
    str1 = str1.lower()
    str1 = set(str1)
    return str1 == alphaset
ispangram("The quick brown fox jumps over the lazy dog")
string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'


# In[ ]:




