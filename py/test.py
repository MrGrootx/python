 
D={101: "Peter",102:"Richard",103: "Firoza",104:"Parvathi"}
val = input('Enter Name : ')
found = 0
for k in D:
    if val.lower() == D[k].lower():
      print("value found at key : ",k)
      found = 1
    elif found == 0:
      print("Value not found")

