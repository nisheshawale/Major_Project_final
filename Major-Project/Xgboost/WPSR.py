import numpy as np
import re


def sequence_generator(occurence_list, index):
    match_seq_number = occurence_list
    final_space_sequence = []
    repeat = index
    for i in range(len(match_seq_number)):
        # print(i)

        c = i + 1
        d = i
        if c == len(match_seq_number):
            final_space_sequence.append(repeat)
            break
        if (match_seq_number[c] == match_seq_number[d] + 1):
            repeat = repeat + 1
            continue
        else:
            if index == 0:
                if repeat > 0:
                    final_space_sequence.append(repeat)
            else:
                final_space_sequence.append(repeat)

            repeat = index

    return final_space_sequence

def pattern_distance(pattern, raw_text1, raw_text2, index):
    matches1 = pattern.finditer(raw_text1)
    matches2 = pattern.finditer(raw_text2)
    match_seq_number1 = []
    match_seq_number2 = []
    for match in matches1:
        match_seq_number1.append(match.start())
    for match in matches2:
        match_seq_number2.append(match.start())
    vector1 = np.array(sequence_generator(match_seq_number1, index))
    #print(vector1)
    vector2 = np.array(sequence_generator(match_seq_number2, index))
    #print(vector2)
    if vector1.shape[0] > vector2.shape[0]:
        temp = np.zeros(vector1.shape[0])
        temp[:vector2.shape[0]] = vector2
        vector2 = temp
    else:
        temp = np.zeros(vector2.shape[0])
        temp[:vector1.shape[0]] = vector1
        vector1 = temp
    sum_vector1 = vector1.sum()
    sum_vector2 = vector2.sum()
    distance = (np.absolute(vector1 - vector2).sum())
    return distance, sum_vector1, sum_vector2


def edit_distance(filename1, filename2):
    raw_text1 = open(filename1).read()
    raw_text2 = open(filename2).read()
    space_distance, space1, space2 = pattern_distance(re.compile(r' '), raw_text1, raw_text2, 1)
    indent_distance, indent1, indent2 = pattern_distance(re.compile(r'\t'), raw_text1, raw_text2, 1)
    newline_distance, newline1, newline2 = pattern_distance(re.compile(r'\n'), raw_text1, raw_text2, 0)
    evaluate = np.array([space_distance, indent_distance, newline_distance])
    ED = indent_distance + space_distance + newline_distance
    Total1 = space1 + indent1 + newline1
    Total2 = space2 + indent2 + newline2
    if Total1 > Total2:
        total = Total1
    else:
        total = Total2
    WPSR = 1 - (ED / total)
    #print(ED)
    #print(WPSR)

    return WPSR



 

  