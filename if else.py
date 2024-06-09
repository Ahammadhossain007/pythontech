### পাইথন `if`, `else`, এবং `elif` শর্তগুলোর উদাহরণ

#### ১. `if` স্টেটমেন্ট

**উদাহরণ ১:**
```python
a = 5
if a > 3:
    print("a is greater than 3")
```

**উদাহরণ ২:**
```python
temperature = 30
if temperature > 25:
    print("It's a hot day")
```

**উদাহরণ ৩:**
```python
score = 85
if score >= 80:
    print("You got an A")
```

**উদাহরণ ৪:**
```python
age = 18
if age >= 18:
    print("You are an adult")
```

**উদাহরণ ৫:**
```python
height = 175
if height > 150:
    print("You are tall")
```

#### ২. `else` স্টেটমেন্ট

**উদাহরণ ১:**
```python
a = 5
if a > 10:
    print("a is greater than 10")
else:
    print("a is not greater than 10")
```

**উদাহরণ ২:**
```python
temperature = 20
if temperature > 25:
    print("It's a hot day")
else:
    print("It's not a hot day")
```

**উদাহরণ ৩:**
```python
score = 65
if score >= 80:
    print("You got an A")
else:
    print("You did not get an A")
```

**উদাহরণ ৪:**
```python
age = 16
if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")
```

**উদাহরণ ৫:**
```python
height = 145
if height > 150:
    print("You are tall")
else:
    print("You are not tall")
```

#### ৩. `elif` স্টেটমেন্ট

**উদাহরণ ১:**
```python
a = 5
if a > 10:
    print("a is greater than 10")
elif a > 3:
    print("a is greater than 3 but less than or equal to 10")
else:
    print("a is 3 or less")
```

**উদাহরণ ২:**
```python
temperature = 20
if temperature > 30:
    print("It's a very hot day")
elif temperature > 25:
    print("It's a hot day")
else:
    print("It's not a hot day")
```

**উদাহরণ ৩:**
```python
score = 75
if score >= 90:
    print("You got an A")
elif score >= 80:
    print("You got a B")
else:
    print("You did not get an A or B")
```

**উদাহরণ ৪:**
```python
age = 17
if age >= 21:
    print("You can drink alcohol")
elif age >= 18:
    print("You can vote")
else:
    print("You are a minor")
```

**উদাহরণ ৫:**
```python
height = 155
if height > 180:
    print("You are very tall")
elif height > 150:
    print("You are tall")
else:
    print("You are not tall")
```

#### ৪. শর্ট হ্যান্ড `if`

**উদাহরণ ১:**
```python
a = 10
if a > 5: print("a is greater than 5")
```

**উদাহরণ ২:**
```python
temperature = 30
if temperature > 25: print("It's a hot day")
```

**উদাহরণ ৩:**
```python
score = 85
if score >= 80: print("You got an A")
```

**উদাহরণ ৪:**
```python
age = 18
if age >= 18: print("You are an adult")
```

**উদাহরণ ৫:**
```python
height = 175
if height > 150: print("You are tall")
```

#### ৫. শর্ট হ্যান্ড `if...else`

**উদাহরণ ১:**
```python
a = 5
print("a is greater than 10") if a > 10 else print("a is not greater than 10")
```

**উদাহরণ ২:**
```python
temperature = 20
print("It's a hot day") if temperature > 25 else print("It's not a hot day")
```

**উদাহরণ ৩:**
```python
score = 65
print("You got an A") if score >= 80 else print("You did not get an A")
```

**উদাহরণ ৪:**
```python
age = 16
print("You are an adult") if age >= 18 else print("You are not an adult")
```

**উদাহরণ ৫:**
```python
height = 145
print("You are tall") if height > 150 else print("You are not tall")
```

#### ৬. একাধিক `else if` (টেরনারি অপারেটর)

**উদাহরণ ১:**
```python
a = 15
print("a is greater than 20") if a > 20 else print("a is 20") if a == 20 else print("a is less than 20")
```

**উদাহরণ ২:**
```python
temperature = 28
print("Very hot day") if temperature > 35 else print("Hot day") if temperature > 25 else print("Warm day")
```

**উদাহরণ ৩:**
```python
score = 85
print("A grade") if score >= 90 else print("B grade") if score >= 80 else print("C grade")
```

**উদাহরণ ৪:**
```python
age = 17
print("Adult") if age >= 18 else print("Teenager") if age >= 13 else print("Child")
```

**উদাহরণ ৫:**
```python
height = 175
print("Very tall") if height > 180 else print("Tall") if height > 160 else print("Average height")
```

#### ৭. লজিক্যাল অপারেটর

