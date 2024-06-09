                                   CLASS-----13.2



1.
istitle():

s = "This Is A Title"
print(s.istitle())  # True

t = "This is not a title"
print(t.istitle())  # False

এখানে, s স্ট্রিংটির প্রতিটি শব্দের প্রথম অক্ষর বড় হাতের, তাই True রিটার্ন করে। t স্ট্রিংটি সেই নিয়ম মেনে চলে না
তাই False রিটার্ন করে।

2.
isupper():

s = "THIS IS UPPERCASE"
print(s.isupper())  # True

t = "This Is Not Uppercase"
print(t.isupper())  # False

isupper() method টি চেক করে যে সমস্ত অক্ষর বড় হাতের কিনা।

3.
islower():

s = "this is lowercase"
print(s.islower())  # True

t = "This Is Not Lowercase"
print(t.islower())  # False

islower() method টি চেক করে যে সমস্ত অক্ষর ছোট হাতের কিনা।

4.
isspace():

s = "   "
print(s.isspace())  # True

t = "This is not space"
print(t.isspace())  # False

isspace() method টি চেক করে যে স্ট্রিংটি শুধুমাত্র স্পেস অক্ষর দিয়ে গঠিত কিনা।

5.
isidentifier():

s = "variable1"
print(s.isidentifier())  # True

t = "1variable"
print(t.isidentifier())  # False

isidentifier() method টি চেক করে যে স্ট্রিংটি একটি বৈধ পাইথন আইডেন্টিফায়ার কিনা।

6.
encode():

s = "পাইথন প্রোগ্রামিং"
encoded_s = s.encode("utf-8")
print(encoded_s)  # b'\xe0\xa6\xaa\xe0\xa6\xbe\xe0\xa6\x87\xe0\xa6\xa5\xe0\xa6\xa8 \xe0\xa6\xaa\xe0\xa7\x8d\xe0\xa6\xb0\xe0\xa7\x8b\xe0\xa6\x97\xe0\xa7\x8d\xe0\xa6\xb0\xe0\xa6\xbe\xe0\xa6\xae\xe0\xa6\xbf\xe0\xa6\x82'

encode() method টি স্ট্রিংটিকে নির্দিষ্ট এনকোডিং ব্যবহার করে এনকোড করে। এখানে, s স্ট্রিংটিকে "utf-8" এনকোডিং ব্যবহার করে এনকোড করা হয়েছে।

                 CLASS------13.3

অবশ্যই, আমি পাইথনের স্ট্রিং methods isdigit, isalpha, isalnum, isascii, isprintable, isdecimal, এবং isnumeric সম্পর্কে বিস্তারিত ব্যাখ্যা এবং উদাহরণ সহ বলছি:

7.
isdigit():
•  এই method টি চেক করে যে স্ট্রিংটি শুধুমাত্র ডিজিট দিয়ে গঠিত কিনা।

s = "12345"
print(s.isdigit())  # True

t = "12345a"
print(t.isdigit())  # False

8.
isalpha():
•  এই method টি চেক করে যে স্ট্রিংটি শুধুমাত্র অক্ষর দিয়ে গঠিত কিনা।

s = "abcde"
print(s.isalpha())  # True

t = "abcde1"
print(t.isalpha())  # False

9.
isalnum():
•  এই method টি চেক করে যে স্ট্রিংটি অক্ষর এবং ডিজিট উভয় দিয়ে গঠিত কিনা।

s = "abc123"
print(s.isalnum())  # True

t = "abc123!"
print(t.isalnum())  # False

10.
isascii():
•  এই method টি চেক করে যে স্ট্রিংটি ASCII অক্ষর দিয়ে গঠিত কিনা।

s = "abc123"
print(s.isascii())  # True

t = "abc123£"
print(t.isascii())  # False

11.
isprintable():
•  এই method টি চেক করে যে স্ট্রিংটি প্রিন্ট করা যায় কিনা।

s = "Printable String"
print(s.isprintable())  # True

t = "Non\x00Printable"
print(t.isprintable())  # False

12.
isdecimal():
•  এই method টি চেক করে যে স্ট্রিংটি শুধুমাত্র দশমিক সংখ্যা দিয়ে গঠিত কিনা।

s = "12345"
print(s.isdecimal())  # True

t = "123.45"
print(t.isdecimal())  # False

13.
isnumeric():
•  এই method টি চেক করে যে স্ট্রিংটি সংখ্যা দিয়ে গঠিত কিনা, যা ইউনিকোড সংখ্যা অন্তর্ভুক্ত করে।

