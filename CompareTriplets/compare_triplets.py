def compareTriplets(ar1, ar2):
    arSizeMax = 3
    i = 0
    ar1Points = 0
    ar2Points = 0

    validateTriplet(ar1)
    validateTriplet(ar2)

    while i < arSizeMax :
        if ar1[i] > ar2[i]:
            ar1Points += 1
        else:
            
        
def validateTriplet(ar):
    for x in triplet:
        if x < 1 or x > 100:
            print(f'The following tripplet has invalid parameters: {ar}')
            return 0

