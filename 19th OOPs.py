"""
Selection sort Using Python

In this method swapping is done at ones as follows
Step 1 : Lets take eg array as 5,3,8,6,7,2
Step 2 : In this lets take min as 5 at first
step 3 : Now it will check 2 number of first 2 index like 5,3 in this 3 is small so 5and 3 will swap
Step 4: But taking 5 as min will be still there until it checks with all array like - last number in array is 2
        So it will swap 5 with 2
Step 5 : This complete the first Iteration in array...This will continue until all number are checked

* After step 4 The min value will be set as 2. The the 2 will be shifted to new array as sorted array
* after that 3 onwards number will be present in unsorted array, In each Iteration one number will be shifted to sorted array
"""

def sort(nums):
    for i in range(5):
        min = i
        for j in range(i,6):
            if nums[j]<nums[min]:
                min = j
        temp = nums[i]
        nums[i] = nums[min]
        nums[min] = temp
        print (nums,"\n")

nums = [2,8,4,5,6,1]
sort(nums)

print(nums)
