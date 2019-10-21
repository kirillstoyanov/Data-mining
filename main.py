import csv
import statistics
with open('wine.data', 'r') as f:
    wines = list(csv.reader(f))
avg_list = []
for j in range(0, 13):
    avg = [float(i[j]) for i in wines]
    sum_score = sum(avg)
    num_score = len(avg)
    avg_list.append(sum_score/num_score)
print(avg_list)
mode_list = []
for j in range(0, 13):
    moda = [float(i[j]) for i in wines if i[j] != ""]
    num_wines = len(moda)
    sorted_prices = sorted(moda)
    mode_list.append(statistics.median(sorted_prices))
print(mode_list)
