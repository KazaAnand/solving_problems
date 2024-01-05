def binary():
    nums=list(map(int,input().split()))
    target=int(input())
    l=0
    r=len(nums)-1
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return -1
print(binary())