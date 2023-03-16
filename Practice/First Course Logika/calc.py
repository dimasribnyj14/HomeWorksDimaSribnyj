a=int(input("Пишите первое число."))
b=int(input('Пишите второе число.'))
pm=input("Плюс или минус (+ или -)?")
if pm == '+' or pm == 'plus' or pm == 'плюс' or pm == 'PLUS' or pm == 'ПЛЮС' or pm == 'Plus' or pm == 'Плюс':
    print(a+b)
    input("Скажи пока!")
elif pm == '-' or pm == 'minus' or pm == 'минус' or pm == 'Minus' or pm == 'Минус' or pm == 'MINUS' or pm == 'МИНУС':
    print(a-b)
    input("Скажи пока!")
else:
    print('Error: You tried to write other words which not looks like - and +, please, restart program.')
    input("Скажи пока!")