even = {'0', '2', '4', '6', '8'}

def addOne(s):
    arr = list(s)

    for i in range (len(arr)):
        arr[i] = int(arr[i])

    carryover = 1
    runner = len(arr)-1

    while( carryover and runner > -1):
        if arr[runner] != 9:
            arr[runner] += 1
            carryover = 0
        else:
            arr[runner] = 0

        runner -= 1

    r = ''
    for x in arr:
        r += str(x)
    if(carryover):
        r = '1' + r

    return r

def removeOne(s):
    arr = list(s)

    for i in range (len(arr)):
        arr[i] = int(arr[i])

    carryover = 1
    runner = len(arr)-1

    while( carryover and runner > -1):
        if arr[runner] != 0:
            arr[runner] -= 1
            carryover = 0
        else:
            arr[runner] = 9

        runner -= 1

    if arr[0] == 0:
        del arr[0]

    return ''.join( str(x) for x in arr )

def divisionByTwo(s):
    s = s[::-1]
    arr = list(s)

    for i in range (len(arr)):
        arr[i] = int(arr[i])

    ten = 0

    for n in range( len(arr)-1, -1, -1 ):
        if arr[n] == 1:
            ten = 1
            arr[n] = 0
        elif arr[n] % 2 != 0:
            arr[n] = (arr[n] + ten*10 -1)/2
            ten = 1
        else:
            arr[n] = (arr[n]+ 10*ten)/2
            ten = 0

        if( arr[len(arr)-1] == 0):
            arr.pop()

    arr[::-1]
    r = ''

    for x in arr:
        r += str(x)
    return r

res = {}
res['1'] = 0

def answer(n):
    # print(n)

    global res

    if n in res:
        return res[n]

    steps = 0

    if n[len(n)-1] in even:
        steps = answer( divisionByTwo(n) )
    else:
      # print("See odd number ", n)
      steps = min( answer(addOne(n)), answer(removeOne(n)))

    res[n] = steps+1
    return steps + 1

print( answer("15") )
