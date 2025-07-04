data = [[1, 2, 3], [4, 5], [6, 3, 3]]
total=0
for sublist in data:
    for number in sublist:
        total+=number
print(f"總和是: {total}")
