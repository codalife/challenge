def answer(l):
    res = [0]
    dic = {}
    helper = []

    for n in range(len(l)):
      dic[l[n]] = n
      helper.append([])

    for i in range(len(l)-1):
      for j in range(i+1, len(l), 1):
        if l[j] % l[i] == 0:
          helper[i].append(j)

    def recursiveCount(arr):
      for s in arr:
        res[0] += len(helper[s])

    for p in helper:
      recursiveCount(p)

    return res[0]
