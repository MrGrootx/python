para=[]
print("Enter a Para : ")

while True:
   line = input()
   if line :
      para.append(line)
   else:
      break

output = ',\n'.join(para)
print(output)