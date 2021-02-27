import subprocess


def unused_number(name_of_file):
    index = 1
    shell_value = False
    command = ['cppcheck', '--enable=all', name_of_file]

    if name_of_file[-3:] == '.py':
        index = 0
        shell_value = True
        command = "vulture " + name_of_file

    p = subprocess.Popen(command, shell=shell_value, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[index]
    #print(str(p).splitlines("\n"))

    # name_of_file = "a1.c"
    # p = subprocess.Popen(['cppcheck', '--enable=all', 'a1.c'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[1]

    unused_vars = 0
    unused_funcs = 0
    unused_imports = 0
    for line in p.split(b"\n"):
        decoded_line = line.decode().lower()
        print(decoded_line)
        if decoded_line.find('variable') > 0:
            unused_vars += 1
        elif decoded_line.find('function') > 0:
            unused_funcs += 1
        elif decoded_line.find('import') > 0:
            unused_imports += 1

    return (unused_vars, unused_funcs, unused_imports)


def common_lines(filename1, filename2):
    # index = 0
    # shell_value = True
    # command = "grep -Fxf {} {}".format(filename1, filename2) 
    # #command = "comm -12 <(sort {}) <(sort {})".format(filename1, filename2)
    # print(command) 
    count = 0

    # p = subprocess.Popen(command, shell=shell_value, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[index]
    # #return len(p.split(b"\n"))
    # return p.split(b"\n")

    file1 = set(line.strip() for line in open(filename1))
    file2 = set(line.strip() for line in open(filename2))

    for line in file1 & file2:
        if line:
            #print(line)
            count += 1
    return count




#print(unused_number('a1.c'))
#print(common_lines('test1.py', 'test2.py'))

