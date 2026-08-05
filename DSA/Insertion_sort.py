"""Time Complexity:
Best	:O(n)
Average :O(n²)
Worst	:O(n²)


SC=O(1)

"""
def insertion_sort(nums):
    n=len(nums)
    for i in range(1,n):
        Key=nums[i]
        j=i-1
    
        while j>=0 and nums[j]>Key:
            nums[j+1]=nums[j]
            j-=1
        
        nums[j+1]=Key
    

nums=[4,6,2,8,1,6]
print(insertion_sort(nums))