#!/usr/local/bin/python3

for i in range(10):
  x = i
  print(x)

count = 0

while True:
#  print("The count is {}".format(count))
  print(f"The count is {count}")
  if count > 5:
    break
  count += 1

my_sequence = "Bill Cheatham"
my_sequence.index('C')
my_sequence.index('a',9, 12) #search within range
my_sequence[2]

my_sequence = [0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4]
len(my_sequence)
min(my_sequence)
max(my_sequence)
my_sequence.count(1)
#Lists
a = list()
b = list(range(10))
c = list("Henry Miller")
nine = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nine.append('rhubarb')
nine.insert(1, 'cream')
b.extend(c)

squares = [i*i for i in range(10)]
squares = [i*i for i in range(10) if i%2==0]
#Strings
multi_line = ''' Print
multi
line
string'''
print(multi_line)
url = "gt.motomomo.io/v2/api/asset/143"
url.split('/')
items = ['cow', 'milk', 'bread', 'butter']
print(" and ".join(items)
name = "John Paul Jones"
name.capitalize())
name.upper()
name.title()
name.swapcase()

