import re
hand = open('regex_sum_1506522.txt')
numlist = list()
for line in hand:
    line = line.strip()
    #print(line)
    nums = re.findall('[0-9]+', line)
    #print(nums)
    numlist = numlist + nums
    #print(numlist)
    #print(numlist) #appending every number in the list to the end of the main list, if empty list, would just repeat the list
sum = 0
for i in numlist:
    #print(i) #searches through every element in the main list and returns it
    sum=sum + int(i)
print(sum)

