userName  = input("Enter employee name");
salary  = int(input("Enter your salary"));
experience = float(input("enter your experience"));

print (f"Hi {userName} welcome to quantela technolgies . Your monthly take home  {salary }  and your over all experience {experience}");

if salary>= 50000:
    print(f"High salary {salary}" )
else :
    print(f"Average salary")
    
if experience >=5 :
    print("senior employee")
else :
    print("junior employee")
    

