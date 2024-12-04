import colorama

with open('day_1/input.txt', 'r') as file:
    column1 = []
    column2 = []
    for line in file:
        col1, col2 = line.split()
        column1.append(int(col1))
        column2.append(int(col2))
        column1_copy = column1.copy()
        column2_copy = column2.copy()

# puzzle 1
distance = 0
for i in range(len(column1)):
    col1_min = min(column1)
    col2_min = min(column2)
    column1.remove(col1_min)
    column2.remove(col2_min)
    diff = abs(int(col1_min) - int(col2_min))
    distance += diff
    
print(colorama.Fore.GREEN +  "🎄 Distance: " + colorama.Fore.RED + f"{distance} 🎅")

# puzzle 2
score_sum = 0
for val1 in column1_copy:
    count = 0
    for val2 in column2_copy:
        if val1 == val2:
            count = count + 1
    score = val1 * count
    score_sum = score_sum + score

print(colorama.Fore.GREEN +  "🎄 Similarity score: " + colorama.Fore.RED + f"{score_sum} 🎅")