s = "12345"
print(s.isnumeric())  # True

t = "½"
print(t.isnumeric())  # True

                    Class-----13.4

পাইথনের count() method এবং len() function দুটি খুবই উপকারী এবং প্রায়ই ব্যবহৃত হয়। এগুলি স্ট্রিং, লিস্ট,
এবং অন্যান্য সিকোয়েন্স টাইপের সাথে কাজ করে। নিচে প্রতিটির ব্যবহার এবং উদাহরণ দেওয়া হল:

1.
count() Method:
•  count() method টি একটি সিকোয়েন্সের মধ্যে নির্দিষ্ট একটি আইটেম কতবার আছে তা গণনা করে।

# একটি লিস্টে 'a' কতবার আছে তা গণনা করা
letters = ['a', 'b', 'a', 'c', 'a']
a_count = letters.count('a')
print(a_count)  # Output: 3

# Using count()
sentence = "the quick brown fox jumps over the lazy dog"
e_count = sentence.count('e')
print(e_count)  # Output: 3

# Using len()
length_sentence = len(sentence)
print(length_sentence)  # Output: 43

###  akti niddisto songer por kato golo a ase ta dekher janno, (start) er jaigai kato theke count
suro hobe and (end) khotai ses hobe (index) number dite hobe
sentence = "the quick brown fox jumps over the lazy dog"
e_count = 'e'
print(sentence.count(e_count, 3, 43))  # Output: 2


2.
len() Function:
•  len() function টি একটি সিকোয়েন্সের মধ্যে মোট আইটেমের সংখ্যা ফেরত দেয়।

# একটি লিস্টে মোট আইটেমের সংখ্যা গণনা করা
letters = ['a', 'b', 'a', 'c', 'a']
total_items = len(letters)
print(total_items)  # Output: 5

# Example with String:
 text = "hello world"
length_text = len(text)
 print(length_text)  # Output: 11



এই দুটি ফাংশনের মূল পার্থক্য হল, count() একটি নির্দিষ্ট আইটেমের ঘটনা গণনা করে,
অন্যদিকে len() সমগ্র সিকোয়েন্সের দৈর্ঘ্য বা মোট আইটেমের সংখ্যা ফেরত দেয়।


                                   CLASS-----13.5
1.
startswith() Method:
•  এই method টি চেক করে যে স্ট্রিংটি নির্দিষ্ট একটি সাবস্ট্রিং দিয়ে শুরু হয়েছে কিনা।

text = "Python programming"
print(text.startswith("Python"))  # Output: True

2.
endswith() Method:
•  এই method টি চেক করে যে স্ট্রিংটি নির্দিষ্ট একটি সাবস্ট্রিং দিয়ে শেষ হয়েছে কিনা।

text = "Python programming"
print(text.endswith("programming"))  # Output: True

3.
index() Method:
•  এই method টি স্ট্রিংয়ের মধ্যে নির্দিষ্ট একটি সাবস্ট্রিং প্রথম কোথায় আছে তা বের করে। যদি সাবস্ট্রিংটি না পাওয়া যায়,
তাহলে একটি ValueError থ্রো করে।

text = "Python programming"
print(text.index("programming"))  # Output: 7

4.
rindex() Method:
•  এই method টি স্ট্রিংয়ের মধ্যে নির্দিষ্ট একটি সাবস্ট্রিং শেষ কোথায় আছে তা বের করে।
যদি সাবস্ট্রিংটি না পাওয়া যায়, তাহলে একটি ValueError থ্রো করে।

text = "Python programming, Python scripting"
print(text.rindex("Python"))  # Output: 22


### aro bistarito vabe alochona

1.
startswith() Method:
•  এই method টি স্ট্রিংয়ের শুরুতে নির্দিষ্ট একটি সাবস্ট্রিং আছে কিনা তা চেক করে।
এটি বুলিয়ান (True বা False) মান ফেরত দেয়।

text = "Hello, world!"
print(text.startswith("Hello"))  # Output: True
print(text.startswith("world"))  # Output: False

2.
endswith() Method:
•  এই method টি স্ট্রিংয়ের শেষে নির্দিষ্ট একটি সাবস্ট্রিং আছে কিনা তা চেক করে। এটি বুলিয়ান মান ফেরত দেয়।

text = "Hello, world!"
print(text.endswith("!"))  # Output: True
print(text.endswith("Hello"))  # Output: False

3.
index() Method:
•  এই method টি স্ট্রিংয়ের মধ্যে নির্দিষ্ট একটি সাবস্ট্রিং প্রথম কোথায় আছে তা বের করে।
যদি সাবস্ট্রিংটি না পাওয়া যায়, তাহলে একটি ValueError থ্রো করে।

