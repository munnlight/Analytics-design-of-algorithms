def knapsack(bag_size, weights, values):
  portion = []

  for i in range(len(weights)):
    portion.append(values[i] / weights[i])
  
  index = portion.index(max(portion))
  value = values[index]
  weight = weights[index]

  if bag_size >= weight:
    values.pop(index)
    weights.pop(index)
    return value + knapsack(bag_size - weight, weights, values)
  else:
    return portion[index] * bag_size
  
size = 10
values = [10, 12, 15, 20]
weights = [5, 3, 5, 4]
print(knapsack(size, weights, values))