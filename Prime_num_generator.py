def prime_num_gen(num1,num2):
    prime_nums = []
    for i in range (num1, num2 + 1):
        if((i % 2 != 0) or (i == 2)):
            prime_nums.append(i)
    return prime_nums
        
num1 = 2
num2 = 39

print(prime_num_gen(num1,num2))