# 5
# 16115 164024 634560 46828 551274 32945 35236 6060 453096 22624

def find_n(n1, n2):
    while n1 != n2:
        if n1 > n2:
            n1 -= n2
        else:
            n2 -= n1
    return n1

n = input()

nums = input().split()
nums = [int(a) for a in nums]
nums.sort()
table = [[0] * len(nums) for _ in range(len(nums))]

for i in range(len(nums)):
    for j in range(len(nums)):
        if i == j:
            continue
            
        if table[i][j] != 0:
            continue
        
        # if max(nums[j], nums[i]) % min(nums[j], nums[i]) == 0:
        #     table[j][i] = table[i][j] = max(nums[j], nums[i]) / (max(nums[j], nums[i]) / min(nums[j], nums[i]))
        else:
            table[j][i] = table[i][j] = find_n(nums[j], nums[i])
        

# for i in range(len(nums)):
#     print(table[i])

            
minn = []
used = 0
notUse = []

while len(notUse) / 2 != len(nums) / 2:
    maxi = 0
    x = y = -1
    for i in range(len(nums)):
        if i in notUse:
            continue
            
        temp = max(table[i])
        
        if maxi < temp:
            maxi = temp
            x = i
            y = table[i].index(maxi)
            
    # if maxi == 0:
    #     iter = len(nums) // 2 - len(notUse) // 2
    #     for i in range(iter):
    #         minn.append(1)
    #     break
    
    notUse.append(x)
    notUse.append(y)
    minn.append(maxi)

sum = 0
minn.sort()

for i in range(len(minn)):
    sum += (i + 1) * minn[i]
    
print(int(sum))
    

        
        