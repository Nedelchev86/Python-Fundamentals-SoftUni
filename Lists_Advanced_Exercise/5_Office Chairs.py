number_of_rooms = int(input())
free_chairs = 0
enough_chairs = True

for i in range(number_of_rooms):
    chairs, visitors = input().split()
    chairs = len(chairs)
    visitors = int(visitors)
    if chairs < visitors:
        print(F"{visitors - chairs} more chairs needed in room {i+1}")
        enough_chairs = False
    else:
        free_chairs += chairs - visitors
if enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")
