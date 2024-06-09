### পাইথনে ডিকশনারি: বিস্তারিত আলোচনা

পাইথনে ডিকশনারি একটি ডেটা স্ট্রাকচার যা কী-ভ্যালু জোড়া আকারে ডেটা সংরক্ষণ করে।
এটি দ্রুত অনুসন্ধান এবং ম্যানিপুলেশনের জন্য ব্যবহার করা হয়।

#### ১. ডিকশনারি কী?

ডিকশনারি হল কী-ভ্যালু জোড়া ভিত্তিক একটি সংগ্রহ, যেখানে প্রতিটি কী একটি ইউনিক ভ্যালু নির্দেশ করে।
ডিকশনারিগুলি কার্লি ব্র্যাকেট `{}` এর ভিতরে কী-ভ্যালু জোড়া দ্বারা সংজ্ঞায়িত হয়।

**উদাহরণ:**
```python
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
```

#### ২. ডিকশনারি আইটেমে অ্যাক্সেস করা

ডিকশনারির আইটেমগুলি কী ব্যবহার করে অ্যাক্সেস করা যায়।

**উদাহরণ:**
```python
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(my_dict["name"])  # আউটপুট: Alice
```

**get() মেথড**: এই মেথডটি ব্যবহার করে ডিফল্ট ভ্যালু সহ আইটেম অ্যাক্সেস করা যায়।
```python
print(my_dict.get("age"))  # আউটপুট: 25
print(my_dict.get("country", "USA"))  # আউটপুট: USA (কী না থাকলে ডিফল্ট ভ্যালু রিটার্ন করবে)
```

#### ৩. ডিকশনারি আইটেম পরিবর্তন করা

ডিকশনারির আইটেমগুলি কী ব্যবহার করে পরিবর্তন করা যায়।

**উদাহরণ:**
```python
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
my_dict["age"] = 30
print(my_dict)  # আউটপুট: {'name': 'Alice', 'age': 30, 'city': 'New York'}
```

#### ৪. ডিকশনারিতে আইটেম যোগ করা

নতুন কী-ভ্যালু জোড়া অ্যাড করার মাধ্যমে ডিকশনারিতে আইটেম যোগ করা যায়।

**উদাহরণ:**
```python
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
my_dict["country"] = "USA"
print(my_dict)  # আউটপুট: {'name': 'Alice', 'age': 25, 'city': 'New York', 'country': 'USA'}
```

#### ৫. ডিকশনারি থেকে আইটেম সরানো

**pop() মেথড**: নির্দিষ্ট কী এর আইটেম সরায় এবং তার ভ্যালু রিটার্ন করে।

**উদাহরণ:**
```python
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
age = my_dict.pop("age")
print(age)  # আউটপুট: 25
print(my_dict)  # আউটপুট: {'name': 'Alice', 'city': 'New York'}
```

**del স্টেটমেন্ট**: নির্দিষ্ট কী এর আইটেম সরায়।

**উদাহরণ:**
```python
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
del my_dict["city"]
print(my_dict)  # আউটপুট: {'name': 'Alice', 'age': 25}
```

**clear() মেথড**: সমস্ত আইটেম সরিয়ে ফেলে।

**উদাহরণ:**
```python
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
my_dict.clear()
print(my_dict)  # আউটপুট: {}
```

#### ৬. ডিকশনারিতে লুপ করা

ডিকশনারির উপর বিভিন্নভাবে লুপ করা যায়।

**কী এর উপর লুপ করা**:
```python
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
for key in my_dict:
    print(key)
```
**আউটপুট:**
```
name
age
city
```

**কী ও ভ্যালু এর উপর লুপ করা**:
```python
for key, value in my_dict.items():
    print(f"{key}: {value}")
```
**আউটপুট:**
```
name: Alice
age: 25
city: New York
```

#### ৭. ডিকশনারি কপি করা

**copy() মেথড**: একটি নতুন কপি তৈরি করে।

**উদাহরণ:**
```python
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
new_dict = my_dict.copy()
print(new_dict)  # আউটপুট: {'name': 'Alice', 'age': 25, 'city': 'New York'}
```

