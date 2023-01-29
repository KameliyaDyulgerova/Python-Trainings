#!/usr/bin/env python
# coding: utf-8

# In[1]:


def display_list(mylist):
    print(mylist)
mylist = [0,1,2,3,4,5,6,7,8,9,10]
display_list(mylist)


# In[3]:


input('Please enter a value: ')
result = input("Please enter a number: ")
type(result)
str
int(result)
2
result = int(input("Please enter a number: "))
type(result)
int


# In[4]:


def user_choice():
    choice = input("Please input a number (0-10)")   
    return int(choice)
user_choice()


# In[ ]:


def user_choice():
    choice = 'wrong'
    while choice.isdigit() == False:
        choice = input("Choose a number: ")
    return int(choice)
user_choice()


# In[1]:


def user_choice():
    choice = 'wrong'
    while choice.isdigit() == False:
        choice = input("Choose a number: ")
        if choice.isdigit() == False:
            print("Sorry, but you did not enter an integer. Please try again.")
    return int(choice)
user_choice()


# In[2]:


def user_choice():
    choice = 'wrong'
    while choice.isdigit() == False:
        choice = input("Choose a number: ")       
        if choice.isdigit() == False:
            clear_output()           
            print("Sorry, but you did not enter an integer. Please try again.")
    return int(choice)
user_choice()


# In[1]:


from IPython.display import clear_output
clear_output()
def user_choice():
    choice = 'wrong'
    while choice not in ['0','1','2']:
        choice = input("Choose one of these numbers (0,1,2): ")        
        if choice not in ['0','1','2']:
            clear_output()          
            print("Sorry, but you did not choose a value in the correct range (0,1,2)")
    return int(choice)
user_choice()


# In[2]:


def user_choice():  
    choice ='WRONG'
    within_range = False   
    while choice.isdigit() == False or within_range == False:  
        choice = input("Please enter a number (0-10): ")       
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")          
        if choice.isdigit() == True:
            if int(choice) in range(0,10):
                within_range = True
            else:
                within_range = False   
    return int(choice)
user_choice()


# In[5]:


game_list = [0,1,2]
def display_game(game_list):
    print("Here is the current list")
    print(game_list)
display_game(game_list)

def position_choice():
    choice = 'wrong'
    while choice not in ['0','1','2']:
        choice = input("Pick a position to replace (0,1,2): ")      
        if choice not in ['0','1','2']:
            clear_output()          
            print("Sorry, but you did not choose a valid position (0,1,2)")
    return int(choice)
user_choice()


# In[ ]:


def replacement_choice(game_list,position): 
    user_placement = input("Type a string to place at the position")    
    game_list[position] = user_placement    
    return game_list
def gameon_choice():
    choice = 'wrong'
    while choice not in ['Y','N']:
        choice = input("Would you like to keep playing? Y or N ")       
        if choice not in ['Y','N']:
            clear_output()          
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")

    if choice == "Y":
        return True
    else:
        return False


game_on = True
game_list = [0,1,2]


while game_on:
    clear_output()
    display_game(game_list)
    position = position_choice()
    game_list = replacement_choice(game_list,position)
    clear_output()
    display_game(game_list)
    game_on = gameon_choice()
    


# In[ ]:




