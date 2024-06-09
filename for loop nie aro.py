## 1. Basic Looping Through a List
**কাজ**: একটি লিস্টের প্রতিটি উপাদানকে iterate করে প্রক্রিয়াজাত করা।

**কিভাবে কাজ করে**: `for` কীওয়ার্ড ব্যবহার করে লিস্টের প্রতিটি আইটেমকে loop এর ভিতরে iterate করা হয়।

#### উদাহরণ:
```python
# উদাহরণ ১
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
**Output:**
```
apple
banana
cherry
```

```python
# উদাহরণ ২
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number * 2)
```
**Output:**
```
2
4
6
8
10
```

```python
# উদাহরণ ৩
animals = ["cat", "dog", "rabbit"]
for animal in animals:
    print(f"I love {animal}s!")
```
**Output:**
```
I love cats!
I love dogs!
I love rabbits!
```

```python
# উদাহরণ ৪
cities = ["Dhaka", "Chittagong", "Khulna"]
for city in cities:
    print(city.upper())
```
**Output:**
```
DHAKA
CHITTAGONG
KHULNA
```

```python
# উদাহরণ ৫
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(f"Hello, {name}!")
```
**Output:**
```
Hello, Alice!
Hello, Bob!
Hello, Charlie!
```

## 2. Looping Through a String
**কাজ**: একটি স্ট্রিংয়ের প্রতিটি ক্যারেক্টারকে iterate করা।

**কিভাবে কাজ করে**: স্ট্রিংকে iterate করার জন্য `for` লুপ ব্যবহার করা হয় এবং প্রতিটি ক্যারেক্টার লুপের ভিতরে প্রক্রিয়াজাত করা হয়।

#### উদাহরণ:
```python
# উদাহরণ ১
name = "Python"
for letter in name:
    print(letter)
```
**Output:**
```
P
y
t
h
o
n
```

```python
# উদাহরণ ২
word = "programming"
for char in word:
    print(char.upper())
```
**Output:**
```
P
R
O
G
R
A
M
M
I
N
G
```

```python
# উদাহরণ ৩
sentence = "Hello World"
for char in sentence:
    if char != " ":
        print(char)
```
**Output:**
```
H
e
l
l
o
W
o
r
l
d
```

```python
# উদাহরণ ৪
greeting = "Good Morning"
for char in greeting:
    print(f"Character: {char}")
```
**Output:**
```
Character: G
Character: o
Character: o
Character: d
Character:
Character: M
Character: o
Character: r
Character: n
Character: i
Character: n
Character: g
```

```python
# উদাহরণ ৫
phrase = "Data Science"
for char in phrase:
    print(f"{char} - ASCII: {ord(char)}")
```
**Output:**
```
D - ASCII: 68
a - ASCII: 97
t - ASCII: 116
a - ASCII: 97
  - ASCII: 32
S - ASCII: 83
c - ASCII: 99
i - ASCII: 105
e - ASCII: 101
n - ASCII: 110
c - ASCII: 99
e - ASCII: 101
```

## 3. Using the `range()` Function
**কাজ**: একটি নির্দিষ্ট সংখ্যক বার loop চালানো।

**কিভাবে কাজ করে**: `range()` ফাংশন ব্যবহার করে নির্দিষ্ট সংখ্যক বার loop চালানো হয়।

#### উদাহরণ:
```python
# উদাহরণ ১
for i in range(5):
    print(i)
```
**Output:**
```
0
1
2
3
4
```

```python
# উদাহরণ ২
for i in range(1, 6):
    print(i)
```
**Output:**
```
1
2
3
4
5
```

```python
# উদাহরণ ৩
for i in range(0, 10, 2):
    print(i)
```
**Output:**
```
0
2
4
6
8
```

```python
# উদাহরণ ৪
for i in range(5, 0, -1):
    print(i)
```
**Output:**
```
5
4
3
2
1
```

```python
# উদাহরণ ৫
for i in range(3):
    print(f"Loop iteration: {i}")
