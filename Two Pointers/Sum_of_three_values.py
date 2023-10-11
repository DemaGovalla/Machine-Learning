def find_sum_of_threes(nums, target):
    nums.sort()

    for i in range(0, len(nums)-2):
        low = i + 1
        high = len(nums) - 1

        while low < high:
            triplet = nums[1] + nums[low] + nums[high]

            if triplet == target: 
                return True
            
            elif triplet < target: 
                low +=1

            else:
                high -=1

    return False


def main(): 
    nums_lists = [[3,7,1,2,8,4,5], [-1,1,1,-4,5,-3], [2,3,4,1,7,9],
                  [1,-1,0], [2,4,2,7,6,3,1]]
    
    targets = [10, 7, 20, -1, 8]

    for i in range(len(nums_lists)):
        print(i + 1, ".\tInput array: ", nums_lists[i], sep="")
        if find_sum_of_threes(nums_lists[i], targets[i]):
            print("\tSum for", targets[i], "exist")
        else: 
            print("\tSum for", targets[i], "does not exist")
        print("-"*100)

if __name__ == '__main__':
    main()