s=raw_input()
n=s.lower()
h=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

if all(i in n for i in h):
    print("yes")
else:
    print("no")
