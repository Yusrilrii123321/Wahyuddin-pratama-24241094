# operasi komparasi/perbandingan 

# perhatikan
"""
    hasi; dari operasi komparasi
    selalu bertipe data boolean
    (true/false)
"""
# >, <, >=, <=, ==, !=, is, dan is not

a = 4
b = 2 

# lebih dari > 
print("===lebih dari (>)")    
hasil = a > 3 # TRUE
print(a, ">", 3, "=", hasil)
hasil = b > 3 # FALSE
print(b, ">", 3, "=", hasil)
hasi = b > 2
print(b, ">", 2, "=", hasil)

# kurang dari <  
print("===lebih dari (<)")    
hasil = a < 3 # FALSE
print(a, "<", 3, "=", hasil)
hasil = b < 3 # TRUE
print(b, "<", 3, "=", hasil)
hasi = b < 2
print(b, "<", 2, "=", hasil)
 
# lebih dari sama dengan >=
print("===lebih dari (>=)")    
hasil = a >= 3 # TRUE
print(a, ">=", 3, "=", hasil)
hasil = b >= 3 # FALSE
print(b, ">=", 3, "=", hasil)
hasi = b >= 2
print(b, ">=", 2, "=", hasil)

# kurang dari sama dengan <=
print("===lebih dari (<=)")    
hasil = a <= 3 # FALSE
print(a, "<=", 3, "=", hasil)
hasil = b <= 3 # FALSE
print(b, "<=", 3, "=", hasil)
hasi = b <= 2
print(b, "<=", 2, "=", hasil)
     
 # sama sama dengan ==
print("===lebih dari (==)")    
hasil = a == 3 # FALSE
print(a, "==", 3, "=", hasil)
hasil = b == 3 # FALSE
print(b, "==", 3, "=", hasil)
hasi = b == 2
print(b, "==", 2, "=", hasil)

# tidak sama dengan !=
print("===lebih dari (!=)")    
hasil = a != 3 # TRUE
print(a, "!=", 3, "=", hasil)
hasil = b != 3 # TRUE
print(b, "!=", 3, "=", hasil)
hasi = b != 2
print(b, "!=", 2, "=", hasil)