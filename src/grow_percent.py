test_array = [1,-2,4,00,00,-32, 0, -2, 2]
percent_array = []
array_count = len(test_array)
for i in range(0, array_count):
    if i+1 >= array_count:
        break
    if test_array[i] != 0:
        percent_array.append(((test_array[i+1] - test_array[i]) / abs(test_array[i])) * 100)
    else:
        if test_array[i+1] > 0:
            percent_array.append(100)
        elif test_array[i+1] == 0:
            percent_array.append(0)
        else:
            percent_array.append(-100)

for item in percent_array:
    print(item)

print('--------------------------------------')
print(sum(percent_array) / len(percent_array))