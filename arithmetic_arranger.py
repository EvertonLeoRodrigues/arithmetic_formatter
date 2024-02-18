import re

def arithmetic_arranger(problems, show_answer=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'



    top = ''
    bottom = ''
    lines = ''
    answers = ''
    

    for problem in problems:
        if re.search('[^0-9+\- ]', problem):
            if re.search('[/]', problem) or re.search('[*]', problem):
                return 'Error: Operator must be \'+\' or \'-\'.'
            return 'Error: Numbers must only contain digits.'
        
        value_1, operator, value_2 = problem.split()
        
        if len(value_1) > 4 or len(value_2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        max_leght = max(len(value_1), len(value_2)) + 2
        
        line_width = '-'*max_leght
        
            
        answer = int(value_1)+int(value_2) if operator=="+" else int(value_1)-int(value_2)
        
        if problem == problems[-1]:
            top += value_1.rjust(max_leght)
            bottom += operator + value_2.rjust(max_leght-1)
            lines += line_width 
            answers += str(answer).rjust(max_leght)
        else:
            top += value_1.rjust(max_leght)+ '    '
            bottom += operator + value_2.rjust(max_leght-1)+ '    '
            lines += line_width + '    '
            answers += str(answer).rjust(max_leght) + '    '
            
    arranged_problems = f'{top}\n{bottom}\n{lines}'
    
    if show_answer:
        arranged_problems += f'\n{answers}'
        return arranged_problems
    
    return arranged_problems
