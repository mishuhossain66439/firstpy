Result = []
while True:
	print('Type "A" or "a" for Add')
	print('Type "B" or "b" for Sub')
	print('Type "C" or "c" for Mult')
	print('Type "D" or "d" for Div')
	print('Type "E" or "e" for Exit')
	print('===========================')
	operator = input('Enter A Operator : ').lower()
	
	if operator == 'a':
		num1 = int(input('Enter First Number : '))
		num2 = int(input('Enter 2nd Number : '))
		cal = num1+num2
		print(f'{num1} + {num2} = {cal}')
		Result.append(cal)
		print('===========================')
	elif operator == 'b':
		num1 = int(input('Enter First Number : '))
		num2 = int(input('Enter 2nd Number : '))
		cal = num1-num2
		print(f'{num1} - {num2} = {cal}')
		Result.append(cal)
		print('===========================')
	elif operator == 'C':
		num1 = int(input('Enter First Number : '))
		num2 = int(input('Enter 2nd Number : '))
		cal = num1*num2
		print(f'{num1}*{num2} = {cal}')
		Result.append(cal)
		print('===========================')
	elif operator == 'd':
		num1 = int(input('Enter First Number : '))
		num2 = int(input('Enter 2nd Number : '))
		cal = num1/num2
		print(f'{num1}/{num2} = {cal}')
		Result.append(cal)
		print('===========================')
	elif operator == 'e':
		break
	else:
		print('invalid value')		
		print('===========================')		    	
print(Result)