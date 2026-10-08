import random
uppercase=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowercase=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','()','_','-',':',';',',','<','>','.','?','/','|','\\','+']
print("1-WEAK PASSWORD","\n","2-STRONG PASSWORD")
password=int(input("Enter you choice of password "))
a=set("")
if password==1 :
    n=random.randint(2,10)
    if n<2:
        a=uppercase[::n]+lowercase[::n]+numbers[::n]
        a="".join(a)
        print(a)
    elif n==6:
        a=uppercase[::n]+lowercase[::n]+symbols[::n]
        a="".join(a)
        print(a)
    elif n==2:
        a=lowercase[::n]+uppercase[::n]+symbols[::n]
        a="".join(a)
        print(a)
    elif n==3:
        a=lowercase[::n]+uppercase[::n]+numbers[::n]
        a="".join(a)
        print(a)
    elif n==4:
        a=numbers[::n]+uppercase[::n]+symbols[::n]
        a="".join(a)
        print(a)
    elif n==5:
        a=numbers[::n]+lowercase[::n]+symbols[::n]
        a="".join(a)
        print(a)
    elif n==6:
        a=symbols[::n]+uppercase[::n]+symbols[::n]
        a="".join(a)
        print(a)
    elif n==7:
        a=symbols[::n]+lowercase[::n]+symbols[::n]
        a="".join(a)
        print(a)
    else:
        a=lowercase[::n-2]+uppercase[::n+2]+symbols[::n]
        a="".join(a)
        print(a)
if password==2:
    n=random.randint(1,10)
    if n<2:
        a=uppercase[::n]+lowercase[::n]+numbers[::n]+symbols[::n]
        a="".join(a)
        print(a)
    elif n==6:
        a=uppercase[::n]+lowercase[::n]+symbols[::n]+symbols[::n]
        a="".join(a)
        print(a)
    elif n==2:
        a=lowercase[::n]+uppercase[::n]+symbols[::n]+numbers[::n]
        a="".join(a)
        print(a)
    elif n==3:
        a=lowercase[::n]+lowercase[::n]+uppercase[::n]+numbers[::n]+symbols[::n]
        a="".join(a)
        print(a)
    elif n==4:
        a=numbers[::n]+uppercase[::n]+symbols[::n]+lowercase[::n]
        a="".join(a)
        print(a)
    elif n==5:
        a=numbers[::n]+lowercase[::n]+symbols[::n]+uppercase[::n]
        a="".join(a)
        print(a)
    elif n==6:
        a=symbols[::n]+uppercase[::n]+symbols[::n]+lowercase[::n]
        a="".join(a)
        print(a)
    elif n==7:
        a=symbols[::n]+lowercase[::n]+symbols[::n]+uppercase[::n]
        a="".join(a)
        print(a)
    else:
        a=lowercase[::n-2]+uppercase[::n+2]+symbols[::n]+numbers[::n]
        a="".join(a)
        print(a)
if password!=1 and password!=2:
    print("Invalid number")
if len(a)>=10:
    print("The generated password is valid")
else:
    print("The generated password is invalid",
              "Try entering again")
n1=n2=n3=n4=0
for i in  a :
    if i in uppercase:
        n1+=1
    elif i in lowercase:
        n2+=1
    elif i in numbers:
        n3+=1
    else:
        n4+=1
if n1 and n2 and n3 and n4>1:
    print("The generated password is a strong password")
else:
    print("The generated password is a weak password")
