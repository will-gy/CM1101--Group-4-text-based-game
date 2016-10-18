x =input (":\n")
k = x.replace(" ", "")
pos = 0
text = list(k)
z = 0
length = len(text)
pasw = int(input("enter pass:\n"))


crypt = ""
aph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
while pos < length:
 while True:
  try:
      new_position = aph.index(text[pos]) - pasw

  except:
         z=0
         continue
  break
 if new_position >= 26:
    new_position = new_position - 26
 text[pos]=aph[new_position]
 crypt = crypt + text[pos]
 pos = pos +1
 z=z+1

print (crypt)