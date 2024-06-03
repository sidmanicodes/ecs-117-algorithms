def brute_force_continuous(arr):
    max_val = float('-inf')
    max_subarr = []
    n = len(arr)
    for i in range(n):  
        for j in range(i+1, n+1):
            subarr = arr[i:j]
            if all(subarr[k] < subarr[k+1] for k in range(len(subarr) - 1)):
                if sum(subarr) >= max_val:
                    max_val = sum(subarr)
                    max_subarr = subarr 

    return max_subarr

def brute_force_noncontinuous(arr):
    max_val = float('-inf')
    max_subarr = []
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            subarr = arr[i:j+1]
            cur_sum = sum(subarr)
            if cur_sum > max_val:
                max_val = cur_sum
                max_subarr = subarr
    return max_subarr

arr = [-6, -5, -2, -100, -200]
print(brute_force_continuous(arr=arr))
print(brute_force_noncontinuous(arr=arr))
