# Naive approach
# def is_happy_number(n):
#     slow = n 
#     fast = sum_of_squared_digits(slow)
#     lists = []
#     lists.append(slow)
#     if fast == slow:
#         return True
#     while fast != slow:
#         if fast != 1: 
#             slow = sum_of_squared_digits(slow) 
#             fast = sum_of_squared_digits(fast)
#             lists.append(slow)
#             if fast in lists:
#                 return False
#             else:
#                 pass
#         else:
#             return True
#     return False

# Using fast and slow pointers
def is_happy_number(n):
    slow = n 
    fast = sum_of_squared_digits(slow)

    # if fast == slow:
    #     return True
    
    while fast != slow or fast == slow:
        if fast != 1: 
            slow = sum_of_squared_digits(slow) 
            fast = sum_of_squared_digits(fast)
            fast = sum_of_squared_digits(fast)

            if fast == slow:
                return False
            
        else:
            return True

def sum_of_squared_digits(number): # Helper function that calculates the sum of squared digits.
    total_sum = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        total_sum += digit ** 2
    return total_sum

def main(): 

    input = [1, 5, 19, 25, 7]
    # input = [1]


    for i in range(len(input)):
        print("Test Case #", i + 1)
        print(" Given the input:", input[i], ", Is it a happy number?", is_happy_number(input[i]))
        print("-"*100)


if __name__ == "__main__":
    main()