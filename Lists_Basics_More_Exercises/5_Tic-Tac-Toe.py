first = input().split()
second = input().split()
third = input().split()

if first[0] == "1" and first[1] == "1" and first[2] =="1":
    print("First player won")
elif second[0] == "1" and second[1] == "1" and second[2] =="1":
    print("First player won")
elif third[0] == "1" and third[1] == "1" and third[2] == "1":
    print("First player won")
elif first[0] == "1" and second[0] == "1" and third[0] == "1":
    print("First player won")
elif first[1] == "1" and second[1] == "1" and third[1] == "1":
    print("First player won")
elif first[2] == "1" and second[2] == "1" and third[2] == "1":
    print("First player won")
elif first[0] == "1" and second[1] == "1" and third[2] == "1":
    print("First player won")
elif first[2] == "1" and second[1] == "1" and third[0] == "1":
    print("First player won")
elif first[0] == "2" and first[1] == "2" and first[2] =="2":
    print("Second player won")
elif second[0] == "2" and second[1] == "2" and second[2] =="2":
    print("Second player won")
elif third[0] == "2" and third[1] == "2" and third[2] == "2":
    print("Second player won")
elif first[0] == "2" and second[0] == "2" and third[0] == "2":
    print("Second player won")
elif first[1] == "2" and second[1] == "2" and third[1] == "2":
    print("Second player won")
elif first[2] == "2" and second[2] == "2" and third[2] == "2":
    print("Second player won")
elif first[0] == "2" and second[1] == "2" and third[2] == "2":
    print("Second player won")
elif first[2] == "2" and second[1] == "2" and third[0] == "2":
    print("Second player won")
else:
    print("Draw!")