import colorama

with open('input.txt', 'r') as file:
    column1 = []
    column2 = []
    for line in file:
        col1, col2 = line.split()
        column1.append(col1)
        column2.append(col2)
distance = 0
for i in range(len(column1)):
    col1_min = min(column1)
    col2_min = min(column2)
    column1.remove(col1_min)
    column2.remove(col2_min)
    diff = abs(int(col1_min) - int(col2_min))
    distance += diff
    
print(colorama.Fore.GREEN + "🎄 Distance: " + colorama.Fore.RED + f"{distance} 🎅")