text = "Hello, world!"
print(text.index("world"))  # Output: 7
# print(text.index("Python"))  # ValueError: substring not found

4.
rindex() Method:
•  এই method টি স্ট্রিংয়ের মধ্যে নির্দিষ্ট একটি সাবস্ট্রিং শেষ কোথায় আছে তা বের করে।
এটি index() method এর মতোই কাজ করে, তবে শেষ থেকে শুরু করে খোঁজে। যদি সাবস্ট্রিংটি না পাওয়া যায়,
তাহলে একটি ValueError থ্রো করে।

text = "Hello, world! Welcome to the world of Python."
print(text.rindex("world"))  # Output: 25
# print(text.rindex("Python"))  # Output: 38

                     CLASS----13.6


1.
find() Method:
•  find() method টি একটি স্ট্রিংয়ের মধ্যে নির্দিষ্ট একটি সাবস্ট্রিং প্রথম কোথায় আছে তা বের করে।
এটি স্ট্রিংয়ের শুরু থেকে খোঁজা শুরু করে এবং সাবস্ট্রিংটির প্রথম অবস্থানের ইনডেক্স ফেরত দেয়। যদি সাবস্ট্রিংটি না পাওয়া যায়,
তাহলে -1 রিটার্ন করে।

sentence = "পাইথন একটি জনপ্রিয় প্রোগ্রামিং ভাষা।"
index = sentence.find("জনপ্রিয়")
print(index)  # Output: 7

2.
rfind() Method:
•  rfind() method টি find() method এর মতোই কাজ করে, তবে এটি স্ট্রিংয়ের শেষ থেকে খোঁজা শুরু করে। এটি সাবস্ট্রিংটির শেষ অবস্থানের ইনডেক্স ফেরত দেয়।

sentence = "পাইথন একটি জনপ্রিয় প্রোগ্রামিং ভাষা। পাইথন শিখুন।"
index = sentence.rfind("পাইথন")
print(index)  # Output: 33

3.
replace() Method:
•  replace() method টি একটি স্ট্রিংয়ের মধ্যে নির্দিষ্ট একটি সাবস্ট্রিংকে অন্য একটি সাবস্ট্রিং দিয়ে প্রতিস্থাপন করে।
এটি পুরানো সাবস্ট্রিংটি সম্পূর্ণ স্ট্রিংয়ের মধ্যে প্রতিটি ঘটনা প্রতিস্থাপন করে।

sentence = "পাইথন একটি জনপ্রিয় প্রোগ্রামিং ভাষা।"
replaced_sentence = sentence.replace("জনপ্রিয়", "শক্তিশালী")
print(replaced_sentence)  # Output: পাইথন একটি শক্তিশালী প্রোগ্রামিং ভাষা।

এই methods গুলি স্ট্রিং অপারেশনের জন্য খুবই উপকারী, যেমন টেক্সট প্রসেসিং, ডেটা মাইনিং, এবং ওয়েব স্ক্র্যাপিং।

                                   CLASS---13.7

পাইথনের strip, lstrip, এবং rstrip methods স্ট্রিং থেকে অবাঞ্ছিত স্পেস বা অক্ষরগুলি সরানোর জন্য ব্যবহৃত হয়। এগুলি কিভাবে কাজ করে তা নিচে ব্যাখ্যা করা হল:

1.
strip() Method:
•  strip() method টি একটি স্ট্রিং থেকে শুরু এবং শেষের দিকের স্পেস বা নির্দিষ্ট অক্ষরগুলি সরায়।
 যদি কোনো অক্ষর নির্দিষ্ট না করা হয়, তাহলে ডিফল্ট হিসেবে স্পেস সরানো হয়।

example = "   পাইথন   "
print(example.strip())  # Output: "পাইথন"

পাইথনের strip() method টি একটি স্ট্রিং থেকে শুরু এবং শেষের দিকের অবাঞ্ছিত স্পেস বা অক্ষরগুলি সরানোর জন্য ব্যবহৃত হয়।
এই method টি খুবই কার্যকরী যখন আপনি ডেটা পরিষ্কার করতে চান বা ইনপুট থেকে অতিরিক্ত স্পেস সরাতে চান।
এখানে strip() method টির বিস্তারিত ব্যাখ্যা দেওয়া হল:

•  সিনট্যাক্স:

str.strip([chars])

