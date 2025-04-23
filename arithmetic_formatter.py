def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return 'Error: Too many problems.'

    line_1 = ''
    line_2 = ''
    line_3 = ''
    if show_answers:
        line_4 = ''

    for n in problems:
        for i in n:
            if i == '*':
                return "Error: Operator must be '+' or '-'."
            elif i == '/':
                return "Error: Operator must be '+' or '-'."

    
    
    for n in problems:

        first_line = '  '
        first_number = ''

        for i in n:
            if i.isdigit():
                first_number += i
            elif len(first_number) > 4:
                return "Error: Numbers cannot be more than four digits."
            elif i == ' ':
                break
            else:
                return "Error: Numbers must only contain digits."

        second_line = n[len(first_number) + 1] + ' '
        second_number = ''

        for i in n[len(first_number) + 3:]:
            if i.isdigit():
                second_number += i
                if len(second_number) > 4:
                    return "Error: Numbers cannot be more than four digits."
            else: 
                return "Error: Numbers must only contain digits."

        if show_answers:
            fourth_line = ''
            if n[len(first_number) + 1] == '+':
                fourth_number = int(first_number) + int(second_number)
            elif n[len(first_number) + 1] == '-':
                fourth_number = int(first_number) - int(second_number)

        for i in n:
            if len(first_number) < len(second_number):
                first_number = ' ' + first_number
            elif len(first_number) > len(second_number):
                second_number = ' ' + second_number
            
        first_line += first_number
        second_line += second_number

        if show_answers:
            for i in first_line:
                if len(str(fourth_number)) < len(first_line):
                    fourth_number = ' ' + str(fourth_number)

        third_line = ''

        if show_answers:
            fourth_line += str(fourth_number)

        for i in first_line:
            third_line += '-'

        if n != problems[-1]:
            line_1 += first_line + '    '
            line_2 += second_line + '    '
            line_3 += third_line + '    '
            if show_answers:
                line_4 += fourth_line + '    '
        else:
            line_1 += first_line
            line_2 += second_line
            line_3 += third_line
            if show_answers:
                line_4 += fourth_line

    if show_answers:
        print(line_1 + '\n' + line_2 + '\n' + line_3 + '\n' + line_4)
        return line_1 + '\n' + line_2 + '\n' + line_3 + '\n' + line_4
    else:
        print(line_1 + '\n' + line_2 + '\n' + line_3)
        return line_1 + '\n' + line_2 + '\n' + line_3

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