**dict() কনস্ট্রাক্টর**: কপি তৈরিতে ব্যবহৃত হয়।

**উদাহরণ:**
```python
new_dict = dict(my_dict)
print(new_dict)  # আউটপুট: {'name': 'Alice', 'age': 25, 'city': 'New York'}
```

#### ৮. নেস্টেড ডিকশনারি

ডিকশনারি ভিতরে ডিকশনারি রাখা যেতে পারে।

**উদাহরণ:**
```python
my_family = {
    "child1": {
        "name": "Emily",
        "year": 2004
    },
    "child2": {
        "name": "John",
        "year": 2006
    },
    "child3": {
        "name": "Anna",
        "year": 2008
    }
}
```

#### ৯. ডিকশনারি মেথড

ডিকশনারির উপর বিভিন্ন মেথড ব্যবহার করা যায়। কিছু সাধারণ মেথড নিচে দেওয়া হলো:

- **keys()**: সমস্ত কী রিটার্ন করে।
- **values()**: সমস্ত ভ্যালু রিটার্ন করে।
- **items()**: সমস্ত কী-ভ্যালু জোড়া রিটার্ন করে।
- **update()**: ডিকশনারি আপডেট করে।

**উদাহরণ:**
```python
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

keys = my_dict.keys()
print(keys)  # আউটপুট: dict_keys(['name', 'age', 'city'])

values = my_dict.values()
print(values)  # আউটপুট: dict_values(['Alice', 25, 'New York'])

items = my_dict.items()
print(items)  # আউটপুট: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

my_dict.update({"age": 30})
print(my_dict)  # আউটপুট: {'name': 'Alice', 'age': 30, 'city': 'New York'}
```

#### ১০. ডিকশনারি এক্সারসাইজ

ডিকশনারির উপর প্র্যাকটিস এবং এক্সারসাইজ করার জন্য কিছু উদাহরণ নিচে দেওয়া হলো:

**Exercise 1**: একটি ডিকশনারি তৈরি করুন এবং একটি কী-ভ্যালু জোড়া যোগ করুন।
```python
my_dict = {}
my_dict["name"] = "Alice"
print(my_dict)  # আউটপুট: {'name': 'Alice'}
```

**Exercise 2**: একটি ডিকশনারি থেকে একটি কী-ভ্যালু জোড়া সরান।
```python
my_dict = {"name": "Alice", "age": 25}
my_dict.pop("age")
print(my_dict)  # আউটপুট: {'name': 'Alice'}
```

**Exercise 3**: একটি ডিকশনারি থেকে সমস্ত কী এবং ভ্যালু প্রিন্ট করুন।
```python
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in my_dict.items():
    print(f"{key}: {value}")
```
**আউটপুট:**
```
name: Alice
age: 25
city: New York
```

### সারসংক্ষেপ

- **ডিকশনারি**: কী-ভ্যালু জোড়া ভিত্তিক একটি সংগ্রহ।
- **অ্যাক্সেস করা**: কী ব্যবহার করে।
- **পরিবর্তন করা**: কী এর মাধ্যমে ভ্যালু পরিবর্তন করা।
- **আইটেম যোগ করা**: নতুন কী-ভ্যালু জোড়া যোগ করা।
- **আইটেম সরানো**: `pop()`, `del`, এবং `clear()` মেথড দ্বারা।
- **লুপ করা**: কী, ভ্যালু, এবং কী-ভ্যালু জোড়ার উপর।
- **

কপি করা**: `copy()` মেথড এবং `dict()` কনস্ট্রাক্টর দ্বারা।
- **নেস্টেড ডিকশনারি**: ডিকশনারি ভিতরে ডিকশনারি।
- **মেথডগুলি**: `keys()`, `values()`, `items()`, `update()` ইত্যাদি।

এই ধারণাগুলি আপনাকে পাইথনের ডিকশনারি ব্যবহার করে ডেটা ম্যানিপুলেট করতে সাহায্য করবে।



