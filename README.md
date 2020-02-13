# Engineering Economics Calculator

How to use:
```
python3 calculator.py
```

You will be given a prompt. Enter an equation without variables (use defined values for `i` and `N`) and it will calculate the result as well as the result rounded to the nearest cent.

Examples
```
$: 500(P/A, 0.06, 10)
3680.0435257073514
500(P/A, 0.06, 10) = 3680.04

$: 20000(P/F, 0.09, 10) + 1000(P/A, 0.09, 40) + 5000(P/A, 0.09, 10) + 2000( (P/A, 0.09, 40) - (P/A, 0.09, 10) )
59973.26982710777
20000(P/F, 0.09, 10) + 1000(P/A, 0.09, 40) + 5000(P/A, 0.09, 10) + 2000( (P/A, 0.09, 40) - (P/A, 0.09, 10) ) = 59973.27
```

This calculator can also solve for i to find IRR
```
$: 0 = 2200(P/A, i, 15) + 6000(P/F, i, 15) - 9500
i = 0.22751940767673506
0 = 2200(P/A, i, 15) + 6000(P/F, i, 15) - 9500, for i = 0.23
```
