#!/usr/bin/env python
# coding: utf-8

# # Muhammad Siddiq 19B-071-SE

# Pracrice problem 2.1

# In[5]:


n = 5
sum_num = (n * (n + 1)) / 2
print(sum_num)


# In[15]:


def Average(lst): 
    return sum(lst) / len(lst)
lst = [23, 19, 21] 
average = Average(lst)
print("Average of the list =",round(average, 2)) 


# In[18]:


#number of times:
ans= 403 // 73
print(ans)


# In[19]:


#Remainder
a= 403 % 73
print(a)


# In[20]:


#power
x = 2**10
print(x)


# In[22]:


#Difference
Differenceofheights= 54 - 57
print (abs(Differenceofheights))


# In[25]:


#lowest price
x=min('34.99', '29.95', '31.50')
print (x)


# Practice problem 2.2

# In[26]:


#sum of 2+2 is less than 4
2+2<4


# In[30]:


#Boolean
7 // 4== 1+1


# In[31]:


#Sum and squared
3 ** 2 + 4 ** 2 == 25


# In[33]:


#sum is greater
2+4+6 > 12


# In[35]:


#Divisblilty
1387 % 19 == 0


# In[36]:


#even number
31 % 2 == 0


# In[37]:


x = min(34.99, 29.95, 31.50)
y = 30.00
x<y


# Problem 2.3

# In[38]:


#Assign variable
a=3
a


# In[39]:


#Assign variable
b=4
b


# In[40]:


#Assign C
c= a * a + b * b
c


# Problem 2.4

# In[15]:


s1= 'ant'
s2= 'bat'
s3= 'cod'

print(s1+" "+s2+" "+s3)
print(10*(s1+" "))
print(s1+" "+2*(s2+" ")+3*(s3+" "))
print(7*(s1+" "+s2+" "))
print(5*(2*s2+s3+" "))


# Program 2.5

# In[10]:


#Indexing
s = '0123456789'
print(s[0])
print(s[1])
print(s[6])
print(s[8])
print(s[-1])


# Problem 2.6

# In[19]:


words = ['bat','ball','barn','basket','badminton']
print(words[0])
print(words[-1])


# Problem 2.7

# In[1]:


grades=[9,7,7,10,3,9,6,6,2]
grades.count(7)


# In[5]:


#b
grades[-1]=4
grades


# In[3]:


#c
max(grades)


# In[4]:


#d
grades.sort
grades


# In[7]:


#e
sum(grades)/len(grades)


# Problem 2.8

# In[9]:


#a
a=4
((2+3)==4) or (a >=5)


# In[10]:


#b
lst=[1,2,4,5]
((lst[1]*-3)< -10 ==0)


# In[14]:


#c
(((lst[1]*(-3)) <-10)) in [0,True]


# In[15]:


#d
2*(3**2)


# In[17]:


#e
(4/2) in [1,2,3]


# Problem 2.9

# In[19]:


#a
False+False


# In[20]:


#b
x= 2* (3**2.0)
type(x)


# In[21]:


#c
y= (4//2) + (4%2)
type(y)


# In[4]:


#d
z = ((2+3)==4) or (5>=5)
type(z)


# Problem 2.10

# In[9]:


#a
import math
a=eval(input("base:"))
b=eval(input("height:"))
c=math.sqrt(a**2 + b**2)
print("Hypotenuse is:",c)


# In[10]:


#b
c==5


# In[12]:


#c
import math
a=eval(input("radius:"))
area=math.pi * a**2
print("Area of a disk:",area)


# In[2]:


#d
x=eval(input("x-point:"))
y=eval(input("y-point:"))
r=eval(input("value of radius:"))
a=eval(input("distance of a:"))
b=eval(input("distance of b:"))

if (x-a)**2 + (y-b) < r**2:
    print("hit")
else:
    print("miss")


# # EXERCISES

# 2.11
# 

# In[12]:


#a
def sumNegative(list):
    m = 0
    for x in list:
        if x < 0:
            m+=x
    return(int(m))

a = [-7,-6,-5,-4,-3,-2,-1,0]
print (sumNegativeInts(a))


# In[2]:


#b
ages=[(17*9),(24*10),(21*11),(27*12)]
total=17 + 24 + 21 + 27
avg=sum(ages)/total
print(int(avg))


# In[3]:


#c
2**-20


# In[6]:


#d
4365%61


# In[7]:


#e
4365//61


# 2.12

# In[9]:


s1='_'
s2='+'
s1+s2


# In[11]:


s1+s2+s1


# In[12]:


s2+s1+s1


# In[13]:


s2+2*s1+s2+2*s1


# In[14]:


10*(s2+2*s1)


# In[15]:


5*(s2+s1+3*s2+2*s1)


# 2.13

# In[20]:


a= 'abcdefghijklmnopqrstuvwxyz'
print(a[0])
print(a[2])
print(a[25])
print(a[24])
print(a[16])


# 2.14

# In[24]:


s='goodbye'
s[0]=='g'


# In[25]:


s[7]=='g'


# In[4]:


s='goodbye'
s[0:1]=='g' or'a'


# In[37]:


#d


# In[10]:


len(s)/2
s[3:4] =='d' or 'd'


# In[11]:


s[0]==s[-1]


# In[19]:


#g


# 2.15

# In[20]:


x = ['a', 'n', 'a', 'c', 'h', 'r', 'o', 'n', 'i', 's', 't', 'i', 'c', 'a', 'l' ,'l' ,'y']
y = ['c', 'o', 'u', 'n', 't', 'e', 'r', 'i', 'n', 't', 'u', 'i', 't', 'i', 'v', 'e']
c = len(x)
d = len(y)
diff = int(c - d)
print('the difference between the characters of the given words:' )
print(diff)
print(" ")


# In[21]:


a = ['misrepresentation','misinterpretation']
print("Before sorting alphabetically: ")
print(a)
print("After sorting alphabetically: ")
a.sort()
print(a)
print("")


# In[22]:


lst = ['f','l','o','c','c','i','n','a','u','c','i','n','i','h','i','l','i','p','i','l','i','f','i','c','a','t','i','o','n']
'e' in lst


# In[23]:


a = ['c','o','u','n','t','e','r','r','e','v','o','l','u','t','i','o','n']
b = ['c','o','u','n','t','e','r']
c = ['r','e','s','o','l','u','t','i','o','n']
d = len(a)
e = len(b)
f = len(c)
sum = e + f
Diff = d - sum
print("The character in lst a is equal to the sum of b and c: ")
print(Diff)
d == sum


# 2.16

# In[26]:


a=6
b=7
c=(a+b)/2
print(c)


# In[27]:


inventory = ['paper','staples','pencils']
print(inventory)


# In[28]:


first= 'John'
middle= 'Fitzgerald'
last= 'Kennedy'
print("full name is: "+ first + " " + middle + " " + last)


# 2.17

# In[29]:


17+(-9)<10


# In[31]:


#b


# In[33]:


c<=24


# In[43]:


a<=6.75<=b


# In[45]:


print(len(first)<len(middle))
print(len(last)>len(middle))


# In[46]:


#f


# 2.18

# In[64]:


flowers=['rose','bougainvillea','yucca','marigold','daylilly','lilly of the valey']
print('potato' in flowers)
print(flowers) 


# In[76]:


thorny=flowers[0:5]
thorny


# In[70]:


poisonous=flowers[-1]
poisonous


# In[77]:


#e


# 2.19

# In[85]:


answer=5*['x','y']
numYes_Y=answer.count('x')
print(numYes_Y)
numNo_X=answer.count('y')
print(numNo_X)
#c
answer.sort()
print(answer)
answer[0]='f'
print(answer)





# 2.20

# In[87]:


s=input("string:")
s.reverse()
print(s)
#string haven't any built-in reverse function


# 2.21

# In[ ]:


#remain


# 2.22

# In[ ]:


#remain


# 2.23

# In[88]:


monthsL = ['jan','feb','mar','may']
monthsT = ('jan', 'feb','mar','may')
monthsL.insert(3, 'apr')
print(monthsL)
monthsT.insert(3, 'apr')


# In[89]:


monthsL = ['jan','feb','mar','may']
monthsT = ('jan', 'feb','mar','may')
monthsL.append('jun')
print(monthsL)
monthsT.append('jun')
print(monthsT)


# In[90]:


monthsL = ['jan','feb','mar','may']
monthsT = ('jan', 'feb','mar','may')
monthsL.pop()
print(monthsL)
monthsT.pop()
print(monthsT)


# In[91]:


monthsL = ['jan','feb','mar','may']
monthsT = ('jan', 'feb','mar','may')
monthsL.remove('feb')
print(monthsL)
monthsT.remove('feb')
print(monthsT)


# In[92]:


monthsL = ['jan','feb','mar','may']
monthsT = ('jan', 'feb','mar','may')
monthsL.sort(reverse= True)
print(monthsL)
monthsT.sort(reverse= True)
print(monthsT)


# In[93]:


monthsL = ['jan','feb','mar','may']
monthsT = ('jan', 'feb','mar','may')
monthsL.sort()
print(monthsL)
monthsT.sort()
print(monthsT)


# 2.24

# In[11]:


grades=['B','B','F','C','B','A','A','D','C','D','A','A','B']
print(grades.count('A'),",",grades.count('B'),",",grades.count('C'),",",grades.count('D'),",",grades.count('F'))



# 2.25

# In[17]:


#remain


# 2.26

# In[16]:


import math
r=10
X=0
Y=0
a= math.sqrt((0-0)**2 + (0-0)**2)
if a<r:
    print('hit')
else:
    print('miss')


# In[13]:


b= math.sqrt((10-0)**2 + (10-0)**2)
if b<r:
    print('hit')
else:
    print('miss')


# In[14]:


c= math.sqrt((6-0)**2 + (6-0)**2)
if c<r:
    print('hit')
else:
    print('miss')


# In[15]:


d= math.sqrt((8-0)**2 + (7-0)**2)
if d<r:
    print('hit')
else:
    print('miss')


# 2.27

# In[18]:


from math import sin
from math import pi
#a) 16 feet and 75 degree 
height = 16 * sin(pi * (75/180))
print("answer a)" + str(height))
#b) 20 feet and 0 degree
height = 20 * sin(pi * (0/180))
print("answer b)" + str(height))
#c) 24 feet and 45 degree
height = 24 * sin(pi* (45/180))
print("answer c)" + str(height))
#d) 24 feet and 80 degree
height = 24 * sin(pi *(80/180))
print("answer d)" + str(height))


# 2.28

# In[19]:


lst = [2, 5, 7, 10, 8, 9, 12]
#a) index of middle element
mid_index = int(len(lst)/2)
print(mid_index)
#b) middle element of list 
print("middle element of the list is:" + str(lst[3]))
#c) sorting list in descending order
lst.sort(reverse= True)
print(lst)
#d) remove and extend
lst.remove(12)
lst.extend([12])
print(lst)   


# 2.29

# In[32]:


#Remain


# 2.30

# In[26]:


def convert(string):
    li=list(string.split(" "))
    return li
string = "siddiq shaikh"
print(convert(string))


# In[ ]:




