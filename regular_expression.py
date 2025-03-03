import re


>>> phone_number = "My number is 91-90257 92266"
>>> match = re.search(r'\d{2}-\d{5} \d{5}', phone_number)
>>> if match:
...     "Phone number found:", match.group()

('Phone number found:', '91-90257 92266')

# re.match()

# basic match
>>> text = "Good Morning"
>>> a = re.match(r'Good', text)
>>> (match.group() if a else "No match")

'Hello'

# matching digits at the start
>>> b = "123abc"
>>> b1 = re.match(r'\d+', b)
>>> (b1.group() if b1 else "No match")

'123'

# Matching a full word
>>> c = "Python is great"
>>> c1 = re.match(r'\w+', c)
>>> (c1.group() if c1 else "No match")

'Python'

# matching with special characters
>>> d = "#Python3"
>>> d1 = re.match(r'[#@]\w+', d)
>>> (d1.group())

'#Python3'

>>> d = "Python3"
>>> d1 = re.match(r'[#@]\w+', d)
>>> (d1.group() if d1 else "No Special Character")

'No Special Character'

# using Groups
>>> e = "2025-03-01"
>>> e1 = re.match(r'(\d{4})-(\d{2})-(\d{2})', e)
>>> if e1:
...     ("Year:", e1.group(1))
...     ("Month:", e1.group(2))
...     ("Day:", e1.group(3))
...
('Year:', '2025')
('Month:', '03')
('Day:', '01')
>>>
>>> ee = "2025-03-sub"
>>> ee1 = re.match(r'(\d{4})-(\d{2})-(\d{2})', ee)
>>> if ee1:
...     ("Year:", ee1.group(1))
...     ("Month:", ee1.group(2))
...     ("Day:", ee1.group(3))
... else:
...     "Enter proper date"
...
'Enter proper date'
>>>

# re.search

# finding numbers in a string

>>> f = "My age is 22"
>>> f1 = re.search(r'\d+', f)
>>> (f1.group())

'22'


>>> ff = "My age is Twenty-Two"
>>> ff1 = re.search(r'\d+', ff)
>>> if ff1:
...     ff1.group()
... else:
...     "There is no number in this string."
...
'There is no number in this string.'

# finding mail id

>>> g = "Mail id subash@gmail.com"
>>> g1 = re.search(r'\w+@\w+\.\w', g)
>>> 
>>> g = "Mail id subash@gmail.com"
>>> g1 = re.search(r'\w+@\w+\.\w+', g)
>>> if g1:
...     g1.group()
... else:
...     "no mail id"
... 
'subash@gmail.com'
>>> 
>>> gg = "Mail id subash@gmail"
>>> gg1 = re.search(r'\w+@\w+\.\w+', gg)
>>> if gg1:
...     gg1.group()
... else:
...     "Enter a proper mail id"
... 
'Enter a proper mail id'

# finding a date in a sentence

>>> h = "He is running fast."
>>> h1 = re.search(r'\b\w+ing\b', h)
>>> if h1:
...     h1.group()
... else:
...     "There is no gerunds"
... 
'running'
>>> 
>>> hh = "he runs fast."
>>> hh1 = re.search(r'\b\w+ing\b', hh)
>>> if hh1:
...     hh1.group()
... else:
...     "There is no gerunds."
... 
'There is no gerunds.'
>>> 

