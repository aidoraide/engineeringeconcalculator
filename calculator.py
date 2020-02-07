import re

def FP(i, N):
    return (1+i)**N

def PF(i, N):
    return 1 / FP(i, N)

def AF(i, N):
    return i / ((i+1)**N - 1)

def FA(i, N):
    return 1 / AF(i, N)

def AP(i, N):
    return i*(i+1)**N / ((i+1)**N - 1)

def PA(i, N):
    return 1 / AP(i, N)

pattern2formula = {
    r'F/P': 'FP',
    r'P/F': 'PF',
    r'A/F': 'AF',
    r'F/A': 'FA',
    r'A/P': 'AP',
    r'P/A': 'PA',
}

def sub(match):
    match_args = match.group().strip('(').strip(')').split(',')
    pattern, i, N = match_args
    func, i, N = pattern2formula[pattern], float(i), int(N)
    code = f'{func}({i}, {N})'
    return code

def sub_assume_multiplication(match):
    group = match.group()
    return group.replace('(', '*(').replace(')', ')*')

def parse_user_input(user_in):
    evaluation = user_in
    evaluation = evaluation.replace(' ', '')   # no whitespace
    evaluation = evaluation.replace('^', '**') # regular exponents to Python exponents
    evaluation = re.sub(r'[0-9]+\(|\)[0-9]+', sub_assume_multiplication, evaluation) # 500(F/A, ...) -> 500 * (F/A, ...)
    for pattern, formula_func in pattern2formula.items():
        # (formula, float, int)
        match_regex = f'\({pattern},[0-9]*\.?[0-9]*,[0-9]+\)'
        evaluation = re.sub(match_regex, sub, evaluation)
    return evaluation

def handle_simple_evaluation(user_in):
    try:
        evaluation = parse_user_input(user_in)
        value = eval(evaluation)
        print(value)
        print(user_in, '=', round(value, 2))
    except KeyboardInterrupt as e:
        exit()
    except SyntaxError as e:
        print(f'Error when evaluating "{evaluation}" as Python code')
    except NameError as e:
        print(f'Error when evaluating "{evaluation}" as Python code')


user_in = ''
while not user_in.startswith('exit') and not user_in.startswith('quit'):
    try:
        user_in = input('\n$: ')
        handle_simple_evaluation(user_in)
    except Exception as e:
        print(type(e).__name__)
        print(e)
        continue
