def kbig(nums, k):
    i = 0
    m = 0
    while i != k:
        for j in range(len(nums)):
            m = max(nums)
            if i+1 != k:
                nums.remove(m)
                break
        i += 1
    return m


nums = list(map(int, input().split()))
k = int(input())
print(kbig(nums, k))
