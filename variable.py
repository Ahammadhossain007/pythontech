পাইথনে ভেরিয়েবলগুলি বিভিন্ন ধরনের ডেটা সংরক্ষণ করার জন্য ব্যবহৃত হয়। এখানে ভেরিয়েবল সংক্রান্ত বিস্তারিত আলোচনা করা হলো:

### 1. ভেরিয়েবল কি?

ভেরিয়েবল হল এমন একটি নাম যার মাধ্যমে আপনি মেমোরির একটি নির্দিষ্ট স্থানে সংরক্ষিত ডেটার সাথে কাজ করতে পারেন। এটি একটি কন্টেইনারের মতো যা বিভিন্ন ধরনের ডেটা সংরক্ষণ করতে পারে, যেমন নাম্বার, স্ট্রিং, লিস্ট, ডিকশনারি ইত্যাদি।

### 2. ভেরিয়েবল ডিক্লেয়ার এবং এসাইনমেন্ট

পাইথনে ভেরিয়েবল ডিক্লেয়ার করার জন্য কোনো বিশেষ কীওয়ার্ড প্রয়োজন নেই। ভেরিয়েবল ডিক্লেয়ার করার সময় আপনি তাকে একটি মান (value) এসাইন করতে পারেন।

```python
# Variable declaration and assignment
x = 10
name = "Alice"
is_valid = True
```

### 3. ভেরিয়েবলের নামকরণের নিয়ম

ভেরিয়েবলের নামকরণের কিছু নির্দিষ্ট নিয়ম আছে:

- ভেরিয়েবলের নাম অবশ্যই একটি অক্ষর বা আন্ডারস্কোর (_) দিয়ে শুরু হতে হবে।
- নামের মধ্যে শুধুমাত্র অক্ষর (a-z, A-Z), সংখ্যা (0-9), এবং আন্ডারস্কোর (_) থাকতে পারে।
- নাম অবশ্যই কেস সেনসিটিভ (case-sensitive) হবে, অর্থাৎ `age` এবং `Age` দুটি আলাদা ভেরিয়েবল।
- পাইথনের কীওয়ার্ড (যেমন, `if`, `else`, `while` ইত্যাদি) ভেরিয়েবল নাম হিসেবে ব্যবহার করা যাবে না।

```python
# Valid variable names
age = 25
_age = 30
age1 = 35

# Invalid variable names
1age = 25  # শুরুতে সংখ্যা থাকা যাবে না
age@ = 30  # বিশেষ চিহ্ন থাকা যাবে না
```

### 4. বিভিন্ন ধরনের ভেরিয়েবল

পাইথনে ভেরিয়েবলে বিভিন্ন ধরনের ডেটা রাখা যায়। নিচে কিছু উদাহরণ দেয়া হলো:

```python
# Integer
x = 10

# Float
pi = 3.14159

# String
name = "Alice"

# Boolean
is_valid = True

# List
numbers = [1, 2, 3, 4, 5]

# Tuple
coordinates = (10, 20)

# Dictionary
person = {"name": "Alice", "age": 25}

# Set
unique_numbers = {1, 2, 3, 4, 5}
```

### 5. ভেরিয়েবল নিয়ে কাজ করা

#### 5.1 ভেরিয়েবলের মান পরিবর্তন করা
ভেরিয়েবলের মান সহজেই পরিবর্তন করা যায়।

```python
x = 10
print(x)  # Output: 10

x = 20
print(x)  # Output: 20
```

#### 5.2 একাধিক ভেরিয়েবলকে একসাথে মান দেওয়া
একই লাইনে একাধিক ভেরিয়েবলকে মান দেয়া সম্ভব।

```python
a, b, c = 5, 10, 15
print(a, b, c)  # Output: 5 10 15
```

#### 5.3 ভেরিয়েবলের ধরন চেক করা
`type()` ফাংশন ব্যবহার করে ভেরিয়েবলের ধরন চেক করা যায়।

```python
x = 10
print(type(x))  # Output: <class 'int'>

name = "Alice"
print(type(name))  # Output: <class 'str'>
```

### 6. উদাহরণ সহ ভেরিয়েবল ব্যবহার

#### 6.1 স্ট্রিং কনক্যাটেনেশন
```python
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe
```

#### 6.2 সংখ্যার উপর গণনা করা
```python
a = 10
b = 20
sum = a + b
print(sum)  # Output: 30
```

#### 6.3 লিস্টে ভেরিয়েবল ব্যবহার
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple

fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
```

#### 6.4 ডিকশনারিতে ভেরিয়েবল ব্যবহার
```python
person = {"name": "Alice", "age": 25}
print(person["name"])  # Output: Alice

person["city"] = "New York"
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
```

### 7. একটি উদাহরণ: পণ্য সংক্রান্ত তথ্য টেমপ্লেট তৈরি

চলুন, একটি উদাহরণ দিয়ে দেখাই কিভাবে ভেরিয়েবল ব্যবহার করে পণ্য সংক্রান্ত তথ্যের টেমপ্লেট তৈরি করা যায় এবং USD কে BDT তে রূপান্তর করা যায়।

```python
# Example dictionary data
product = {
    "name": "Xiaomi Note 5",
    "country": "China",
    "price_usd": 300
}

# Conversion rate from USD to BDT
usd_to_bdt_conversion_rate = 103.25

# Convert price to BDT
price_bdt = product["price_usd"] * usd_to_bdt_conversion_rate

# Create template
template = (f"{product['name']} is made in {product['country']}. "
            f"The price is {product['price_usd']} USD which is almost equal to {price_bdt:.2f} BDT.")

# Print the template
print(template)
```

**Output:**
```
Xiaomi Note 5 is made in China. The price is 300 USD which is almost equal to 30975.00 BDT.
```

এই কোডটি একটি ডিকশনারি থেকে পণ্যের তথ্য নিয়ে একটি টেমপ্লেট তৈরি করে এবং USD থেকে BDT তে রূপান্তর করে প্রিন্ট করে। এতে ভেরিয়েবল ব্যবহার, স্ট্রিং ইন্টারপোলেশন, এবং গণনার বিভিন্ন পদ্ধতি দেখানো হয়েছে।