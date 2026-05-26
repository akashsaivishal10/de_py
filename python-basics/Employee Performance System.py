name = input("Enter Employee name")
dept = input("Enter Department name")
salary = float(input("Enter a salary"))
rating = int(input("Enter your perfromance rating"))
year_salary = salary *12

if rating < 1 or rating > 5:
    print("Invalid Rating")
elif rating >=4 :
    print(f"your rating {rating} performance is excellent")
elif rating == 3 :
    print(f"your rating {rating} performance is good")
elif rating <= 2:
    print(f"your rating is {rating} needs improve")
else :
    print("your performance is very bad")
    
    
print(f"Hii {name} your working department is {dept} and your rating is {rating} and your yearly {year_salary}")
    