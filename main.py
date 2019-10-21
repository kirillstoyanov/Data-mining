import csv
import statistics
# data set "wine" has been converted to a list
with open('wine.data', 'r') as f:
    wines = list(csv.reader(f))
#avg value of each atribute
avg_list = []
for j in range(1, 14):
    avg = [float(i[j]) for i in wines]
    sum_score = sum(avg)
    num_score = len(avg)
    avg_list.append(sum_score/num_score)
print(avg_list)
#medain for each atribute
mode_list = []
for j in range(1, 14):
    median = [float(i[j]) for i in wines if i[j] != ""]
    num_wines = len(median)
    sorted_prices = sorted(median)
    mode_list.append(statistics.median(sorted_prices))
print(mode_list)
#minimum and maximum for each atribute
min_score = []
max_score = []
for j in range(1, 14):
    scores = [float(i[j]) for i in wines if i[j] != ""]
    max_score.append(max(scores))
    min_score.append(min(scores))
print(min_score, '\n', max_score)