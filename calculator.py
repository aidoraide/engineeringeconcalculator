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

def sub(allow_symbols):
    def f(match):
        match_args = match.group().strip('(').strip(')').split(',')
        pattern, i, N = match_args
        func, N = pattern2formula[pattern], int(N)
        if not allow_symbols:
            i = float(i)
        code = f'{func}({i}, {N})'
        return code
    return f

def sub_assume_multiplication(match):
    group = match.group()
    return group.replace('(', '*(').replace(')', ')*')

def parse_user_input(user_in, allow_symbols):
    evaluation = user_in
    evaluation = evaluation.replace(' ', '')   # no whitespace
    evaluation = evaluation.replace('^', '**') # regular exponents to Python exponents
    evaluation = re.sub(r'[0-9]+\(|\)[0-9]+', sub_assume_multiplication, evaluation) # 500(F/A, ...) -> 500 * (F/A, ...)
    for pattern, formula_func in pattern2formula.items():
        # (formula, float, int)
        match_regex = f'\({pattern},[0-9i]*\.?[0-9]*,[0-9]+\)'
        evaluation = re.sub(match_regex, sub(allow_symbols), evaluation)
    return evaluation


# Find where func == 0
def solve(func, lo=0, hi=1):
    # Swap the sign of function if not increasing
    if func(0.7) - func(0.6) < 0:
        return solve(lambda x: -func(x), lo, hi)
    
    # func is constantly increasing
    mid = (lo + hi) / 2
    fmid = func(mid)
    if abs(fmid) < 1e-8:
        return mid
    elif fmid < 0:
        return solve(func, mid, hi)
    else:
        return solve(func, lo, mid)


def evaluate_for_i(evaluation):
    def func(i):
        # Sets the value of i before eval
        return eval(evaluation)
    return func


def handle_simple_evaluation(user_in):
    try:
        if '=' in user_in:
            l, r = user_in.split('=')
            levaluation = parse_user_input(l, True)
            revaluation = parse_user_input(r, True)
            i = solve(evaluate_for_i(f'{revaluation} - ({levaluation})'))
            print(f'i = {i}')
            print(f'{user_in}, for i = {round(i, 2)}')
        else:
            evaluation = parse_user_input(user_in, False)
            value = eval(evaluation)
            print(value)
            print(user_in, '=', round(value, 2))
    except KeyboardInterrupt as e:
        exit()
    except SyntaxError as e:
        print(f'Error when evaluating "{evaluation}" as Python code')
    except NameError as e:
        print(f'Error when evaluating "{evaluation}" as Python code')
    except ValueError as e:
        print(f"Error when evaluating expression. An input of i was given for interest rate but the input was not an equation (input did not have an '=')")


user_in = ''
while not user_in.startswith('exit') and not user_in.startswith('quit'):
    try:
        user_in = input('\n$: ').strip()
        if not user_in:
            continue
        handle_simple_evaluation(user_in)
    except Exception as e:
        print(type(e).__name__)
        print(e)
        continue
