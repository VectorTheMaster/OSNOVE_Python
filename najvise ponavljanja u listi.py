test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 2]
print(max(set(test), key=test.count))
