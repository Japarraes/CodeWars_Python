def pick_peaks(arr):

    res = { "peaks":[], "pos":[] }

    position = 0
    value = 0
    meseta = False

    for i in range(1, len(arr)-1):
        
        arr2 = arr[i-1:i+2]
        if (arr2[0] < arr2[1]) and (arr2[1] > arr2[2]):
            res["peaks"].append(arr2[1])
            res["pos"].append(i)
            continue

        if (arr2[0] < arr2[1]) and (arr2[1] == arr2[2]):
            position = i
            value = arr2[1]
            meseta = True

        if (arr2[0] <= arr2[1]) and (arr2[1] > arr2[2]):
            if meseta:
                res["peaks"].append(value)
                res["pos"].append(position)

    return res