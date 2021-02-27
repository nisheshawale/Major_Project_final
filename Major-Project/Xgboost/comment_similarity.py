import re
import sys
# from braces_similarity import longest_common_sequence

def splitted_lines(filename):
    with open(filename) as f:
        text = f.read()

    if filename[-2:] == '.c':
        single_line = '//'
        multi_line = '/*'
    elif filename[-3:] == '.py':
        single_line = '#'
        multi_line = ''

    temp = text.splitlines()
    for i in range(len(temp)):
        temp[i] = temp[i].lstrip()
    return (temp, single_line, multi_line)

def comment_format(text_splitted_lines, single_line, multi_line):
    string_parsed = ""

    for i in range(len(text_splitted_lines)):
        index_1 = text_splitted_lines[i].find(single_line)
        #print(index_1)
        if multi_line == '':
            index_2 = sys.maxsize
        else:
            index_2 = text_splitted_lines[i].find(multi_line)
        if (index_1 != -1) and (index_2 != -1):
            index = min(index_1, index_2)
        else:
            index = max(index_1, index_2)
        # if index != -1:
        #      print(index)
        if (index == -1) or (index == sys.maxsize):
            pass
        elif (text_splitted_lines[i][index] == single_line) or (text_splitted_lines[i][index:index + 2] == single_line):
            if index == 0:
                string_parsed += 'S1'
            else:
                string_parsed += 'S2'
        else:
            string_parsed += 'M3'

    return string_parsed

