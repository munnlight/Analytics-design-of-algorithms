def greedy1(bag_size, values, weights):
  value = max(values)
  index = values.index(value)
  weight = weights[index]

  if len(values) == 0:
    return 0

  if bag_size >= weight:
    bag_size -= weight
  else:
    values.pop(index)
    weights.pop(index)
    return greedy1(bag_size, values, weights)

  if bag_size > min(weights):
    return value + greedy1(bag_size, values, weights)
  
  return value


def greedy2(bag_size, values, weights):
  portion = [] 
  in_bag = 0
  for i in range(len(values)):
    portion.append(values[i]/weights[i])

  while min(weights) < bag_size and len(values) > 0:
    index = portion.index(max(portion))
    if weights[index] <= bag_size:
      in_bag += values[index]
      bag_size -= weights[index]
      values.pop(index)
      weights.pop(index)
      portion.pop(index)
    else:
      values.pop(index)
      weights.pop(index)
      portion.pop(index)

  return in_bag

 


values = [1, 5, 10, 15, 10, 12]
weights = [1, 3, 5, 10, 8, 7]
bag_size = 15

# print(greedy1(bag_size, values, weights))
print(greedy2(bag_size, values, weights))