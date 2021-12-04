# 1- Absloute:
#   C:\sys\ssys\inpy.txt
# 2- Relative:
# current pwd
#   input.txt
#   ./input.txt (linux) 
#   .\input.txt (windows)
#   ../A/input.txt

input_file_address = "./files/input.txt"
output_file_address = "./files/output.txt"
temp_file_addr = "./files/temp.txt"
break_line = "\n" # "\r\n"
tab = "\t"


# ascii, utf-8

str_a = "aydin"
str_b = b'aydin'
str_c = str_b.decode('utf-8')

# mode of opening
# r => reading access
# w => writing access (also reading access)
# b => binary :  rb, wb
# a => append 

# os  => import os


with open(temp_file_addr, "r") as file:
    names = file.readlines()


file = open(temp_file_addr, "w")
for name in names:
    file.write(name+"\n")
file.close()


p = "1,2,apple;koroush,moz"
# dilimeter 
p_splited = p.split(',')
p_replaced = p.replace('apple', '')

print(p_splited)
print(p_replaced)

