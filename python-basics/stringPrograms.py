# String Reverse

name ="Akash Sai Vishal" 
print(name[::-1])

# Palindrome

text ="madam"

if text == text[::-1] :
    print("palindrome")
else:
    print("not palindrome")
 
#  3. Count Vowels   
count =0

for ch in name :
    if ch.lower() in "aeiou":
        count = count + 1;
print(count)

#  4. Count chars   

for ch in name :
    count =count +1 ;
    
    print (count)
