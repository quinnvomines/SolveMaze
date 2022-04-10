str_input = 'FLFLFRFRFFRRFFLFLFRFRFLFLFFLFFRFLFRFRFRRFLFLFFFLFLF'
expected_output = 'RFLFFLFFRFRFFLFLF'
input = list(str_input)

def countForwardMoves(lst):
    count = 0
    for element in lst:
        if(element == 'F'):
            count += 1
        else:
            break
    return count

def removeN():
    global input
    input[:] = [x for x in input if x != 'N']

def replace_pattern1(index):
    global input
    #Check conditions
    if (input[index-num_forwd_deadend-1] == 'L' and
    input[index+num_forwd_deadend+2] == 'L' and input[index+num_forwd_deadend+3] == 'F'):
        for i in range(index-num_forwd_deadend-1, index+num_forwd_deadend+3):
            input[i] = 'N' #Replace

def replace_pattern2(index):
    global input
    #Check conditions
    if (input[index-num_forwd_deadend-1] == 'L'):
        for i in range(index-num_forwd_deadend-1, index+num_forwd_deadend+1):
            input[i] = 'N' #Replace
        input[index + num_forwd_deadend + 1] = 'R'

def replace_pattern3(index):
    global input
    #Check conditions
    if (input[index+num_forwd_deadend+2] == 'L'):
        for i in range(index-num_forwd_deadend, index+num_forwd_deadend+2):
            input[i] = 'N' #Replace
        input[index + num_forwd_deadend + 2] = 'R'

def replace_pattern4(index):
    global input
    #Check conditions
    if(input[index] == 'R' and input[index+1] == 'R'):
        #Replace
        input[index] = 'L'
        input[index+1] = 'L'

while(('').join(input).find('RR') != -1):
    for i in range(len(input)):
        if(i + 1 < len(input) and input[i] == 'R' and input[i + 1] == 'R'):
            #Count number of forwards before and after 180 turn
            count_before180 = countForwardMoves(input[0:i][::-1])
            count_after180 = countForwardMoves(input[(i+2):])
            num_forwd_deadend = min([count_before180, count_after180])

            #Stop if no forward moves after 180 turn
            if(num_forwd_deadend == 0):
                continue

            #Check pattern 1 and replace
            if(i-num_forwd_deadend-1 >= 0 and i+num_forwd_deadend+3 < len(input)):
                replace_pattern1(i)

            #Check pattern 2 and replace
            if(i-num_forwd_deadend-1 >= 0):
                replace_pattern2(i)

            #Check pattern 3 and replace
            if(i+num_forwd_deadend+2 < len(input)):
                replace_pattern3(i)

            #Check pattern 4 and replace
            replace_pattern4(i)
    removeN()

print("input: \t\t\t\t" + str_input)
print("output: \t\t\t" + ('').join(input))
print("output: \t\t\t" + ('').join(input).replace('N',''))
print("expected_output: \t" + expected_output)
if(('').join(input).replace('N','') == expected_output):
    print('match!')


