# class Solution(object):
#     def leastInterval(self, tasks, n):
#         difTask = {}
#         for i in range(len(tasks)):
#             if tasks[i] in difTask:
#                 difTask[tasks[i]] += 1
#             else:
#                 difTask[tasks[i]] = 1
        
#         # difTask = dict(sorted(difTask.items(), key = lambda item: item[1], reverse=True))
#         # print(difTask)
#         vals = list(difTask.values())
#         # print(vals)
#         pos = [0] * len(vals)
#         count = 0
#         kl = len(vals)
        
#         while kl != 0:
#             for i in range(n):
#                 i = vals.index(max(vals))
#                 if pos[i] == 0:
#                     pos[i] = n + 1
#                     vals[i] -= 1

#                     if vals[i] == 0:
#                         vals.pop(i)
#                         pos.pop(i)
#                         kl = len(vals)
                        

#                 elif 0 in pos:
#                     ind = pos.index(0)
#                     pos[ind] = n + 1
#                     vals[ind] -= 1
                    
#                     if vals[ind] == 0:
#                         vals.pop(ind)
#                         pos.pop(ind)
#                         kl = len(vals)

#                 pos = [x - 1 if x > 1 else 0 for x in pos]
#                 count += 1
#                 # print(vals)
#                 # print(pos,' aa')
#                 if kl == 0:
#                     break
#             # print(difTask)
        
#         # print(count)
#         return count
                 
class Solution(object):
    def leastInterval(self, tasks, n):
        difTask = {}
        for i in range(len(tasks)):
            if tasks[i] in difTask:
                difTask[tasks[i]] += 1
            else:
                difTask[tasks[i]] = 1
        
        vals = list(difTask.values())
        count = 0
        kl = len(vals)
        
        while kl != 0:
            if kl > n + 1:
                for i in range(n):
                    vals[i] -= 1
            else:
                for i in range(kl):
                    vals[i] -= 1
                    
            count += n
            
            for i in range(len(vals) - 1, -1, -1):
                if vals[i] == 0:
                    vals.pop(i)
                    if len(vals) == 0:
                        break
                    
            s = kl
            kl = len(vals)
            if kl == 0:
                count = count - n + s

        return count

tasks = ["A","A","A","B","B","B"]
n = 2

c = Solution()
print(c.leastInterval(tasks, n))