#  !!!!  aro akti odaharon

### পাইথনে ডিকশনারি: উদাহরণ সহ বিস্তারিত আলোচনা

ডিকশনারি সম্পর্কে প্রতিটি বিষয় ব্যাখ্যা করা হয়েছে এবং প্রতিটি বিষয়ে উদাহরণ দেওয়া হয়েছে।

#### ১. ডিকশনারি কী?

ডিকশনারি হল কী-ভ্যালু জোড়া ভিত্তিক একটি সংগ্রহ, যেখানে প্রতিটি কী একটি ইউনিক ভ্যালু নির্দেশ করে।
ডিকশনারিগুলি কার্লি ব্র্যাকেট `{}` এর মধ্যে কী-ভ্যালু জোড়া দ্বারা সংজ্ঞায়িত হয়।

**উদাহরণ:**
```python
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
```

#### ২. ডিকশনারি আইটেমে অ্যাক্সেস করা

ডিকশনারির আইটেমগুলি কী ব্যবহার করে অ্যাক্সেস করা যায়।

**উদাহরণ:**
```python
print(my_dict["name"])  # আউটপুট: Alice
```

**get() মেথড**: এই মেথডটি ব্যবহার করে ডিফল্ট ভ্যালু সহ আইটেম অ্যাক্সেস করা যায়।
```python
print(my_dict.get("age"))  # আউটপুট: 25
print(my_dict.get("country", "USA"))  # আউটপুট: USA (কী না থাকলে ডিফল্ট ভ্যালু রিটার্ন করবে)
```

#### ৩. ডিকশনারি আইটেম পরিবর্তন করা

ডিকশনারির আইটেমগুলি কী ব্যবহার করে পরিবর্তন করা যায়।

**উদাহরণ:**
```python
my_dict["age"] = 30
print(my_dict)  # আউটপুট: {'name': 'Alice', 'age': 30, 'city': 'New York'}
```

#### ৪. ডিকশনারিতে আইটেম যোগ করা

নতুন কী-ভ্যালু জোড়া অ্যাড করার মাধ্যমে ডিকশনারিতে আইটেম যোগ করা যায়।

**উদাহরণ:**
```python
my_dict["country"] = "USA"
print(my_dict)  # আউটপুট: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}
```

#### ৫. ডিকশনারি থেকে আইটেম সরানো

**pop() মেথড**: নির্দিষ্ট কী এর আইটেম সরায় এবং তার ভ্যালু রিটার্ন করে।

**উদাহরণ:**
```python
age = my_dict.pop("age")
print(age)  # আউটপুট: 30
print(my_dict)  # আউটপুট: {'name': 'Alice', 'city': 'New York', 'country': 'USA'}
```

**del স্টেটমেন্ট**: নির্দিষ্ট কী এর আইটেম সরায়।

**উদাহরণ:**
```python
del my_dict["city"]
print(my_dict)  # আউটপুট: {'name': 'Alice', 'country': 'USA'}
```

**clear() মেথড**: সমস্ত আইটেম সরিয়ে ফেলে।

**উদাহরণ:**
```python
my_dict.clear()
print(my_dict)  # আউটপুট: {}
```

#### ৬. ডিকশনারিতে লুপ করা

ডিকশনারির উপর বিভিন্নভাবে লুপ করা যায়।

**কী এর উপর লুপ করা**:
```python
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
for key in my_dict:
    print(key)
```
**আউটপুট:**
```
name
age
city
```

**কী ও ভ্যালু এর উপর লুপ করা**:
```python
for key, value in my_dict.items():
    print(f"{key}: {value}")
```
**আউটপুট:**
```
name: Alice
age: 25
city: New York
```

#### ৭. ডিকশনারি কপি করা

**copy() মেথড**: একটি নতুন কপি তৈরি করে।

**উদাহরণ:**
```python
new_dict = my_dict.copy()
print(new_dict)  # আউটপুট: {'name': 'Alice', 'age': 25, 'city': 'New York'}
```

**dict() কনস্ট্রাক্টর**: কপি তৈরিতে ব্যবহৃত হয়।

