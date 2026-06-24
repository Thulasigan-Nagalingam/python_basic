subject=["Maths","Tamil","Maths","English","IT"]

subject.insert(2,"Geography")
subject.append("Economics")
subject.extend(["Music","Art"])

subject.pop(1)
subject.pop()

index=subject.index("English")
count=subject.count("Maths")

print(f"Index of English: {index}")
print(f"Maths occurs: {count} times")
print(f"Final List: {subject}")
    
