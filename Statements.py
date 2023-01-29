#!/usr/bin/env python
# coding: utf-8

# In[1]:


#If, elif, else
loc = 'Bank'
if loc == 'Auto Shop':
    print('Welcome to the Auto Shop!')
elif loc == 'Bank':
    print('Welcome to the bank!')
else:
    print('Where are you?')


# In[2]:


person = 'John'
if person == 'John':
    print('Welcome John!')
else:
    print("Welcome, what's your name?")


# In[3]:


person = 'Lora'
if person == 'John':
    print('Welcome John!')
elif person =='Jack':
    print('Welcome Jack!')
else:
    print("Welcome, what's your name?")


# In[4]:


#For loops
list_1 = [1,2,3,4,5,6,7,8,9,10]
for num in list_1:
    print(num)
for num in list_1:
    if num % 2 == 0:
        print(num)
for num in list_1:
    if num % 2 == 0:
        print(num)
    else:
        print('Odd number')


# In[5]:


list_2 = [1,2,3,4,5,6,7,8,9,10]
list_sum = 0 
for num in list_2:
    list_sum = list_sum + num
print(list_sum)
for letter in 'This is a string.':
    print(letter)
tup = (1,2,3,4,5)
for t in tup:
    print(t)


# In[6]:


d = {'k1' : 1,'k2' : 2,'k3' : 3}
for item in d:
    print(item)
d.keys() 
d.values() 
d.items()


# In[7]:


for k,v in d.items():
    print(k)
    print(v) 
list(d.keys())
sorted(d.values())


# In[ ]:


#While loops
x = 0
while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
x = 0
while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('x==3')
    else:
        print('continuing...')
    continue


# In[1]:


list(range(0,11))
list(range(0,11,2))
index_count = 0
for letter in 'abcde':
    print("At index {} the letter is {}".format(index_count,letter))
    index_count += 1
for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))
list(enumerate('abcde'))


# In[2]:


mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']
zip(mylist1,mylist2)
list(zip(mylist1,mylist2))
for item1, item2 in zip(mylist1,mylist2):
    print('For this tuple, first item was {} and second item was {}'.format(item1,item2))


# In[3]:


'x' in ['x','y','z']
'x' in [1,2,3]
mylist = [10,20,30,40,100]
min(mylist)
max(mylist)


# In[4]:


mylist = [40, 10, 100, 30, 20]
from random import shuffle
shuffle(mylist)
from random import randint
randint(0,100)


# In[5]:


#List comprehension
list = [x for x in 'word']
list
list = [x**2 for x in range(0,11)]
list
list = [x for x in range(11) if x % 2 == 0]
list
list = [ x**2 for x in [x**2 for x in range(11)]]
list


# In[6]:


celsius = [0,10,20.1,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celsius ]
fahrenheit


# In[7]:


string = 'Print only the words that start with s in this sentence'
for word in string.split():
    if word[0] == 's':
        print(word)
st = 'Create a list of the first letters of every word in this string'
[word[0] for word in st.split()]    


# In[8]:


[x for x in range(1,51) if x%3 == 0]
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word)%2 == 0:
        print(word+" <-- has an even length!")


# In[9]:


for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


# In[11]:


import random

num = random.randint(1,100)
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
guesses = [0]
while True:
guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))

if guess < 1 or guess > 100:
 print('OUT OF BOUNDS! Please try again: ')
        continue
     if guess == num:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break
        
    guesses.append(guess)
if guesses[-2]:  
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
   
    else:
        if abs(num-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')


# In[ ]:




