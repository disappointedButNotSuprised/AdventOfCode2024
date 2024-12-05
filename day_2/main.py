import colorama

with open('day_2/input.txt', 'r') as file:
    safe_count = 0
    for line in file:
        incr, decr, safe = False, False, False
        values = line.split()
        for i in range(len(values)):
            values[i] = int(values[i])

        incr = all(x < y for x, y in zip(values, values[1:]))
        desc = all(x > y for x, y in zip(values, values[1:]))

        if incr or desc:
            safe = True
            differences = [abs(y - x) for x, y in zip(values, values[1:])]
            for diff in differences:
                if diff not in range(1, 4):
                    safe = False
                    break

        if safe:
            safe_count = safe_count + 1
    
    print(colorama.Fore.GREEN +  "🎄 Safe count: " + colorama.Fore.RED + f"{safe_count} 🎅")