#!/usr/bin/env python
# coding: utf-8

# In[1]:

#dog year converter
dog_years=input('please tell me how much dog years you want to convert into human years: ')
if (dog_years.isdigit()):

    if (int(dog_years)<3):
        human_years=int(dog_years)*12
        print(human_years)
    elif(int(dog_years)>20):
        print('Number is too big!!')
    elif (int(dog_years)>=3):
        human_years=2*12+(int(dog_years)-2)*4
        print(human_years,'human years')
else:
    print('HAS TO BE NUMBER')


# In[2]:

#cat year converter
cat_years=input('Please tell me how much cat years you want to convert into human years: ')
if (cat_years.isdigit()):
   
    if (int(cat_years)==1):
        human_year_1=15
        print(human_year_1)
    elif (int(cat_years)==2):
        human_year_2=24
        print(human_year_2)
    elif(int(cat_years)>20):
        print('Number is too big!!')
    elif(int(cat_years)>3):
        human_years=24+(int(cat_years)-2)*4
        print(human_years,'human years') 
else:
    print('HAS TO BE NUMBER')


# In[4]:

#password
import time
x='hello'
user_answer=input('what is the password choose a word: ')
counter=1
while not(user_answer==x):
    print('wrong password! Try again in 10 seconds')
   
    time.sleep(10)
    user_answer=input('what is the password choose a word: ')
    
    if (counter>3):
        print ('You have tried too many times! GAME OVER!',counter)
        break
    counter=counter+1 
print('correct password! Your in!')        


# In[ ]:




