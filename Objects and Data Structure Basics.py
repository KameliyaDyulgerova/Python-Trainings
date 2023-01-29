#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Addition
1 + 2
#Substraction
8 - 5
#Multiplication
1 * 4
#Division
8 / 4
#Modulo
8 / 4
#Powers
2**4
(12 + 12)  / 2


# In[2]:


#Valuable assignment
a = 5
a + a
#Reassignment
a = 7
a + a
my_income = 100
tax_rate = 0.1
my_taxes = my_income*tax_rate
print(my_taxes)


# In[3]:


my_dogs = 2
print(my_dogs)
my_dogs = ['Sharo', 'Lasi']
print(my_dogs)
a = 10
a * a
a += a
a
a += 5
print(a)


# In[4]:


#Strings
'Use \n to print a new line'
a = 'Hello World'
print(a)
print(a[1])
print(a[:])
print('\n')
print(a[3:])
print(a[:4])
print(a[::5]) 
print(a[5::])
b = 'a'
print(b*8)
print(b.upper())
print(b.split('l'))


# In[5]:


#Concatenation
player = 'John'
points = 33
'Last night, '+player+' scored '+str(points)+' points.'


# In[6]:


#String formatting
f'Last night, {player} scored {points} points.'
#Formatting with placeholders
print("I'm going to inject %s here." %'something')
print("I'm going to inject %s text here, and %s text here." %('some','more'))
x, y = 'some', 'more'
print("I'm going to inject %s text here, and %s text here." %(x, y))
print('He said his name was %s.' %'John')


# In[7]:


print('I once caught a fish %s.' %'this \tbig')
print('I wrote %s programs today.' %3.75)
print('I wrote %d programs today.' %3.75) 
print('Floating point numbers: %5.2f' %(13.144))
print('Floating point numbers: %1.0f' %(13.144))
print('Floating point numbers: %1.5f' %(13.144))
print('Floating point numbers: %10.2f' %(13.144))
print('Floating point numbers: %25.2f' %(13.144))


# In[8]:


#Multiple formatting
print('First: %s, Second: %5.2f, Third: %r' %('hi!',3.1415,'bye!'))
#Formatting with ().format method

'String here {} then also {}'.format('something1','something2')
print('This is a string with an {}'.format('insert'))
print('The {2} {1} {0}'.format('fox','brown','quick'))
print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1,b='Two',c=12.3))
print('A %s saved is a %s earned.' %('penny','penny'))
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))


# In[9]:


print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))
print('This is my ten-character, two-decimal number:%10.2f' %13.579)
print('This is my ten-character, two-decimal number:{0:10.2f}'.format(13.579))


# In[10]:


#Formatted String Literals (f-strings)
name = 'Fred'

print(f"He said his name is {name}.")
print(f"He said his name is {name!r}")
num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")
num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:10.4f}")


# In[11]:


#Lists
my_list = [1,2,3]
my_list = ['A string',23,100.232,'o']
len(my_list)
my_list[0]
my_list[1:]
my_list[:3]
my_list + ['new item']


# In[12]:


# Reassignment
my_list = my_list + ['add new item permanently']
my_list
my_list * 2
#Append
list1 = [1,2,3]
list1.append('append me!')
list1
list1.pop(0)
popped_item = list1.pop()
popped_item


# In[13]:


#Reverse
new_list = ['a','e','x','b','c']
new_list
new_list.reverse()
new_list
new_list.sort()
new_list


# In[14]:


#Matrix
list_1=[1,2,3]
list_2=[4,5,6]
list_3=[7,8,9]
matrix = [list_1,list_2,list_3]
matrix
matrix[0]
matrix[0][0]
first_col = [row[0] for row in matrix]
first_col


# In[15]:


#Dictionaries
my_dict = {'key1':'value1','key2':'value2'}
my_dict['key2']
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
my_dict['key3']
my_dict['key3'][0]
my_dict['key3'][0].upper()


# In[16]:


#Substract value
my_dict['key1'] = my_dict['key1'] - 123
my_dict['key1']
d = {}
d['animal'] = 'Dog'
d['answer'] = 42
d


# In[17]:


#Nested disctionaries
d = {'key1':{'nestkey':{'subnestkey':'value'}}}
d
d = {'key1':1,'key2':2,'key3':3}
d.keys()
d.values()
d.items()


# In[18]:


#Tuples 
t = ('one', 2)
len(t)
t[0]
t[-1]
t.index('one')
t.count('one')


# In[19]:


#Sets 
x = set()
x.add(1)
x
x.add(2)
x
{1, 2}
x.add(1)
x
{1, 2}
list1 = [1,1,2,2,3,4,5,6,1,1]
set(list1)


# In[20]:


#Booleans
a = True
a
1 > 2
b = None
print(b)


# In[21]:


#Files
my_file = open("C:\\Users\\mn\\Desktop\\DWH\\Proc.txt")
my_file.read()
my_file.seek(0)
my_file.readlines()
my_file.write('This is a new line')
my_file.seek(0)
my_file.read()
my_file.close()


# In[ ]:




