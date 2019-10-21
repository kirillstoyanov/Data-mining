# import csv
# with open('wine.data', 'r') as f:
#     wines = list(csv.reader(f))
#
# scores = [float(i[0]) for i in wines]
# sum_score = sum(scores)
# num_score = len(scores)
# avg_score = sum_score/num_score
# print(avg_score)
#
# scores = []
# for i in wines:
#     x = float[i]
#     sum_score = sum(x)
#     num_score = len(x)
#     i += 1
# print(scores)

import csv
with open('wine.data', 'r') as f:
    wines = list(csv.reader(f))
avg_score = []
for j in range(0, 13):
    scores = [float(i[j]) for i in wines]
    sum_score = sum(scores)
    num_score = len(scores)
    avg_score.append(sum_score/num_score)
print(avg_score)