**উদাহরণ ১ (and অপারেটর):**
```python
a = 10
b = 20
if a > 5 and b > 15:
    print("Both conditions are true")
```

**উদাহরণ ২ (and অপারেটর):**
```python
temperature = 28
humidity = 60
if temperature > 25 and humidity > 50:
    print("It's hot and humid")
```

**উদাহরণ ৩ (and অপারেটর):**
```python
score = 85
attendance = 90
if score > 80 and attendance > 85:
    print("Eligible for award")
```

**উদাহরণ ৪ (and অপারেটর):**
```python
age = 18
income = 50000
if age >= 18 and income > 40000:
    print("Eligible for loan")
```

**উদাহরণ ৫ (and অপারেটর):**
```python
height = 175
weight = 70
if height > 170 and weight < 75:
    print("Ideal body")
```

**উদাহরণ ১ (or অপারেটর):**
```python
a = 5
b = 20
if a > 10 or b > 15:
    print("At least one condition is true")
```

**উদাহরণ ২ (or অপারেটর):**
```python
temperature = 18
humidity = 60
if temperature > 25 or humidity > 50:
    print("Either hot or humid")
```

**উদাহরণ ৩ (or অপারেটর):**
```python
score = 85
attendance = 80
if score > 80 or attendance > 85:
    print("Eligible for partial award")
```

**উদাহরণ ৪ (or অপারেটর):**
```python
age = 17
income = 50000
if age >= 18 or income > 40000:
    print("Eligible for loan with conditions")
```

**উদাহরণ ৫ (or অপারেটর):**
```python
height = 165
weight = 80
if height > 170 or weight < 75:
    print("Meets one of the criteria")
```

#### ৮. নেস্টেড `if` স্টেটমেন্ট

**উদাহরণ ১:**
```python
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
```

**উদাহরণ ২:**
```python
num = 25
if num > 10:
    print("Number is greater than 10")
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
```

**উদাহরণ

৩:**
```python
marks = 75
if marks > 50:
    print("Passed")
    if marks > 75:
        print("Passed with distinction")
    else:
        print("Passed without distinction")
```

**উদাহরণ ৪:**
```python
balance = 1000
if balance > 500:
    print("Sufficient balance")
    if balance > 1500:
        print("Eligible for premium account")
    else:
        print("Eligible for basic account")
```

**উদাহরণ ৫:**
```python
age = 20
if age > 18:
    print("Adult")
    if age > 21:
        print("Eligible for drinking")
    else:
        print("Not eligible for drinking")
```

#### ৯. `pass` স্টেটমেন্ট

**উদাহরণ ১:**
```python
a = 5
if a > 3:
    pass  # TODO: implement later
```

**উদাহরণ ২:**
```python
temperature = 30
if temperature > 25:
    pass  # Placeholder for future implementation
```

**উদাহরণ ৩:**
```python
score = 85
if score >= 80:
    pass  # No action needed yet
```

**উদাহরণ ৪:**
```python
age = 18
if age >= 18:
    pass  # Adult category handling pending
```

**উদাহরণ ৫:**
```python
height = 175
if height > 150:
    pass  # Placeholder for height-related logic
```

উপরের প্রতিটি উদাহরণ পাইথনের `if`, `else`, এবং `elif` শর্তগুলোর বিভিন্ন ব্যবহারের ক্ষেত্রে প্রদর্শন করছে,
যা আপনার শর্তমূলক বিবৃতির সাথে আরও ভাল বোঝাপড়া এবং দক্ষতা বৃদ্ধি করবে।


#!!!! aro akti odaharo
### পাইথনের শর্তমূলক বিবৃতির কাজ এবং কিভাবে কাজ করে

#### ১. `if` স্টেটমেন্ট
**কাজ:** শর্ত পরীক্ষা করা এবং শর্ত সত্য হলে নির্দিষ্ট ব্লক কোড কার্যকর করা।
**কিভাবে কাজ করে:** যদি শর্তটি সত্য হয় (True), তাহলে `if` ব্লকের ভেতরের কোড কার্যকর হয়।

**উদাহরণ:**
```python
a = 5
if a > 3:
    print("a is greater than 3")
```
**কাজ:** যদি `a` এর মান ৩ এর চেয়ে বড় হয়, তাহলে "a is greater than 3" মুদ্রিত হবে।

#### ২. `else` স্টেটমেন্ট
**কাজ:** `if` শর্ত মিথ্যা হলে বিকল্প ব্লক কোড কার্যকর করা।
**কিভাবে কাজ করে:** যদি `if` শর্ত মিথ্যা (False) হয়, তাহলে `else` ব্লকের কোড কার্যকর হয়।

