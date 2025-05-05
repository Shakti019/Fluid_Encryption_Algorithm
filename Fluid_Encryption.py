from itertools import combinations, permutations

import itertools

def fluid_encrypt(values):
    value = [int(c) for c in values]
    permutations = list(itertools.permutations(value,4))
    xor_results = []
    for perm in permutations:
        xor_result = 0
        for i in range(len(perm) - 1):
            xor_result ^= perm[i] ^ perm[i + 1]
        xor_results.append(xor_result)
    print("xor",xor_results)
    nor_results = []
    for i in range(len(xor_results) - 1):
        nor_result = ~(xor_results[i] | xor_results[i + 1])
        nor_results.append(nor_result)
    print("nor",nor_results)
    and_results = []
    xor_and_results = []
    print("xor",xor_result)
    for i in range(len(nor_results) - 1):
        and_result = nor_results[i] & nor_results[i + 1]
        and_results.append(and_result)
        xor_result = nor_results[i] ^ nor_results[i + 1]
        xor_and_results.append(xor_result)
    print("Pattern of Password Encryption: ",xor_and_results)
    print("Final Value Saved in Database: " ,"[",xor_result,"]")



    return  xor_result




if __name__ =='__main__':
    values = ['111111', '000000', '000000', '111111', '000000', '111111', '000000', '000000', '000000',
              '111111','000000', '111111']

    fluid_encrypt(values)