
x = [2, 4, 6, 8, 9, 10, 12]

for num in x:
    if num % 2 != 0:   # if number is odd
        print(f"Found odd number: {num}")
        break           # stop the loop
    print(num)

    index_count =0
    for letter in 'abcde':
        print("at index is {},at index letter is {}".format(index_count,letter))
        index_count+=1

