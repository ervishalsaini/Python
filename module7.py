# 1. Write a Python program to check if a number is positive, negative or zero.
# x = int(input("Enter the number : ")) 
# print('Number is postive') if x>0 else print('Number is negative') if x <0 else print('Number is zero')

# 2. Write a Python program to get the Factorial number of given numbers.
# x = int(input("Enter the number : ")) 
# facto = 1
# while(x>0):
#     facto = facto*(x)
#     x-= 1
# print(f'The factorial of given number is {facto}')

# 3. Write a Python program to get the Fibonacci series of given range. 
# x = int(input("Enter the number : "))
# a = 0
# b = 1
# for i in range(x):
#     print(a)
#     c = a + b 
#     a = b
#     b = c

# 4. Write python program that swap two number with temp variable and without temp variable. 
# x = 25
# y = 50
# z = y
# y = x
# x = z
# print(f'The numbers after swapping is {z} and {y}')
# x = x + y 
# y = x - y 
# x = x - y
# print('The number after swapping is {} and {}'.format(x,y))


# 5.  Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user. 
# x = int(input("Enter the number : "))
# print("The number is odd") if(x%2!=0) else print("The number is even")


# 6. Write a Python program to test whether a passed letter is a vowel or not. 
# vowel = ["a","e","i","o","u"]
# def check(alphabets):
#     x = alphabets.lower()
#     if x in vowel:
#         print(f'The given alphabet is an vowel')
#     else:
#         print(f'The given alphabet is not an vowel')
# obj1 = check("I")


# 7. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 
# x = int(input("Enter the first integer : "))
# y = int(input("Enter the first integer : "))
# z = int(input("Enter the first integer : "))
# if (x==y or y==z or x==z):
#     print("The sum of three integer is zero beacause any two values are equal")
# else:
#     a = (x,y,z)
#     b = sum(a)
#     print(f'The sum of three interger is {b}')


# 8. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. 
# x = int(input("Enter the first integer : "))
# y = int(input("Enter the first integer : "))
# def check(x,y):
#     summation = x + y
#     difference = x- y 
#     if (x==y or summation==5 or abs(difference)== 5 ):
#         return True
#     else:
#         return False
# print(check(x,y))


# 9. Write a python program to sum of the first n positive integers. 
# n = int(input("Enter the first n numbers: "))
# def addition(n):
#     x = n*(n+1)/2
#     print(x)
# addition(n)


# 10. Write a Python program to calculate the length of a string. 
# x = "HELLO INDIA"
# count = 0
# for i in x:
#     count+= 1
# print(count)


# 11.  Write a Python program to count the number of characters (character frequency) in a string.
# from collections import Counter
# x = "HELLO"
# z = Counter(x)
# print(z)


# 12. Write a Python program to count occurrences of a substring in a string.
# string1 = input("Write anything you want : ")
# substring1 = input("write anything for substring: ")
# def count_of_ocuurence_of_substring(string1,substring1):
#     x = string1.count(substring1)
#     return x
# y = count_of_ocuurence_of_substring(string1,substring1)
# print(f'The ocuurence of {substring1} in {string1} is {y} times ')


# 13. Write a Python program to count the occurrences of each word in a given seqeunce.
# sentence = input("Enter a sentence: ")
# words = sentence.lower().split()

# word_frequency = {}

# for word in words:
#     if word in word_frequency:
#         word_frequency[word] += 1
#     else:
#         word_frequency[word] = 1

# for word, frequency in word_frequency.items():
#     print(f"'{word}': {frequency}")


# 14. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 
# def swapping_of_words(string1,string2):
#     x = string1[:2] + string2[2:]
#     y = string2[:2] + string1[2:]
#     res = y + " " + x
#     print(res)
# swapping_of_words("ABCD","XYZ")


# 15. Write a Python program to add 'in' at the end of a given string (length 
# should be at least 3). If the given string already ends with 'ing' then 
# add 'ly' instead if the string length of the given string is less than 3, 
# leave it unchanged. 
# def adding(string1):
#     x = len(string1)
#     if x>=3:
#         if string1[-3:].lower() == "ing":
#             return string1 + "ly"
#         else:
#             return string1 + "in"
#     else:
#         return string1 
# obj1 = adding("GOODING")
# print(obj1)


