from colorama import *
init()

print (Back.GREEN + 'Hi there, welcome BMI calculation sofware!')
print (Back.CYAN)

weight = float(input('What`s your weight ?: '))
height = float(input('And what`s your height?: '))

height = height / 100

BMI = weight / height**2
BMI = round(BMI)

print (Back.RESET + '\nYour current BMI is ' + str(BMI))

if (BMI >= 12) and (BMI <= 18) :
	print (Back.Blue + 'Insufficient body weight\n', end = '')

if (BMI >= 19) and (BMI <= 24) :
	print (Back.GREEN + 'Your weight is normal\n', end = '')

if (BMI >= 25) and (BMI <= 29) :
	print (Back.YELLOW + 'Excess body weight\n', end = '')

if (BMI >= 30) and (BMI <= 50):
	print (Back.RED + 'Obesity of the 1, 2 degree\n', end = '')

print (Style.RESET_ALL)

print ('Pragramm is finished!')