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