**উদাহরণ:**
```python
new_dict = dict(my_dict)
print(new_dict)  # আউটপুট: {'name': 'Alice', 'age': 25, 'city': 'New York'}
```

#### ৮. নেস্টেড ডিকশনারি

ডিকশনারি ভিতরে ডিকশনারি রাখা যেতে পারে।

**উদাহরণ:**
```python
my_family = {
    "child1": {
        "name": "Emily",
        "year": 2004
    },
    "child2": {
        "name": "John",
        "year": 2006
    },
    "child3": {
        "name": "Anna",
        "year": 2008
    }
}
```

#### ৯. ডিকশনারি মেথড

ডিকশনারির উপর বিভিন্ন মেথড ব্যবহার করা যায়। কিছু সাধারণ মেথড নিচে দেওয়া হলো:

- **keys()**: সমস্ত কী রিটার্ন করে।
- **values()**: সমস্ত ভ্যালু রিটার্ন করে।
- **items()**: সমস্ত কী-ভ্যালু জোড়া রিটার্ন করে।
- **update()**: ডিকশনারি আপডেট করে।

**উদাহরণ:**
```python
keys = my_dict.keys()
print(keys)  # আউটপুট: dict_keys(['name', 'age', 'city'])

values = my_dict.values()
print(values)  # আউটপুট: dict_values(['Alice', 25, 'New York'])

items = my_dict.items()
print(items)  # আউটপুট: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

my_dict.update({"age": 30})
print(my_dict)  # আউটপুট: {'name': 'Alice', 'age': 30, 'city': 'New York'}
```

#### ১০. ডিকশনারি এক্সারসাইজ

ডিকশনারির উপর প্র্যাকটিস এবং এক্সারসাইজ করার জন্য কিছু উদাহরণ নিচে দেওয়া হলো:

**Exercise 1**: একটি ডিকশনারি তৈরি করুন এবং একটি কী-ভ্যালু জোড়া যোগ করুন।
```python
my_dict = {}
my_dict["name"] = "Alice"
print(my_dict)  # আউটপুট: {'name': 'Alice'}
```

**Exercise 2**: একটি ডিকশনারি থেকে একটি কী-ভ্যালু জোড়া সরান।
```python
my_dict = {"name": "Alice", "age": 25}
my_dict.pop("age")
print(my_dict)  # আউটপুট: {'name': 'Alice'}
```

**Exercise 3**: একটি ডিকশনারি থেকে সমস্ত কী এবং ভ্যালু প্রিন্ট করুন।
```python
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in my_dict.items():
    print(f"{key}: {value}")
```
**আউটপুট:**
```
name: Alice
age: 25
city: New York
```

### সারসংক্ষেপ

- **ডিকশনারি**: কী-ভ্যালু জোড়া ভিত্তিক একটি সংগ্রহ।
- **অ্যাক্সেস করা**: কী ব্যবহার করে।
- **পরিবর্তন করা**: কী এর মাধ্যমে ভ্যালু পরিবর্তন করা।
- **আইটেম যোগ করা**: নতুন কী-ভ্যালু জোড়া যোগ করা।
- **আইটেম সরানো**: `pop()`, `del`, এবং `clear()` মেথড দ্বারা।
- **লুপ করা**: কী, ভ্যালু, এবং কী-ভ্যালু জোড়ার উপর।
- **কপি করা**: `copy()` মেথড এবং `dict()` কনস্ট্রাক্টর দ্বারা।
- **নেস্টেড ডিকশনারি**: ডিকশনারি ভিতরে ডিকশনারি।
- **মেথডগুলি**: `keys()`, `values()`, `items()`, `update()` ইত্যাদি।

এই ধারণাগুলি আপনাকে পাইথনের ডিকশনারি ব্যবহার করে ডেটা ম্যানিপুলেট করতে সাহায্য করবে।


### !!! aro akti odahaon

### পাইথনে ডিকশনারি

