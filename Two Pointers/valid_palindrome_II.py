def is_palindrome(s):

    left = 0
    right = len(s) - 1

    marker = 0

    while left < right: 
        if s[left] == s[right]:

            left +=1
            right -=1

            # return True
        
        elif s[left] != s[right]:

            right -= 1
            if s[left] != s[right]:

                right += 1
                left += 1
                if s[left] != s[right]:

                    return False

            else: 
                pass

            # marker += 1

            # if marker == 2: 
            #     return False

            # if marker == 2: 
            #     return False
            
            # else: 

            #     marker +=1
            #     right -=1
            #     if s[left] != s[right]:
            #         right +=1
            #         left +=1
                



    return True

def main(): 
    
    test_cases = ["madame", "dead", "oeijdje", "abca", "tebbem", "eeccccbebaeeabebccceea"]
    
    for i in range(len(test_cases)):
        print("Test case #", i + 1)
        print(test_cases[i])
        print("Is it a palindrome?...", is_palindrome(test_cases[i]))
  

if __name__ == "__main__":
    main()