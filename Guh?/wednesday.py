invite=['Walid','Hunter','Denilson','Sagan']
print(invite)
invite.append('Sam')
invite.append('Justin')
invite.append('Ben')
print(invite)
invite.pop(0)
print(invite)
invite.remove("Denilson")
print(invite)
extras=['friends','party','discord']
print(extras)
for i in range(len(extras)):
    add=extras[i]
    invite.append(add)
print(invite)
