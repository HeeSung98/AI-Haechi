import os
import re
from Graph_generator_for_GNN.parsing.Generator import generate


abs_code_path = os.path.abspath('../embedding/embedding_code')
abs_result_path = os.path.abspath('../result/embedding')
tmp = ['unchecked external call']
weakness_name = ['block number dependency', 'dangerous delegatecall', 'ether frozen', 'ether strict equality',
                 'integer overflow', 'reentrancy', 'timestamp dependency', 'unchecked external call']
vocabulary = {}
preprocessed_sentences = []

success_count = 0
fail_count = 0
success_file = []
fail_file = []

for weakness in weakness_name:
    print(weakness)
    folder_path = abs_code_path + '\\' + weakness
    solidity_list = os.listdir(folder_path)
    result = []
    for file_name in solidity_list:
        file_path = folder_path + '\\' + file_name
        try:
            viz_code = generate(file_path, file_name)

            for line in viz_code.split("\n"):
                for word in line.split(' '):

                    result.append(word)
                    if word not in vocabulary:
                        vocabulary[word] = 0
                    vocabulary[word] += 1
            preprocessed_sentences.append(result)
            success_count += 1
            success_file.append(file_name)
            print('now...', file_name)
            if success_count == 80:
                success_count = 0
                break

        except Exception as e:
            fail_count += 1
            fail_file.append(file_name)
            print(file_name + ": " + str(e))

            continue

        print('success:', success_count)
        # print('success:', success_file)
        print('fail:', fail_count)
        # print('fail:', fail_file)

vocabulary_sorted = sorted(vocabulary.items(), key=lambda x: x[1], reverse=True)

integer_encoding = open(abs_result_path + '/WordFrequency.txt', 'w+')
integer_encoding.write(str(vocabulary_sorted))
integer_encoding.close()

print('done')
