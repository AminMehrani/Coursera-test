textfile = open ('regex_sum_1201419.txt')
sum = 0
for x in textfile:
    import re
    numbers = re.findall('([0-9]+)', x)
    if len(numbers) <1: continue
    for number in numbers:
        number = int(number)
        #print(number)
        sum = sum + number
    print(sum)
