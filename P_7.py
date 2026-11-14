#Q: Write a python program to check password strength

p=input("Enter password")
print("8+ characters:",len(p)>=8)
print("starts uppercase:",p[0].isupper())
print("Has Digit:",not p.isalpha())
print("Has Symbol:",not p.isalnum())
print("strong:", len(p)>=8 and p[0:1].isupper() and not p.isalnum())