import braces_similarity as bs, comment_similarity as cs
import WPSR as ws, karp as ss
import total_no_of_unused as tnu
import math

def encapsulate_all(filename1, filename2):
    # braces_notation_1 = bs.braces_format(bs.splitted_lines(filename1))
    # print('Braces notation 1:', braces_notation_1)
    # braces_notation_2 = bs.braces_format(bs.splitted_lines(filename2))
    # print('Braces notation 2:', braces_notation_2)
    if filename1[-3:] == '.py':
        bsr = 0
    else:
        bsr = bs.longest_common_sequence(bs.braces_format(bs.splitted_lines(filename1)), bs.braces_format(bs.splitted_lines(filename2)))
    # print("BSR:", bsr)

    processed_1, s_1, m_1 = cs.splitted_lines(filename1)
    # notation_1 = cs.comment_format(processed_1, s_1, m_1)
    processed_2, s_2, m_2 = cs.splitted_lines(filename2)
    # notation_2 = cs.comment_format(processed_2, s_2, m_2)
    # print('Comment notation 1:', notation_1)
    # print('Comment notation 2:', notation_2)
    csr = bs.longest_common_sequence(cs.comment_format(processed_1, s_1, m_1), cs.comment_format(processed_2, s_2, m_2))
    
    wpsr = ws.edit_distance(filename1, filename2)

    assr = (bsr + wpsr + csr)

    sim_score = ss.summary(filename1, filename2)

    com_lines = tnu.common_lines(filename1, filename2)

    u_var1, u_func1, _ = tnu.unused_number(filename1)
    u_var2, u_func2, _ = tnu.unused_number(filename2)
    u_var = u_var1 + u_var2
    u_func = u_func1 + u_func2

    cpm_value = cpmspc(filename1, filename2, sim_score)

    return (sim_score, assr, cpm_value, com_lines, u_var, u_func)


def cpmspc(filename1, filename2, sim_value):
    similarity_threshold = 0.4
    cpms = 1
    cpmspc = 0
    if sim_value < similarity_threshold:
        cpms = 0
    cpmsp = abs(sim_value - similarity_threshold) / similarity_threshold
    if cpms == 0:
        if (0.5 < cpmsp) and (cpmsp <= 1):
            cpmspc = 1
        elif (0.2 < cpmsp) and (cpmsp <= 0.5):
            cpmspc = 2
        else:
            cpmspc = 3
    else:
        if cpmsp <= 0.2:
            cpmspc = 4
        elif (0.2 < cpmsp) and (cpmsp <= 0.5):
            cpmspc = 5
        else:
            cpmspc = 6

    return cpmspc

#print(encapsulate_all('a1.c', 'a2.c'))