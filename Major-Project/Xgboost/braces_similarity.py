import re

def splitted_lines(filename):
    with open(filename) as f:
        text = f.read()

    temp = text.splitlines()
    for i in range(len(temp)):
        temp[i] = temp[i].lstrip()
    return temp


def braces_format(text_splitted_lines):
    string_parsed = ""

    for i in range(len(text_splitted_lines)):
        pattern = re.compile(r'[{}]')
        res = [i.start() for i in re.finditer(pattern, text_splitted_lines[i])] 
        #print(res)
        if len(res) == 0:
            continue
        for j in range(len(res)):
            if text_splitted_lines[i][res[j]] == '{':
                if res[j] == 0:
                    if len(text_splitted_lines[i]) == 1:
                        string_parsed += '{4'
                    else:
                        #print(text_splitted_lines[i])
                        string_parsed += '{1'
                elif res[j] == (len(text_splitted_lines[i]) - 1):
                    string_parsed += '{2'
                else:
                    string_parsed += '{3'
            else:
                if res[j] == 0:
                    if len(text_splitted_lines[i]) == 1:
                        string_parsed += '}4'
                    else:
                        string_parsed += '}1'
                elif res[j] == (len(text_splitted_lines[i]) - 1):
                    string_parsed += '}2'
                else:
                    string_parsed += '}3'      

    return string_parsed      

def longest_common_sequence(string_1, string_2):
    length = 0
    l = 0
    m = len(string_1) // 2
    for i in range(m):
        for j in range(m - i - length):
            start = 2 * i
            end = (2 * j) + 2 + 2 * i + 2 * length
            #print(start, end)
            if string_2.find(string_1[start:end]) == -1:
                break

            l = (end - start) // 2
            # print('l', l)
        length = l 
        # print('length', length)
    #return length

    #c_L = longest_common_sequence(braces_notation_1, braces_notation_2)
    #print("Longest common subsequence of braces similarity:", length)
    c_1 = len(string_1) / 2
    c_2 = len(string_2) / 2
    #print(c_1, c_2)
    if (c_1 == 0) or (c_2 == 0):
        return 0
    else:
        return (2 * length / (c_1 + c_2))