chars হল ঐচ্ছিক প্যারামিটার যা নির্দিষ্ট করে কোন অক্ষরগুলি স্ট্রিং থেকে সরানো হবে।
যদি chars নির্দিষ্ট না করা হয়, তাহলে স্ট্রিং থেকে সব স্পেস সরানো হবে।

•  ব্যবহার:

strip() method টি স্ট্রিংয়ের শুরু এবং শেষের দিকের স্পেস বা নির্দিষ্ট অক্ষরগুলি সরায়।
এটি মূলত স্ট্রিংয়ের দুই প্রান্ত থেকে অবাঞ্ছিত অংশ সরাতে ব্যবহৃত হয়।

•  উদাহরণ:

ধরুন, আপনি একটি স্ট্রিং থেকে শুরু এবং শেষের দিকের কমা এবং স্পেস সরাতে চান:

text = ", পাইথন, "
clean_text = text.strip(", ")
print(clean_text)  # Output: "পাইথন"

এখানে, strip(", ") ব্যবহার করে স্ট্রিং থেকে কমা এবং স্পেস সরানো হয়েছে।



2.
lstrip() Method:
•  lstrip() method টি শুধুমাত্র স্ট্রিংয়ের শুরুর দিকের স্পেস বা অক্ষরগুলি সরায়।

example = "   পাইথন   "
print(example.lstrip())  # Output: "পাইথন   "

3.
rstrip() Method:
•  rstrip() method টি শুধুমাত্র স্ট্রিংয়ের শেষের দিকের স্পেস বা অক্ষরগুলি সরায়।

example = "   পাইথন   "
print(example.rstrip())  # Output: "   পাইথন"


                     CLASS--13.8

পাইথনের split এবং splitlines methods স্ট্রিং অপারেশনের জন্য খুবই উপকারী।
এগুলি কিভাবে কাজ করে তা নিচে বিস্তারিত ভাবে ব্যাখ্যা করা হল:

1.
split() Method:
•  split() method টি একটি স্ট্রিংকে নির্দিষ্ট একটি সেপারেটরের ভিত্তিতে ভাগ করে এবং একটি লিস্ট রিটার্ন করে।
যদি কোনো সেপারেটর নির্দিষ্ট না করা হয়, তাহলে ডিফল্ট হিসেবে স্পেস ব্যবহৃত হয়।

text = "পাইথন শিখুন এবং মজা করুন"
words = text.split()
print(words)  # Output: ['পাইথন', 'শিখুন', 'এবং', 'মজা', 'করুন']

# r akti odaron
split() Method:
•  split() method টি rsplit() এর মতোই কাজ করে, তবে এটি বাম দিক থেকে শুরু করে স্ট্রিংকে ভাগ করে।
maxsplit নির্দিষ্ট করা হলে, এটি সেই সংখ্যক ভাগ করে এবং বাকি অংশটি একটি আইটেম হিসেবে রাখে।

text = "পাইথন শিখুন এবং মজা করুন"
words = text.split(' ', 1)
print(words)  # Output: ['পাইথন', 'শিখুন এবং মজা করুন']

1.2
rsplit() Method:
•  rsplit() method টি একটি স্ট্রিংকে ডান দিক থেকে শুরু করে নির্দিষ্ট একটি সেপারেটরের ভিত্তিতে ভাগ করে।
যদি maxsplit নির্দিষ্ট করা হয়, তাহলে এটি সেই সংখ্যক ভাগ করে এবং বাকি অংশটি একটি আইটেম হিসেবে রাখে।

text = "পাইথন শিখুন এবং মজা করুন"
words = text.rsplit(' ', 1)
print(words)  # Output: ['পাইথন শিখুন এবং', 'মজা করুন']


2.
splitlines() Method:
•  splitlines() method টি একটি স্ট্রিংকে লাইন ব্রেকের ভিত্তিতে ভাগ করে এবং একটি লিস্ট রিটার্ন করে।
এটি ঐচ্ছিক keeplinebreaks প্যারামিটার নেয়, যা নির্দিষ্ট করে যে লাইন ব্রেকগুলি রাখা হবে কিনা।

text = "পাইথন শিখুন\nএবং মজা করুন"
lines = text.splitlines()
print(lines)  # Output: ['পাইথন শিখুন', 'এবং মজা করুন']

split() method টি বিশেষ করে যখন আপনি একটি স্ট্রিংকে শব্দ বা অন্য কোনো টোকেনে ভাগ করতে চান,
তখন খুবই উপকারী। অন্যদিকে, splitlines() method টি মূলত মাল্টি-লাইন স্ট্রিং প্রসেসিং এর জন্য ব্যবহৃত হয়,
যেমন ফাইল থেকে পড়া টেক্সট বা ইউজার ইনপুট।

                                   CLASS--13.10

