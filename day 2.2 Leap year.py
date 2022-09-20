n=int(input('enter Date:'))
if(n>0):
    if(n%4==0 or n%400==0):
        print ('Given year is a Leap Year')
    else:
        print ('Given year is Non Leap Year')
        if n%4!=0:
            n-= int(n%4)
        print("Leap Year:",n)
else:
    print ('not a valid year')
