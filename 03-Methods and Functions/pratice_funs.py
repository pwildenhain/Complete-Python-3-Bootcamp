name  = 'macdonald'
name[0].upper() + name[1:3] + name[3].upper() + name[4:]

text = 'I am home'
words = text.split()
words.reverse()
words

three_apart = [1, 3, 1, 3]
three_together = [1, 3, 3]

mylist = [str(num) for num in three_together]
mystring = ''
for num in mylist:
    mystring += num

'33' in mystring

text = 'hello'
triple_text = ''
for letter in text:
    triple_text += letter * 3

triple_text


arr = [4, 5, 7, 8, 9]

arr.index(6)
arr.index(9)

nums_to_remove = arr[2:6]

for num in nums_to_remove:
    arr.remove(num)

sum(arr)

arr = []
sum(arr)

num = 3
all_remainders = [num % i for i in range(3, num, 2)] 
0 in all_remainders
all(all_remainders)

num = 9
prime_count = 0
for current_num in range(2, num + 1):
    if current_num % 2 == 0:
        print(f'{current_num} is divisible by 2')
        continue
    print(f'{current_num} is not divisible by 2')
    all_remainders = [current_num % smaller_num for smaller_num in range(3, current_num, 2)] 
    if 0 in all_remainders:
        print(f'{current_num} is not prime')
        print(f'count: {prime_count}')
        continue
    else:
        print(f'{current_num} is prime')
        prime_count += 1
        print(f'count: {prime_count}')



