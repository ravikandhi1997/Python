numbers = [12, 23, 20, 13, 15, 19, 22, 24, 26]

sum_even = 0
sum_odd = 0

for num in numbers:
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)
print(f"Sum of even numbers:{sum_even},Sum of odd numbers: {sum_odd}")