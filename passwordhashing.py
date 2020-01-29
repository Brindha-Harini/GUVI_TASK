import hashlib
pawd=input("Enter password")
p=hashlib.new('md4').hexdigest()
print(p)