পাইথনে ডিকশনারি কী-ভ্যালু জোড়া আকারে ডেটা সংরক্ষণ করে। নিচে বিভিন্ন ডিকশনারি সম্পর্কিত কার্যক্রম ও উদাহরণ দেওয়া হলো:

#### ১. ডিকশনারি কী?

ডিকশনারি একটি অসংরক্ষিত, পরিবর্তনযোগ্য এবং ইনডেক্সড সংগ্রহ। এটি কার্লি ব্র্যাকেট `{}` এর মধ্যে লেখা হয়।

**উদাহরণ:**
```python
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
```

#### ২. ডিকশনারি আইটেম অ্যাক্সেস করা

ডিকশনারির আইটেমগুলি কী নাম ব্যবহার করে অ্যাক্সেস করা যায়।

**উদাহরণ:**
```python
x = thisdict["model"]
print(x)  # আউটপুট: Mustang
```

**get() মেথড ব্যবহার:**
```python
x = thisdict.get("model")
print(x)  # আউটপুট: Mustang
```

#### ৩. ডিকশনারি আইটেম পরিবর্তন করা

কী নাম ব্যবহার করে নির্দিষ্ট আইটেমের ভ্যালু পরিবর্তন করা যায়।

**উদাহরণ:**
```python
thisdict["year"] = 2018
print(thisdict)
```

#### ৪. ডিকশনারিতে আইটেম যোগ করা

নতুন ইনডেক্স কী এবং ভ্যালু অ্যাসাইন করার মাধ্যমে ডিকশনারিতে আইটেম যোগ করা যায়।

**উদাহরণ:**
```python
thisdict["color"] = "red"
print(thisdict)
```

#### ৫. ডিকশনারি থেকে আইটেম সরানো

ডিকশনারি থেকে আইটেম সরানোর জন্য বিভিন্ন মেথড রয়েছে:

**pop() মেথড:**
```python
thisdict.pop("model")
print(thisdict)
```

**del স্টেটমেন্ট:**
```python
del thisdict["year"]
print(thisdict)
```

**clear() মেথড:**
```python
thisdict.clear()
print(thisdict)  # আউটপুট: {}
```

#### ৬. ডিকশনারিতে লুপ করা

ডিকশনারির উপর `for` লুপ ব্যবহার করে লুপ করা যায়।

**কী এর উপর লুপ করা:**
```python
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x)
```

**ভ্যালু এর উপর লুপ করা:**
```python
for x in thisdict:
    print(thisdict[x])
```

**values() মেথড ব্যবহার:**
```python
for x in thisdict.values():
    print(x)
```

**keys() মেথড ব্যবহার:**
```python
for x in thisdict.keys():
    print(x)
```

**items() মেথড ব্যবহার:**
```python
for x, y in thisdict.items():
    print(x, y)
```

#### ৭. ডিকশনারি কপি করা

ডিকশনারি কপি করার জন্য `copy()` মেথড ব্যবহার করা হয়।

**উদাহরণ:**
```python
mydict = thisdict.copy()
print(mydict)
```

**dict() কনস্ট্রাক্টর ব্যবহার:**
```python
mydict = dict(thisdict)
print(mydict)
```

#### ৮. নেস্টেড ডিকশনারি

ডিকশনারির ভিতরে ডিকশনারি রাখা যেতে পারে।

**উদাহরণ:**
```python
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myfamily)
```

#### ৯. ডিকশনারি মেথড

ডিকশনারির উপর বিভিন্ন মেথড ব্যবহার করা যায়। কিছু সাধারণ মেথড নিচে দেওয়া হলো:

