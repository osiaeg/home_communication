#BMI
from termcolor import colored
from colorama  import *
init()


w = int(input('Введите массу тела в килограммах = '))
h = int(input('Введите рост в метрах = '))

BMI = w / (h*2)

if (BMI >= 12) and (BMI <= 18) :
	print (colored('У вас {} BMI в норме'.format(BMI) ,'black', 'on_blue'))

if (BMI >= 19) and (BMI <= 24) :
	print (colored('У вас {} BMI в норме'.format(BMI) ,'black', 'on_green'))

if (BMI >= 25) and (BMI <= 29) :
	print (colored('У вас {} BMI в норме'.format(BMI) ,'black', 'on_yellow'))

if (BMI >= 26) and (BMI <= 50):
	print (colored('У вас {} BMI в норме'.format(BMI) ,'black', 'on_red'))		 