পাইথনের center, ljust, rjust, expandtabs, join,
এবং slicing methods স্ট্রিং নিয়ে কাজ করার জন্য বিভিন্ন উপায় প্রদান করে।
 এগুলি কিভাবে কাজ করে তা নিচে বিস্তারিত ভাবে ব্যাখ্যা করা হল:

1.
center() Method:
•  center() method টি একটি স্ট্রিংকে নির্দিষ্ট প্রস্থের মধ্যে কেন্দ্রে সাজায় এবং বাকি জায়গাগুলি নির্দিষ্ট অক্ষর দিয়ে পূরণ করে।

text = "পাইথন"
centered_text = text.center(10, '-')
print(centered_text)  # Output: --পাইথন--

2.
ljust() Method:
•  ljust() method টি একটি স্ট্রিংকে বাম দিকে সাজায় এবং ডান দিকে নির্দিষ্ট অক্ষর দিয়ে পূরণ করে।

text = "পাইথন"
left_justified_text = text.ljust(10, '-')
print(left_justified_text)  # Output: পাইথন----

3.
rjust() Method:
•  rjust() method টি একটি স্ট্রিংকে ডান দিকে সাজায় এবং বাম দিকে নির্দিষ্ট অক্ষর দিয়ে পূরণ করে।

text = "পাইথন"
right_justified_text = text.rjust(10, '-')
print(right_justified_text)  # Output: ----পাইথন

4.
expandtabs() Method:
•  expandtabs() method টি একটি স্ট্রিংয়ের মধ্যে থাকা ট্যাব অক্ষরগুলিকে নির্দিষ্ট পরিমাণ স্পেস দিয়ে প্রতিস্থাপন করে।

text = "পাইথন\tশিখুন"
expanded_text = text.expandtabs(4)
print(expanded_text)  # Output: পাইথন  শিখুন

5.
join() Method:
•  join() method টি একটি স্ট্রিং লিস্ট বা টাপলকে একটি সেপারেটর দিয়ে যুক্ত করে একটি স্ট্রিং তৈরি করে।

words = ["পাইথন", "শিখুন", "মজা", "করুন"]
joined_text = " ".join(words)
print(joined_text)  # Output: পাইথন শিখুন মজা করুন

6.
Slicing Methods:
•  Slicing টেকনিক দিয়ে আপনি একটি স্ট্রিং বা লিস্টের নির্দিষ্ট অংশ বের করতে পারেন।

text = "পাইথন শিখুন এবং মজা করুন"
sliced_text = text[7:13]
print(sliced_text)  # Output: শিখুন

####### Aro odaharon diya halo ###@@

1.
center() Method:
•  একটি শব্দকে নির্দিষ্ট প্রস্থের মধ্যে কেন্দ্রে রাখে।

word = "পাইথন"
print(word.center(10, '*'))  # Output: [**পাইথন**](https://www.bing.com/search?form=SKPBOT&q=%E0%A6%AA%E0%A6%BE%E0%A6%87%E0%A6%A5%E0%A6%A8)

2.
ljust() Method:
•  শব্দকে বাম দিকে রেখে ডান দিকে স্পেস বা চিহ্ন দিয়ে ভরাট করে।

word = "পাইথন"
print(word.ljust(10, '*'))  # Output: পাইথন****

3.
rjust() Method:
•  শব্দকে ডান দিকে রেখে বাম দিকে স্পেস বা চিহ্ন দিয়ে ভরাট করে।

word = "পাইথন"
print(word.rjust(10, '*'))  # Output: ****পাইথন

4.
expandtabs() Method:
•  ট্যাব চিহ্নগুলিকে নির্দিষ্ট পরিমাণ স্পেস দিয়ে প্রতিস্থাপন করে।

text = "পাইথন\tশিখুন"
print(text.expandtabs(4))  # Output: পাইথন  শিখুন

5.
join() Method:
•  বিভিন্ন শব্দগুলিকে একত্রিত করে একটি বাক্য তৈরি করে।

words = ["পাইথন", "শিখুন", "মজা", "করুন"]
sentence = " ".join(words)
print(sentence)  # Output: পাইথন শিখুন মজা করুন

6.
Slicing:
•  একটি বাক্য থেকে নির্দিষ্ট অংশ বের করে আনে।

text = "পাইথন শিখুন এবং মজা করুন"
part = text[7:13]
print(part)  # Output: শিখুন




