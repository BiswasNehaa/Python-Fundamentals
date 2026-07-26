def freq(nums):
    freq_map={}
    for i in range(len(nums)):
        if nums[i] in freq_map:
            freq_map[nums[i]]+=1
        else:
            freq_map[nums[i]]=1
    return freq_map

def hash(nums):
    print("using hash map")
    hash_map={}
    for i in range(len(nums)):
        hash_map[nums[i]]=hash_map.get(nums[i],0)+1
    return hash_map

print(freq([5,6,7,1,1,7]))
print(hash([5,6,7,1,1,7]))