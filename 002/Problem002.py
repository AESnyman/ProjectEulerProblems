#Project euler website solution
i = 1
j = 2
limit = 4000000
sum = 2

while j < limit:
    t = j
    j = i+t
    i = t

    if j % 2 == 0:
        sum += j

print(sum)

#freeCodeCamp website solution
# n = 18
# i = 1
# j = 2
# sum = j

# for x in range(n-2):
#     t = j
#     j = i+t
#     i = t

#     if j % 2==0:
#         sum += j

# print(sum)