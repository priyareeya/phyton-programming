x=int(raw_input())
if(x%4==0 and x%100==0 and x%400==0):
	print("leap year")
else:
	print("not a leap year")
