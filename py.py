import re
opening_file = open("regex_sum_875539.txt")
my_list = list()
for line in opening_file:
     finding= re.findall('[0-9]+', line)
     my_list = my_list + finding
sum = 0
for loop in my_list:
    sum = sum + int(loop)
print(sum)