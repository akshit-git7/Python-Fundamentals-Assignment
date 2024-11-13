i1 = int
i2 = int
f1 = float
f2 = float
s1 = str
s2 = str

""" Opreartions on the variables """
i1=15
i2= 4
print(f"The sum of {i1} and {i2} is {i1+i2}")

f1=2.53
f2=3.54
print(f"The sum of {f1} and {f2} is {f1+f2}")

s1="akshit "
s2="pokhrel"
print(s1+s2)


dict={
    "int":[i1, i2],
    "float":[f1,f2],
    "str":[s1,s2]
}

print("\nDictionary items:")
for data_type, values in dict.items():
    print(f"{data_type}: {values}")
