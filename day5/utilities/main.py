from file_operations import read_file,write_file
from transformations import clean_data

read_file("output.csv")

data = [" Rahul  " ,"           Akash" ,"              priya              "]

result = clean_data(data)
print(result)