# 16. Write a Python function to reverses a string if its length is a multiple of 4. 
# string1 = "hell0"
# x = string1[ : : -1]
# y = len(x)
# if (y%4 == 0):
#     print(x)
# else:
#     print("Length of list is not a mutiple of 4 cant't reverse the given string")


# 17. Write a Python program to get a string made of the first 2 and the last 
# 2 chars from a given a string. If the string length is less than 2, return 
# instead of the empty string. 
# def check(string1):
#     x = len(string1)
#     if x > 2 :
#         y = string1[ : 2] + string1[-2: ]
#         return y
#     else:
#         return "The string is Empty"
# obj1 = check("Krishna")
# print(obj1)


# 18. Write a Python function to insert a string in the middle of a string. 
# def inserting_string(original_string, string_to_insert):
#     x = len(original_string)//2
#     result = original_string[ : x] + string_to_insert + original_string[ x: ]
#     return result
# obj1 = inserting_string("Hello, world" ," beautiful")
# print(obj1)


# 19.  Write a Python function to get the largest number, smallest num and sum of all from a list.
# list = [1,2,3,4,55,34,22,2,-5]
# def check(list):
#     x = max(list)
#     print(f'The maximum no in list is : {x}')
#     y = min(list)
#     print(f'The minimum no in list is : {y}')
#     z = sum(list)
#     print(f'The sum of all no in list is : {z}')
# check(list)


# 20. ) Write a Python program to count the number of strings where the string 
# length is 2 or more and the first and last character are same from a given list of strings.
# list = ["ABC","AA","1221","DDCD","123"]
# count = 0
# for i in list:
#     if len(i) >=2 and i[0] == i[-1] :
#         count+= 1
# print(f'The count of strong is : {count}')


# 21. Write a Python program to remove duplicates from a list. 
# list = [1,2,3,1,1,4,5,"A","B",5,"B",8.9,90,8.9,"K","R"]
# unique_list = []
# for i in list:
#     if i not in unique_list:
#         unique_list.append(i)
# print(f'The orginal list is {list} and unique list is {unique_list}')


# 22. Write a Python program to check a list is empty or not. 
# x = int(input("Enter the total no of elements you want to add in list : "))
# list = []
# i = 1
# while(i<=x):
#     y = int(input(f'Enter the  elements : '))
#     list.append(y)
#     i+= 1
# if len(list) == 0:
#     print("List is empty")
# else:
#     print("List is not empty")


# 23. Write a Python function that takes two lists and returns true if they have at least one common member. 
# def checks(list1,list2):
#     for i in list1:
#         for j in list2:
#             if i == j:
#                 return True
#             else:
#                 return False
# list1 = [1,2,3,4,5,66]
# list2 = [5,88,22]
# obj1 = checks(list1,list2)
# print(obj1)


# 24. Write a Python program to generate and print a list of first and last 5 
# elements where the values are square of numbers between 1 and 30. 
# list = [x**2 for x in range(1,31)]
# y = list[ :6] + list[-5: ]
# print(y)


# 25. Write a Python program to convert a list of characters into a string. 
# list = ["H","e","l","l","o","P","y","h","t","o","n"]
# x = "".join(list)
# print(x)


# 26. Write a Python program to select an item randomly from a list. 
# list = [1,2,3,4,5,"a",6.7]
# import random
# y = random.choice(list)
# print(y)


# 27. Write a Python program to find the second smallest number in a list. 
# x = [22,23,24,25,33,24,11,23,44]
# x.sort()
# print(x[1])


# 28. Write a Python program to check whether a list contains a sub list 
# list = [1,2,3,4,5,6,7,8,915]
# sub_list = [5,6,7]
# result  = False
# for i in range(len(list) - len(sub_list) + 1):
#     if list[i : i + len(sub_list)] == sub_list:
#         result = True
#         break
# if result:
#     print("Yes, list contains a sublist")
# else:
#     print("NO, list does not contain sublist")



# 29. Write a Python program to split a list into different variables.
# list = [1,2,3,4,"A",3.5,"22"]
# a,b,c,d,e,f,g = list
# print("variables are : ",a,b,c,d,e,f,g) 


# 30. Write a Python program to create a tuple with different data types. 
# tuple1 = (1,"A","2", 4.9,True,2.0004)
# print(tuple1)


# 31. Write a Python program to unzip a list of tuples into individual lists. 
# x = [("Krishna",100),("Vishal",88),("Amit",97)]
# y = list(zip(*x))
# for i in y:
#     print(list(i))


