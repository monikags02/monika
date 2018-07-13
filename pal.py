try:
	n=int(input())
	temp=n
	reverse=0
	while(temp!=0):
		rem=temp%10
		reverse=reverse*10+rem
		temp=int(temp/10)
	if reverse==n:
		print('palindrome')
	else :
		print('not palindrome')
except:
	print('invalid')
