genome = input()
i=genome.upper()
a=i.count('G') + i.count('C')
print(a/len(i)*100)