```
**Output:**
```
Loop iteration: 0
Loop iteration: 1
Loop iteration: 2
```

## 4. Looping Through a Dictionary
**কাজ**: একটি ডিকশনারির key এবং value-এর উপর iterate করা।

**কিভাবে কাজ করে**: `for` লুপ ব্যবহার করে ডিকশনারির প্রতিটি key এবং value-এর উপর iterate করা হয়।

#### উদাহরণ:
```python
# উদাহরণ ১
student_grades = {"John": 90, "Emily": 85, "Alice": 95}
for student, grade in student_grades.items():
    print(f"{student}: {grade}")
```
**Output:**
```
John: 90
Emily: 85
Alice: 95
```

```python
# উদাহরণ ২
person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")
```
**Output:**
```
name: Alice
age: 25
city: New York
```

```python
# উদাহরণ ৩
inventory = {"apples": 10, "bananas": 5, "oranges": 7}
for fruit, quantity in inventory.items():
    print(f"We have {quantity} {fruit}")
```
**Output:**
```
We have 10 apples
We have 5 bananas
We have 7 oranges
```

```python
# উদাহরণ ৪
prices = {"pen": 1.5, "notebook": 2.0, "eraser": 0.5}
for item, price in prices.items():
    print(f"The price of {item} is {price} dollars")
```
**Output:**
```
The price of pen is 1.5 dollars
The price of notebook is 2.0 dollars
The price of eraser is 0.5 dollars
```

```python
# উদাহরণ ৫
phone_book = {"Alice": "123-456-7890", "Bob": "987-654-3210", "Charlie": "555-555-5555"}
for name, number in phone_book.items():
    print(f"{name}'s phone number is {number}")
```
**Output:**
```
Alice's phone number is 123-456-7890
Bob's phone number is 987-654-3210
Charlie's phone number is 555-555-5555
```

## 5. Nested For Loop
**কাজ**: লুপের ভিতরে আরেকটি লুপ চালানো।

**কিভাবে কাজ করে**: একটি লুপের ভিতরে আরেকটি লুপ ব্যবহার করে একটি মাল্টি-ডাইমেনশনাল প্রক্রিয়াকরণ করা হয়।

#### উদাহরণ:
```python
# উদাহরণ ১
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")
```
**Output:**
```
i = 1, j = 1
i = 1, j = 2
i = 1, j = 3
i = 2, j = 1
i = 2, j = 2
i = 2, j = 3
i = 3, j = 1
i = 3, j = 2
i = 3, j = 3
```

```python
# উদাহরণ ২
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for item in row:
        print(item)
```
**Output:**
```
1
2
3
4
5
6
7
8
9
```

```python
# উদাহরণ ৩
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")
```
**Output:**
```
i = 0, j = 0
i = 0, j = 1
i = 1, j = 0
i = 1, j = 1
i = 2, j = 0
i = 2, j = 1
```

```python
# উদাহরণ ৪
for

 letter in 'ABC':
    for number in range(1, 4):
        print(f"{letter}{number}")
```
**Output:**
```
A1
A2
A3
B1
B2
B3
C1
C2
C3
```

```python
# উদাহরণ ৫
colors = ["red", "green", "blue"]
shapes = ["circle", "square"]
for color in colors:
    for shape in shapes:
        print(f"{color} {shape}")
```
**Output:**
```
red circle
red square
green circle
green square
blue circle
blue square
```

## 6. Looping With Conditions
**কাজ**: লুপের ভিতরে শর্ত ব্যবহার করে নির্দিষ্ট কার্য সম্পাদন করা।

**কিভাবে কাজ করে**: `if` এবং `else` শর্ত ব্যবহার করে লুপের ভিতরে নির্দিষ্ট কাজ করা হয়।

#### উদাহরণ:
```python
# উদাহরণ ১
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
```
**Output:**
```
1 is odd
2 is even
3 is odd
4 is even
5 is odd
6 is even
```

```python
# উদাহরণ ২
temperatures = [22, 18, 30, 15, 25]
for temp in temperatures:
    if temp > 20:
        print(f"{temp} degrees is warm")
    else:
        print(f"{temp} degrees is cold")
