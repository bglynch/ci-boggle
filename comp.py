# List Comprehensions and Dictionary Comprehensions


# -----------------------------------------------------------------List Comprehension
# ---------------------------------------------Example 1

# l = [1, 3, 5]
# p = [n*2 for n in l]
# print(p)


# p=[]
# for n in l:
#     p.append(n * 2)
# print(p)


# # Produce list [0, 2, 4, 6, 8, 10, 12]
# print([i*2 for i in range(7)])

# # Produce a list of even numbers
# print([i for i in range(10) if i % 2 == 0])

# # 
# print([(i,j) for i in range(0, 10)
#             for j in range(0,10)])

# # 
# print([(i,j) for i in range(0, 10)
#         for j in range(0,10)])

# # 
# print([[j for j in range(i)] for i in range(10)])




# ------------------------------------------------------   List Comprehension Challenges

# print([i*2 for i in range(10)])

# # 1. range(5) 
# # -> ["*", "*", "*", "*", "*"]
# print(["*" for i in range(5)])

# # 2. ["Hi", "There", "Everyone"] 
# # -> [2, 5, 8]
# print([len(i) for i in ["Hi", "There", "Everyone"]])

# # 3. range(8) 
# # -> [0, 1, 4, 9, 16, 25, 36, 49]
# print([i**2 for i in range(8)])

# # 4. range(5) 
# # -> [(0,1), (1,2), (2,3), (3,4), (4,5)]
# print([(i, i+1) for i in range(5)])

# # 5. 'woohoo' 
# # -> ['w', 'o', 'o', 'h', 'o', 'o']
# print([i for i in "woohoo"])

# # 6. ['car', 'cat', 'maps', 'if', 'level'] 
# # -> [('car', 3), ('cat', 3), ('maps', 4), ('if', 2), ('level', 5)]
# print([(i, len(i)) for i in ['car', 'cat', 'maps', 'if', 'level']])

# # 7. [(False, False), (False, True), (True, False), (True, True)]
# # ->[False, False, False, True]
# ch7 = [(False, False), (False, True), (True, False), (True, True)]
# print([i[0] and i[1] for i in ch7  ])
# print([j for i in ch7[:2] for j in i ])
# print([ i and j for i,j in ch7])

# # 8. [(False, False), (False, True), (True, False), (True, True)]
# # ->[False, True, True, True]
# print([i[0] or i[1] for i in [(False, False), (False, True), (True, False), (True, True)]])


# ------------------------------------------------------   Dictionary Comprehension Challenges
# range(10) 
# -> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print({i:i*"*" for i in range(10) })


# 1. ['Hi', 'There', 'Everyone'] 
# -> {'Hi':2, 'There':5, 'Everyone':8}

# 2. 'code'
# -> {'c': 99, 'e': 101, 'd': 100, 'o': 111} ord()

# 3. ['car', 'pop', 'maps', 'if', 'level'] 
# -> {'car':False, 'pop':True, 'maps':False, 'if':False, 'level':True}

# 1.

