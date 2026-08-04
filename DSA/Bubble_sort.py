# TC= O(n2) (worst case)
# TC= O(n) (best case)
# SC= O(1) 

def bubble_sort(nums):
    n=len(nums)
    is_swap=False
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                is_swap=True
        
        if is_swap==False:
            return nums
    
    return nums

nums=[4,6,2,8,1,6]
print(bubble_sort(nums))