**উদাহরণ:**
```python
a = 5
if a > 10:
    print("a is greater than 10")
else:
    print("a is not greater than 10")
```
**কাজ:** যদি `a` এর মান ১০ এর চেয়ে বড় না হয়, তাহলে "a is not greater than 10" মুদ্রিত হবে।

#### ৩. `elif` স্টেটমেন্ট
**কাজ:** একাধিক শর্ত পরীক্ষা করা এবং প্রথম সত্য শর্তের কোড ব্লক কার্যকর করা।
**কিভাবে কাজ করে:** `if` শর্ত মিথ্যা হলে `elif` শর্ত পরীক্ষা করা হয়। যদি `elif` শর্ত সত্য হয়, তাহলে তার কোড ব্লক কার্যকর হয়।

**উদাহরণ:**
```python
a = 5
if a > 10:
    print("a is greater than 10")
elif a > 3:
    print("a is greater than 3 but less than or equal to 10")
else:
    print("a is 3 or less")
```
**কাজ:** যদি `a` এর মান ৩ এর চেয়ে বড় এবং ১০ এর চেয়ে ছোট বা সমান হয়, তাহলে "a is greater than 3 but less than or equal to 10" মুদ্রিত হবে।

#### ৪. শর্ট হ্যান্ড `if`
**কাজ:** এক লাইনে ছোট `if` স্টেটমেন্ট লেখা।
**কিভাবে কাজ করে:** `if` এবং তার পরবর্তী কার্যকর হওয়া কোড এক লাইনে লেখা হয়।

**উদাহরণ:**
```python
a = 10
if a > 5: print("a is greater than 5")
```
**কাজ:** যদি `a` এর মান ৫ এর চেয়ে বড় হয়, তাহলে "a is greater than 5" মুদ্রিত হবে।

#### ৫. শর্ট হ্যান্ড `if...else`
**কাজ:** এক লাইনে `if` এবং `else` স্টেটমেন্ট লেখা।
**কিভাবে কাজ করে:** `if` এবং `else` ব্লকের কোড এক লাইনে লেখা হয়।

**উদাহরণ:**
```python
a = 5
print("a is greater than 10") if a > 10 else print("a is not greater than 10")
```
**কাজ:** যদি `a` এর মান ১০ এর চেয়ে বড় না হয়, তাহলে "a is not greater than 10" মুদ্রিত হবে।

#### ৬. একাধিক `else if` (টেরনারি অপারেটর)
**কাজ:** একাধিক শর্ত পরীক্ষা করা এবং প্রথম সত্য শর্তের কোড ব্লক কার্যকর করা।
**কিভাবে কাজ করে:** একাধিক শর্ত এক লাইনে লেখা হয় এবং প্রথম সত্য শর্ত কার্যকর হয়।

**উদাহরণ:**
```python
a = 15
print("a is greater than 20") if a > 20 else print("a is 20") if a == 20 else print("a is less than 20")
```
**কাজ:** যদি `a` এর মান ২০ এর চেয়ে কম হয়, তাহলে "a is less than 20" মুদ্রিত হবে।

#### ৭. লজিক্যাল অপারেটর
**কাজ:** একাধিক শর্ত একত্রে পরীক্ষা করা।
**কিভাবে কাজ করে:** `and` বা `or` অপারেটর ব্যবহার করে একাধিক শর্ত একত্রে পরীক্ষা করা হয়।

**উদাহরণ (and অপারেটর):**
```python
a = 10
b = 20
if a > 5 and b > 15:
    print("Both conditions are true")
```
**কাজ:** যদি `a` এর মান ৫ এর চেয়ে বড় এবং `b` এর মান ১৫ এর চেয়ে বড় হয়, তাহলে "Both conditions are true" মুদ্রিত হবে।

**উদাহরণ (or অপারেটর):**
```python
a = 5
b = 20
if a > 10 or b > 15:
    print("At least one condition is true")
```
**কাজ:** যদি `a` এর মান ১০ এর চেয়ে বড় না হলেও `b` এর মান ১৫ এর চেয়ে বড় হলে "At least one condition is true" মুদ্রিত হবে।

#### ৮. নেস্টেড `if` স্টেটমেন্ট
**কাজ:** একটি `if` স্টেটমেন্টের ভিতরে আরেকটি `if` স্টেটমেন্ট রাখা।
**কিভাবে কাজ করে:** বাহিরের `if` শর্ত সত্য হলে ভিতরের `if` শর্ত পরীক্ষা করা হয় এবং তা কার্যকর হয়।

