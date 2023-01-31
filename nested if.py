email="m.j.d.c3373@gmail.com"
pwd=123456
otp=5467
cemail=input("enter the email:")
cpwd=int(input("enter the pwd:"))
sotp=int(input("enter the otp"))
if(email==cemail and pwd==cpwd):
    print("login successful")
elif(email!=cemail and pwd==cpwd):
    print("login unsuccessful")
elif(email==cemail and pwd!=cpwd):
    print("login unsuccessful due to password")
elif(email==cemail and pwd==cpwd and otp==sotp):
    print("order is placed")
elif(email==cemail and pwd==cpwd and otp!=sotp):
    print("order is not placed")
else:
    print("total order cancelled")





















    