# 32. Write a Python program to convert a list of tuples into a dictionary. 
# x = [("Krishna",100),("Vishal",88),("Amit",97)]
# y = dict(x)
# print(y)


# 34. Write a Python script to sort (ascending and descending) a dictionary by value. 
# x = {"A":100 , "B":180 , "C":50 , "D":200}
# sorted_dict_asc = dict(sorted(x.items(), key=lambda item: item[1]))
# print("Dictionary sorted by value (ascending):", sorted_dict_asc)


# 35. Write a Python script to concatenate following dictionaries to create a new one. 
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# dict3 = {'e': 5, 'f': 6}
# dict4 = {}
# dict4.update(dict1)
# dict4.update(dict2)
# dict4.update(dict3)
# print(dict4)
 

# 36. Write a Python script to check if a given key already exists in a dictionary. 
# x = {"a":1, "b":2 ,"c":3}
# check_key = "d"
# if check_key in x.keys():
#     print(f'The key {check_key} is present having value {x[check_key]}')
# else:
#     print("Not found")


# 37. How Do You Traverse Through a Dictionary Object in Python? 
# dict1 = {"a":1,"b":2,"c":3}
# z = {y:x for x,y in dict1.items()}
# print(z)


# 38. Write a Python script to print a dictionary where the keys are numbers between 1 and 15. 
# x = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256}
# x_keys = [i for i in range(1,16)]
# dict1 = {i:x[i] for i in x_keys}
# print(dict1)


# 40. Write a Python program to check multiple keys exists in a dictionary.
# x = {"a":1,"b":2,"c":3}
# keys_check = ["a","b","d"]
# all_exist = all(i in x for i in keys_check)
# if all_exist:
#     print(f'The keys {keys_check} exist in the dictionary')
# else:
#     print(f'The keys {keys_check} not exist in the dictionary')


# 41. Write a Python program to map two lists into a dictionary.
# keys = ['a', 'b', 'c', 'd']
# values = [400, 400, 300, 400]
# result = dict((zip(keys,values))) 
# print(result)
# result = {keys[i]:values[i]   for i in range(len(keys))}
# print(result)
 
 
# 42. Write a Python program to find the highest 3 values in a dictionary.
# x = {"a":1 , "b":2, "c":10, "d":22, "e": 4, "f":23, "g":27}
# y = [i for i in x.values()]
# z = sorted(y)[ : : -1][ : 3]
# print(z)


# 43. Write a Python program to combine values in python list of dictionaries. 
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
# 300}, o {'item': 'item1', 'amount': 750}] 
# from collections import Counter
# data = [
#     {'item': 'item1', 'amount': 400},
#     {'item': 'item2', 'amount': 300},
#     {'item': 'item1', 'amount': 750}
# ]
# x = Counter()
# for i in data:
#     x[i['item']]+= i['amount']
# print(x)


# 44. )Write a Python program to create a dictionary from a string. 
# Note: Track the count of the letters from the string.
# string1 = "Hello Python"
# x = {}
# for i in string1:
#     if i in x:
#         x[i]+= 1
#     else:
#         x[i] = 1
# print(x)


# 45. Write a Python function to check whether a number is in a given range.
# x = range(1,20)
# number = int(input("Enter the Number : "))
# if number in x:
#     print("Number is in given range")
# else:
#     print("Number is not in range")


# 46. Write a Python function to check whether a number is perfect or not. 
# def perfect_number(n):
#     sum = 0
#     for i in range(1,n):
#         if n%i == 0:
#             sum+= i
#     return sum == n
# x = perfect_number(7)
# print(x)


# 47. Write a Python function that checks whether a passed string is palindrome or not.
# def check(string1):
#     x = string1[::-1]
#     if x == string1:
#         return True
#     else:
#         return False
# string1 = "ABBA"
# obj1 = check(string1)
# print(obj1)


# 48. How can you pick a random item from a list or tuple? 
# import random
# x = (1,2,3,4,5,1)
# y = random.choice(x)
# print(y)


# 49. How can you pick a random item from a range? 
# import random
# x = random.randrange(1,100)
# print(x)


# 50. How can you get a random number in python?
# import random
# x = random.random()
# print(x)
    

# 51. How will you set the starting value in generating random numbers?
# import random
# random.seed(1)
# x = random.random()
# print(x)


# 52. How will you randomize the items of a list in place? 
# import random
# x = [1,2,3,4,1,2]
# random.shuffle(x)
# print(x)


