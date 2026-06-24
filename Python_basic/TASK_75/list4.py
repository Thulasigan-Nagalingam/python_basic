subject=["Mathematics","Tamil","English","Science","IT"]
print("Old list:",subject)   

for x in range(5):
    subject[x]=input(f"Enter new subject{x+1}: ")
    x+=1
    
print("Updated list:",subject)