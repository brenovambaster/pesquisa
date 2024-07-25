arrayA= ['a','b','c']
arrayB= ['d','e','f']

for i in range(0, len(arrayA)):
    print(arrayA[i]+":")
    for j in range(i+1, len(arrayB)-1):
        print(arrayB[j])

    print(",")