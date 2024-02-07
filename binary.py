def binary():
    nums=list(map(int,input("Enter values into list: ").split()))
    target=int(input("Enter target value: "))
    l=0
    r=len(nums)-1
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==target:
            return nums[mid]
        elif nums[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return -1
print(binary())