- **clear()**: সমস্ত আইটেম সরিয়ে ফেলে।
- **copy()**: ডিকশনারির একটি কপি রিটার্ন করে।
- **fromkeys()**: নির্দিষ্ট কী এবং ভ্যালু সহ একটি ডিকশনারি রিটার্ন করে।
- **get()**: নির্দিষ্ট কী এর ভ্যালু রিটার্ন করে।
- **items()**: কী-ভ্যালু জোড়ার একটি তালিকা রিটার্ন করে।
- **keys()**: ডিকশনারির কী গুলির একটি তালিকা রিটার্ন করে।
- **pop()**: নির্দিষ্ট কী এর আইটেম সরায়।
- **popitem()**: সর্বশেষ যোগ করা আইটেম সরায়।
- **setdefault()**: নির্দিষ্ট কী এর ভ্যালু রিটার্ন করে; যদি কী না থাকে তাহলে কী যোগ করে।
- **update()**: নির্দিষ্ট কী-ভ্যালু জোড়া দিয়ে ডিকশনারি আপডেট করে।
- **values()**: ডিকশনারির সমস্ত ভ্যালু রিটার্ন করে।

**উদাহরণ:**
```python
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# clear()
thisdict.clear()
print(thisdict)  # আউটপুট: {}

# copy()
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.copy()
print(x)  # আউটপুট: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# fromkeys()
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)  # আউটপুট: {'key1': 0, 'key2': 0, 'key3': 0}

# get()
x = thisdict.get('key2')
print(x)  # আউটপুট: 0

# items()
x = thisdict.items()
print(x)  # আউটপুট: dict_items([('key1', 0), ('key2', 0), ('key3', 0)])

# keys()
x = thisdict.keys()
print(x)  # আউটপুট: dict_keys(['key1', 'key2', 'key3'])

# pop()
thisdict.pop('key2')
print(thisdict)  # আউটপুট: {'key1': 0, 'key3': 0}

# popitem()
thisdict.popitem()
print(thisdict)  # আউটপুট: {'key1': 0}

# setdefault()
x = thisdict.setdefault('key4', 'default value')
print(x)  # আউটপুট: default value
print(thisdict)  # আউটপুট: {'key1': 0, 'key4': 'default value'}

# update()
thisdict.update({'key1': 'updated value'})
print(thisdict)  # আউটপুট: {'key1': 'updated value', 'key4': 'default value'}

# values()
x = thisdict.values()
print(x)  # আউটপুট: dict_values(['updated value', 'default value'])

# Loop through items()
for x, y in thisdict.items():
    print(x, y)
```

#### ১০. ডিকশনারি এক্সারসাইজ

**Exercise 1:** একটি ডিকশনারি তৈরি করুন এবং কী-ভ্যালু জোড়া যোগ করুন।
```python
ex_dict = {}
ex_dict["name"] = "Alice"
print(ex_dict)  # আউটপুট: {'name': 'Alice'}
```

**Exercise 2:** একটি ডিকশনারি থেকে একটি কী-ভ্যালু জোড়া সরান।
```python
ex_dict = {"name": "Alice", "age": 25}
ex_dict.pop("name")
print(ex_dict)  # আউটপুট: {'age': 25}
```

**Exercise 3:** একটি ডিকশনারির সমস্ত কী-ভ্যালু জোড়া প্রিন্ট করুন।
```python
ex_dict = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in ex_dict.items():
    print(f"{key}: {value}")
```
**আউটপুট:**
```
name: Alice
age: 25
city: New York
```

**Exercise 4:** ডিকশনারিতে একটি কী বিদ্যমান কিনা তা চেক করুন।
```python
if "name" in ex_dict:
    print("Name exists in the dictionary")
```

**Exercise 5:** একটি ডিকশনারি থেকে একটি ভ্যালু পান।
```python
age = ex_dict.get("age")
print(f"Age: {age}")  # আউটপুট: Age: 25
```

**Exercise 6:** একটি ডিকশনারির কপি তৈরি

 করুন।
```python
copy_dict = ex_dict.copy()
print(copy_dict)  # আউটপুট: {'name': 'Alice', 'age': 25, 'city': 'New York'}
```

**Exercise 7:** নেস্টেড ডিকশনারির উদাহরণ।
```python
nested_dict = {
    "child1": {
        "name": "Emily",
        "year": 2004
    },
    "child2": {
        "name": "John",
        "year": 2006
    }
}
print(nested_dict)
```
**আউটপুট:**
```
{
    "child1": {"name": "Emily", "year": 2004},
    "child2": {"name": "John", "year": 2006}
}
```