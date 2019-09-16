with open("text.txt", "w") as my_file:
  my_file.write("Hello world!")
if my_file.closed == False:
  my_file.close()
print my_file.closed
