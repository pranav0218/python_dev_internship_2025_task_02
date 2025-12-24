name=input("Enter student name:")
list=[]
for i in range(5):
    list.append(int(input(f"Enter student marks for subject {i}:")))
print(list)


def total_marks(list,total):
    for i in list:
        total+=i
    return total
def percent(total):
    print(total)
    percentage=float((total/500)*100)
    return percentage

def compare(percentage):
    if percentage>75:
        print("Distinction")
    elif percentage>60 and percentage<74:
        print("First Class")
    elif percentage>50 and percentage<59:
        print("Second Class")
    else:
        print("Fail")

total=total_marks(list,0)
print(total)
percentage=percent(total)
print(percentage)
compare(percentage)
