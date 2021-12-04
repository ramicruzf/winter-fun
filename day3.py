from collections import Counter


def counter(lst, type=None):
    c = Counter(lst)
    zero = c['0']
    one = c['1']

    if type == 'high':
        if zero > one:
            return '0'

        elif one > zero:
            return '1'

        elif one == zero:
                return '1'

    if type == 'low':
        if zero > one:
            return '1'
        elif one > zero:
            return '0'
        elif one == zero:
                return '0'

def show_list(lst):
    for i in lst:
        print(i)

def logico(lst, type):
    for i, l in enumerate(lst):
        bit = counter(lst[i], type)
        reg_lst = [''.join(r) for r in zip(*lst)]
        temp = []
        for index, number in enumerate(reg_lst):
            if bit == number[i]:
                temp.append(number)
        if len(temp) == 1: 
            return temp[0]
        lst = [''.join(r) for r in zip(*temp)]
    return [''.join(r) for r in zip(*lst)][0]

#read file
f = open('report.txt', 'r')
# map (function to remove extra characters, file)
# zip just transposes the matrix 
lst = [''.join(r) for r in zip(*map(str.rstrip, f))]


gamma_rate = ''
epsilon_rate = ''
for l in lst:
    c = Counter(l)
    zero = c['0']
    one = c['1']
    if zero > one:
        gamma_rate += '0'
        epsilon_rate += '1'
    elif one > zero:
        gamma_rate += '1'
        epsilon_rate += '0'
print('--- Part 1 ---')
print(f'gamma_rate: {gamma_rate}')
print(f'epsilon rate: {epsilon_rate}')
pc = int(gamma_rate, 2) * int(epsilon_rate,2)
print(f'PC: {pc}')

# 2nd part
# for high, if equal choose 1 - 10110
# for low, if equal choose 0


    



oxygen_generator_rating = logico(lst, 'high') 
co2_scrubber_rating = logico(lst, 'low')
print('--- Part 2 ---')
print(f'oxygen generator rating: {oxygen_generator_rating}')
print(f'CO2 scrubber rating : {co2_scrubber_rating}')
life_support_rating = int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)
print(f'life support rating: {life_support_rating}')


