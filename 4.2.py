import random


def block_sort(input_list):
    max_value = max(input_list)
    size = max_value / len(input_list)
    block_list = []
    for x in range(len(input_list)):
        block_list.append([])
    for i in range(len(input_list)):
        j = int(input_list[i] / size)
        if j != len(input_list):
            block_list[j].append(input_list[i])
        else:
            block_list[len(input_list) - 1].append(input_list[i])
    for z in range(len(input_list)):
        insertion_sort(block_list[z])
    final_output = []
    for x in range(len(input_list)):
        final_output = final_output + block_list[x]
    return final_output
def insertion_sort(block):
    for i in range (1, len (block)):
        var = block[i]
        j = i - 1
        while (j >= 0 and var < block[j]):
            block[j + 1] = block[j]
            j = j - 1
        block[j + 1] = var
input_list=[random.randint(1,1000) for i in range(100)]
print(block_sort(input_list))