# 53. Write a Python program to read an entire text file.
# f = open("C:/Users/admin/Desktop/Soft_Skills/module1.txt","r")
# print(f.read())


# 54. Write a Python program to append text to a file and display the text.
# f = open("C:/Users/admin/Desktop/Soft_Skills/module1.txt","a") 
# f.write("Good Morning Traders ")
# f = open("C:/Users/admin/Desktop/Soft_Skills/module1.txt","r")
# x = f.read()
# print(x)
# f.close()


# 55. Write a Python program to read first n lines of a file.
# input_file = "C:/Users/admin/Desktop/Soft_Skills/module1.txt"
# N= int(input("Enter the number : "))
# with open(input_file,"r") as f:
#     x = f.readlines()
# for i in x[:N]:
#     print(i,end="")
# f.close()


# 56. Write a Python program to read last n lines of a file. 
# input_file = "C:/Users/admin/Desktop/Soft_Skills/module1.txt"
# N= int(input("Enter the number : "))
# with open(input_file,"r") as f:
#     x = f.readlines()
# for i in x[-N:]:
#     print(i,end="")
# f.close()


# 57. Write a Python program to read a file line by line and store it into a list
# input_file = "C:/Users/admin/Desktop/Soft_Skills/module1.txt"
# with open(input_file,"r") as f:
#     x = f.readlines()
# y = [i.strip() for i in x]
# print(y)


# 58. Write a Python program to read a file line by line store it into a variable.
# input_file = "C:/Users/admin/Desktop/Soft_Skills/module1.txt"
# with open(input_file,"r") as f:
#     x = f.readlines()
# count = 0
# for i in x:
#     count+= 1
#     print("line{}:{}".format(count,i))


# 59. Write a Python program to count the number of lines in a text file. 
# input_file = "C:/Users/admin/Desktop/Soft_Skills/module1.txt"
# with open(input_file,"r") as f:
#     x = f.readlines()
# count = 0
# for i in x:
#     count+= 1
# print(f'The no of lines in given is {count}')


# 60. Write a python program to find the longest words. 
# def checks(text):
#     x =text.split()
#     max_len = len(max(x,key = len))
#     return [i for i in x if len(i) == max_len]
# text = "Good morning all hope you all are good"
# obj1 = checks(text)
# print(obj1)


# 61. Write a Python program to count the frequency of words in a file.
# from collections import Counter
# import re
# def frequencycheck(filename):
#     with open(filename,"r") as f:
#         x = f.read()
#         y = re.findall(r'\b\w+\b', x.lower())
#         z =Counter(y)
#         return z
# filename = "C:/Users/admin/Desktop/Soft_Skills/module1.txt"
# obj1 = frequencycheck(filename)
# for i,j in obj1.items():
#     print(f'{i}:{j}')


# 62. Write a Python program to write a list to a file. 
# def writing(filename,list):
#     with open(filename,"w") as f:
#         for i in list:
#             f.write(f"{i}\n")
# list = ["apple","banana","cherry"]
# filename = "C:/Users/admin/Desktop/Soft_Skills/module1.txt"
# obj1 = writing(filename,list)
# print(obj1)


# 63. Write a Python program to copy the contents of a file to another file
# def copy_file_contents(source_file, destination_file):
#     with open(source_file, 'r') as src:
#         with open(destination_file, 'w') as dest:
#             for line in src:
#                 dest.write(line)

# source_file = 'source.txt'
# destination_file = 'destination.txt'

# copy_file_contents(source_file, destination_file)

# print(f"Contents of {source_file} have been copied to {destination_file}")


# 64. Write python program that user to enter only odd numbers, else will raise an exception. 
# class NotOddNumberError(Exception):
#    pass
# def getoddnumbers():
#     try:
#        x = int(input("Enter the number : "))
#        if x%2 == 0:
#          raise NotOddNumberError("the number enter is not odd")
#        print("You enter the odd number")
#     except NotOddNumberError as e:
#        print(e)

# getoddnumbers()



# 65. How Do You Handle Exceptions with Try/Except/Finally in Python? Explain with coding snippets. 
def addition(a,b):
    try:
        z = (a+b)/(a-b)
    except ZeroDivisionError:
        print("Zero Division Error occured")
    except TypeError:
        print("Type Error")
    else:
        print(z)
    finally:
        print("You Get Your Result!!!")
addition(10,"a")
























    

 



    