**উদাহরণ:**
```python
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
```
**কাজ:** যদি `x` এর মান ১০ এর চেয়ে বড় হয়, তাহলে "Above ten," মুদ্রিত হবে এবং যদি `x` এর মান ২০ এর চেয়ে বড় হয়, তাহলে "and also above 20!" মুদ্রিত হবে।

#### ৯. `pass` স্টেটমেন্ট
**কাজ:** `if` স্টেটমেন্ট খালি রাখা।
**কিভাবে কাজ করে:** কোন কোড লিখতে না চাইলে বা পরবর্তী সময়ে কোড লিখার জন্য `pass` ব্যবহার করা হয়।

**উদাহরণ:**
```python
a = 5
if a > 3:
    pass  # TODO: implement later
```
**কাজ:** `if` ব্লক খালি রাখতে `pass` ব্যবহার করা হয়েছে, যাতে ভবিষ্যতে কোড লেখা যায়।

#!! aro akti odaharon
পাইথনের শর্তসমূহ (if, else) নিয়ে w3schools এর লিঙ্কে যা উল্লেখ করা হয়েছে তা নিচে বিস্তারিতভাবে আলোচনা করা হলো:

### ১. `if` স্টেটমেন্ট

`if` স্টেটমেন্ট ব্যবহার করে শর্ত পরীক্ষা করা হয় এবং শর্ত সত্য হলে নির্দিষ্ট ব্লক কোড কার্যকর করা হয়।

**উদাহরণ:**
```python
a = 33
b = 200
if b > a:
    print("b is greater than a")
```
**আউটপুট:**
```
b is greater than a
```

### ২. `else` স্টেটমেন্ট

`else` স্টেটমেন্ট ব্যবহার করে একটি বিকল্প ব্লক কোড কার্যকর করা হয় যদি `if` শর্তটি মিথ্যা হয়।

**উদাহরণ:**
```python
a = 33
b = 200
if b < a:
    print("b is greater than a")
else:
    print("b is not greater than a")
```
**আউটপুট:**
```
b is not greater than a
```

### ৩. `elif` স্টেটমেন্ট

`elif` (else if) স্টেটমেন্ট ব্যবহার করে একাধিক শর্ত পরীক্ষা করা হয়। প্রথম সত্য শর্তটি পূরণ হলে তার পরের শর্তগুলি আর পরীক্ষা করা হয় না।

**উদাহরণ:**
```python
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif b == a:
    print("b is equal to a")
else:
    print("b is less than a")
```
**আউটপুট:**
```
b is equal to a
```

### ৪. শর্ট হ্যান্ড `if`

একটি ছোট `if` স্টেটমেন্ট এক লাইনে লেখা যায়।

**উদাহরণ:**
```python
a = 200
b = 33
if a > b: print("a is greater than b")
```
**আউটপুট:**
```
a is greater than b
```

### ৫. শর্ট হ্যান্ড `if...else`

`if` এবং `else` এক লাইনে লেখা যায় শর্ট হ্যান্ড ফর্মে।

**উদাহরণ:**
```python
a = 2
b = 330
print("A") if a > b else print("B")
```
**আউটপুট:**
```
B
```

### ৬. একাধিক `else if` (টেরনারি অপারেটর)

একাধিক শর্ত পরীক্ষা করা যায় এক লাইনে টেরনারি অপারেটর ব্যবহার করে।

**উদাহরণ:**
```python
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
```
**আউটপুট:**
```
=
```

### ৭. লজিক্যাল অপারেটর

`and` এবং `or` অপারেটর ব্যবহার করে একাধিক শর্ত একত্রে পরীক্ষা করা যায়।

**উদাহরণ:**

**and অপারেটর:**
```python
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
```
**আউটপুট:**
```
Both conditions are True
```

**or অপারেটর:**
```python
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")
```
**আউটপুট:**
```
At least one of the conditions is True
```

### ৮. নেস্টেড `if` স্টেটমেন্ট

`if` স্টেটমেন্টের ভিতরে `if` স্টেটমেন্ট রাখা যায়, একে নেস্টেড `if` বলা হয়।

**উদাহরণ:**
```python
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
```
**আউটপুট:**
```
Above ten,
and also above 20!
```

### ৯. `pass` স্টেটমেন্ট

`if` স্টেটমেন্ট খালি রাখা যায় না, যদি কোন কোড না লেখার প্রয়োজন হয় তবে `pass` স্টেটমেন্ট ব্যবহার করা হয়।

**উদাহরণ:**
```python
a = 33
b = 200
if b > a:
    pass
```

এই হলো w3schools এর লিঙ্কে if, else শর্ত সম্পর্কিত বিভিন্ন বিষয় এবং তাদের উদাহরণ।