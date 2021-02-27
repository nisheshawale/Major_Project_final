import pygments.token
import pygments.lexers

KLENGTH = 20     # length of each kgram
BASE = 101       # base for rolling hash generation
DIVISOR = 2**32  # divisor for rolling hash generation
WINDOWSIZE = 50 # window size for winnowing 

def tokenize(filename):
    file = open(filename, "r")
    text = file.read()
    file.close()
    lexer = pygments.lexers.guess_lexer_for_filename(filename, text)
    tokens = lexer.get_tokens(text)
    tokens = list(tokens)
    result = []
    lenT = len(tokens)
    count1 = 0    #tag to store corresponding position of each element in original code file
    count2 = 0    #tag to store position of each element in cleaned up code text
    # these tags are used to mark the plagiarized content in the original code files.
    for i in range(lenT):
        if tokens[i][0] == pygments.token.Name and not i == lenT - 1 and not tokens[i + 1][1] == '(':
            result.append(('N', count1, count2))  #all variable names as 'N'
            count2 += 1
        elif tokens[i][0] in pygments.token.Literal.String:
            result.append(('S', count1, count2))  #all strings as 'S'
            count2 += 1
        elif tokens[i][0] in pygments.token.Name.Function:
            result.append(('F', count1, count2))   #user defined function names as 'F'
            count2 += 1
        elif tokens[i][0] == pygments.token.Text or tokens[i][0] in pygments.token.Comment:
            pass   #whitespaces and comments ignored
        else:
            result.append((tokens[i][1], count1, count2))  
            #tuples in result-(each element e.g 'def', its position in original code file, position in cleaned up code/text) 
            count2 += len(tokens[i][1])
        count1 += len(tokens[i][1])
    #print(result)
    return result

def toText(arr):
    cleanText = ''.join(str(x[0]) for x in arr)
    #print(cleanText)
    return cleanText

def kgrams(text, k):
    tokenList = list(text)
    n = len(tokenList)
    kgrams = []
    for i in range(n - k + 1):
        kgram = ''.join(tokenList[i : i + k])
        #hv = hash(kgram)
        #kgrams.append((kgram, hv, i, i + k))  #k-gram, its hash value, starting and ending positions are stored
        #these help in marking the plagiarized content in the original code.
        kgrams.append(kgram)
    return kgrams

def rolling_hash(kgrams):
    hash_values = []
    first_kgram= kgrams[0]
    prev_hash_value = 0
    for i in range(0, KLENGTH):
        prev_hash_value += ord(first_kgram[i])*(BASE**(KLENGTH-1-i))
    
    prev_hash_value *= BASE
    hash_values.append(prev_hash_value % DIVISOR)
    prev_hash_value = prev_hash_value % DIVISOR
    for i in range(0, len(kgrams)-1):
        # Improvement on Rolling Hash | Each character potentially affect all of the hash's bit
        new_hash_value = ((prev_hash_value-ord(kgrams[i][0])*BASE**(KLENGTH))+\
                        ord(kgrams[(i+KLENGTH) % len(kgrams)][0]))*BASE
        prev_hash_value = new_hash_value
        prev_hash_value = prev_hash_value%DIVISOR
        hash_values.append(new_hash_value%DIVISOR)

    return hash_values

def jaccard_similarity(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return len(s1.intersection(s2)) / len(s1.union(s2))
    
def summary(filename1, filename2):
    token_1 = tokenize(filename1)
    text_1 = toText(token_1)
    k_grams_1 = kgrams(text_1, KLENGTH)
    first_code = rolling_hash(k_grams_1)
    token_2 = tokenize(filename2)
    text_2 = toText(token_2)
    k_grams_2 = kgrams(text_2, KLENGTH)
    second_code = rolling_hash(k_grams_2)
    return jaccard_similarity(first_code, second_code)



