# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists are comma separated values in a square bracket. List indices start at 0 and can be sliced or concatenated. 
>> Tuples are used when the position of an element indicates something about its capability. It is immutable unlike list so you cannot modifiy it. 
>> Only immutable elements can be used as dictionary keys. Therefore tupes work but lists don't. It must be hashable.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are both comma separated values but lists are in square brackets while sets are in curly brackets. They are both mutable objects. The main difference is that a value can appear only once in set. Converting from list to set is used when eliminating duplicates. When a list grows really large and program performance becomes slow, it's better to use set. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda form is anonymous functions created at runtime. It's definition does not include "return" statement but always contain an expression which is returned. It can be used for passion a function to another function and is very useful

<b>Example 1</b> <br>
>> (lambda x: sorted(x))(a) <br>
[1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 6, 6, 6, 7, 7, 8, 9]

<b>Example 2</b> <br>
>> b=[[1,2,3],[1,2],[4,2,3,4]] <br>
>> b = sorted(b, key=lambda x:sum(x)) <br>
>> b <br>
>> [[1, 2], [1, 2, 3], [4, 2, 3, 4]] <br>

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are used for constructing lists in a natural way. The result will be a new list resulting form evaluating the expression in the context of the for clause. <br>
>> S = [x**2 for x in range(10)] <br>
>> S <br>
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81] <br>

This can be written in map as below. The map call is similar to the list comprehension expression but it applies a function call to each item insteaed of an arbitrary. Therefore it has limitations compared to comprehensions. However, map usually requires less coding and faster for built-in functions. For any other expressions, list/set/dict comprehensions are faster in performance. <br>
>> b = map(lambda x: x**2, range(10))
>> b <br>
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

filter extracts each element in the sequence for which the function returns True
>> c = list(filter(lambda x: x >5, range(10))) <br>
>> c <br>
[6, 7, 8, 9]


set/dict comprehensions are basically same as list comprehensions,

>>> a = {(x, x**2) for x in range(10)} <br>
>>> a <br>
set([(6, 36), (0, 0), (7, 49), (4, 16), (5, 25), (3, 9), (9, 81), (2, 4), (1, 1), (8, 64)])

>>> print {i : chr(65+i) for i in range(10)} <br>
{0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'}

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   

>>
a.  datetime.datetime.strptime(date_stop, '%m-%d-%Y') - datetime.datetime.strptime(date_start, '%m-%d-%Y')  <br>
datetime.timedelta(937) <br>
937 days <br>
```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```
>>
b.  datetime.datetime.strptime(date_stop, '%m%d%Y') - datetime.datetime.strptime(date_start, '%m%d%Y') <br>
datetime.timedelta(513) <br>
513 days <br>
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 

c.  datetime.datetime.strptime(date_stop, '%d-%b-%Y') - datetime.datetime.strptime(date_start, '%d-%b-%Y') <br>
datetime.timedelta(7850) <br>
7850 days <br>
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





