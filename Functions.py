

def learn_python(num1,num2):
    return num1 +num2
result = learn_python(1,2)
print(result)

def abc_even_list(even):
    even_num_list = []
    for number in even:
        if number%2 == 0:
            even_num_list.append(number)
        else:
            pass
    return even_num_list

print(abc_even_list([1,2,3,4,5,6,7,8,9,0]))

