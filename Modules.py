#!/usr/bin/env python
# coding: utf-8

# In[2]:


from MyMainPackage.some_main_script import report_main
from MyMainPackage.SubPackage import mysubscript

def sub_report():
    print("Hey Im a function inside mysubscript")


def report_main():
    print("Hey I am in some_main_script in main package.")


def my_func():
    print("Hey I am in mymodule.py")



report_main()
mysubscript.sub_report()


# In[6]:


# file one.py
def func():
        print("func() in one.py")

print("top-level in one.py")

if __name__ == "__main__":
        print("one.py is being run directly")
else:
        print("one.py is being imported into another module")


# In[9]:


# file two.py
import one

print("top-level in two.py")
one.func()

if __name__ == "__main__":
        print("two.py is being run directly")
else:
        print("two.py is being imported into another module")


# In[10]:


def func():
    print("func() ran in one.py")

print("top-level print inside of one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")



import one

print("top-level in two.py")

one.func()

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")


# In[ ]:





# In[ ]:




