distribution = [int(x) for x in input().split(", ")]
minimum = int(input())

for i in range(len(distribution)):
    maximun = int(max(distribution))
    if maximun >= minimum:
        if distribution[i] < minimum:
            diference =  minimum - distribution[i]
            distribution[i] = minimum
            idx = distribution.index(maximun)
            distribution[idx] -= diference
            if distribution[idx] < minimum:
                print("No equal distribution possible")
                exit()

    else:
        print("No equal distribution possible")
        break
else:
    print(distribution)