```
**Output:**
```
22 degrees is warm
18 degrees is cold
30 degrees is warm
15 degrees is cold
25 degrees is warm
```

```python
# উদাহরণ ৩
scores = [95, 67, 88, 79, 50]
for score in scores:
    if score >= 80:
        print(f"Score {score} is excellent")
    elif score >= 60:
        print(f"Score {score} is good")
    else:
        print(f"Score {score} is poor")
```
**Output:**
```
Score 95 is excellent
Score 67 is good
Score 88 is excellent
Score 79 is good
Score 50 is poor
```

```python
# উদাহরণ ৪
for num in range(1, 11):
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} is divisible by both 3 and 5")
    elif num % 3 == 0:
        print(f"{num} is divisible by 3")
    elif num % 5 == 0:
        print(f"{num} is divisible by 5")
    else:
        print(f"{num} is not divisible by 3 or 5")
```
**Output:**
```
1 is not divisible by 3 or 5
2 is not divisible by 3 or 5
3 is divisible by 3
4 is not divisible by 3 or 5
5 is divisible by 5
6 is divisible by 3
7 is not divisible by 3 or 5
8 is not divisible by 3 or 5
9 is divisible by 3
10 is divisible by 5
```

```python
# উদাহরণ ৫
marks = [56, 78, 90, 34, 65]
for mark in marks:
    if mark >= 75:
        print(f"Mark {mark} is distinction")
    elif mark >= 50:
        print(f"Mark {mark} is pass")
    else:
        print(f"Mark {mark} is fail")
```
**Output:**
```
Mark 56 is pass
Mark 78 is distinction
Mark 90 is distinction
Mark 34 is fail
Mark 65 is pass
```

## 7. Looping Through Two Lists Using `zip()`
**কাজ**: দুইটি লিস্টের উপাদানগুলিকে একসাথে iterate করা।

**কিভাবে কাজ করে**: `zip()` ফাংশন ব্যবহার করে দুইটি লিস্টের উপাদান একসাথে iterate করা হয়।

#### উদাহরণ:
```python
# উদাহরণ ১
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")
```
**Output:**
```
Alice scored 85
Bob scored 92
Charlie scored 78
```

```python
# উদাহরণ ২
colors = ["red", "green", "blue"]
items = ["apple", "leaf", "sky"]
for color, item in zip(colors, items):
    print(f"The {item} is {color}")
```
**Output:**
```
The apple is red
The leaf is green
The sky is blue
```

```python
# উদাহরণ ৩
students = ["John", "Emily", "Sam"]
grades = ["A", "B", "A"]
for student, grade in zip(students, grades):
    print(f"{student} got grade {grade}")
```
**Output:**
```
John got grade A
Emily got grade B
Sam got grade A
```

```python
# উদাহরণ ৪
countries = ["USA", "Canada", "Australia"]
capitals = ["Washington, D.C.", "Ottawa", "Canberra"]
for country, capital in zip(countries, capitals):
    print(f"The capital of {country} is {capital}")
```
**Output:**
```
The capital of USA is Washington, D.C.
The capital of Canada is Ottawa
The capital of Australia is Canberra
```

```python
# উদাহরণ ৫
first_names = ["John", "Jane", "Jim"]
last_names = ["Doe", "Smith", "Brown"]
for first_name, last_name in zip(first_names, last_names):
    print(f"{first_name} {last_name}")
```
**Output:**
```
John Doe
Jane Smith
Jim Brown
```

## 8. Looping With `enumerate()`
**কাজ**: লুপে index এবং value দুটোই পাওয়া যায়।

**কিভাবে কাজ করে**: `enumerate()` ফাংশন ব্যবহার করে লুপে প্রতিটি আইটেমের সাথে তার index পাওয়া যায়।

#### উদাহরণ:
```python
# উদাহরণ ১
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index {index} is {color}")
```
**Output:**
```
Index 0 is red
Index 1 is green
Index 2 is blue
```

```python
# উদাহরণ ২
students = ["John", "Emily", "Sam"]
for index, student in enumerate(students):
    print(f"Student {index + 1}: {student}")
```
**Output:**
```
Student 1: John
Student 2: Emily
Student 3: Sam
```

```python
# উদাহরণ ৩
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```
**Output:**
```
0: apple
1: banana
2: cherry
```

```python
# উদাহরণ ৪
letters = ["A", "B", "C", "D"]
for index, letter in enumerate(letters):
    print(f"Letter at position {index} is {letter}")
```
**Output:**
```
Letter at position 0 is A
Letter at position 1 is B
Letter at position 2 is C
Letter at position 3 is D
```

```python
# উদাহরণ ৫
tasks = ["task1", "task2", "task3"]
for index, task in enumerate(tasks, start=1):
    print(f"Task {index}: {task}")
```
**Output:**
```
Task 1: task1
Task 2: task2
Task 3: task3
```

## 9. Looping With List Comprehensions
**কাজ**: লুপের মাধ্যমে নতুন লিস্ট তৈরি করা।

**কিভাবে কাজ করে**: লিস্ট comprehension ব্যবহার করে একটি এক-লাইন কোডে লুপ চালিয়ে একটি নতুন লিস্ট তৈরি করা হয়।

#### উদাহরণ:
```python
# উদাহরণ ১
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)
```
**Output:**
```
[1, 4, 9, 16, 25]
```

```python
# উদাহরণ ২
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(upper_words)
```
**Output:**
```
['HELLO', 'WORLD', 'PYTHON']
```

```python
# উদাহরণ ৩
evens = [num for num in range(10) if num % 2 == 0]
print(evens)
```
**Output:**
```
[0, 2, 4, 6, 8]
```

```python
# উদাহরণ ৪


fruits = ["apple", "banana", "cherry"]
fruit_lengths = [len(fruit) for fruit in fruits]
print(fruit_lengths)
```
**Output:**
```
[5, 6, 6]
```

```python
# উদাহরণ ৫
squares = [x**2 for x in range(10)]
print(squares)
```
**Output:**
```
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## 10. Loop With `break` and `continue`
**কাজ**: `break` এবং `continue` ব্যবহার করে লুপ নিয়ন্ত্রণ করা।

**কিভাবে কাজ করে**: `break` কীওয়ার্ড দিয়ে লুপ থামানো হয় এবং `continue` কীওয়ার্ড দিয়ে লুপের বাকি অংশ বাদ দিয়ে পরবর্তী iteration এ যাওয়া হয়।

#### উদাহরণ:
```python
# উদাহরণ ১
for num in range(10):
    if num == 5:
        break
    print(num)
```
**Output:**
```
0
1
2
3
4
```

```python
# উদাহরণ ২
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)
```
**Output:**
```
1
3
5
7
9
```

```python
# উদাহরণ ৩
for num in range(1, 6):
    if num == 3:
        break
    print(f"Number: {num}")
```
**Output:**
```
Number: 1
Number: 2
```

```python
# উদাহরণ ৪
for letter in "python":
    if letter == "h":
        continue
    print(letter)
```
**Output:**
```
p
y
t
o
n
```

```python
# উদাহরণ ৫
for i in range(5):
    for j in range(5):
        if i == j:
            break
        print(f"i={i}, j={j}")
```
**Output:**
```
i=0, j=0
i=1, j=0
i=2, j=0
i=2, j=1
i=3, j=0
i=3, j=1
i=3, j=2
i=4, j=0
i=4, j=1
i=4, j=2
i=4, j=3
```

এই নোটগুলো Python For Loop-এর বিভিন্ন ব্যবহার এবং তাদের উদাহরণ সহ বিস্তারিতভাবে তুলে ধরা হয়েছে। আশা করি এগুলো আপনাকে For Loop সম্পর্কে ভালোভাবে বুঝতে সাহায্য করবে।