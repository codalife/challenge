import fractions

brr = [
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]

def createMatrix(rowCount, colCount, dataList):
    mat = []
    for i in range(rowCount):
        rowList = []
        for j in range(colCount):
            rowList.append(dataList)
        mat.append(rowList)

    return mat

def transposeMatrix(m):
    t = []
    for r in range(len(m)):
        tRow = []
        for c in range(len(m[r])):
            if c == r:
                tRow.append(m[r][c])
            else:
                tRow.append(m[c][r])
        t.append(tRow)
    return t

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

def muliply(X, Y):
  if Y:
    toReturn = createMatrix(len(X), len(Y[0]), 0)
  else:
    toReturn = createMatrix(len(X), 0, 0)
  for i in range(len(X)):
     # iterate through columns of Y
     for j in range(len(Y[0])):
         # iterate through rows of Y
         for k in range(len(Y)):
             toReturn[i][j] += X[i][k] * Y[k][j]

  return toReturn

def shiftRow(sub, steps):
  sub = list(reversed( sub ))
  sub[:steps] = sub[:steps][::-1]
  sub[steps:] = sub[steps:][::-1]

  return sub

def answer(a):

#   if a != brr:
#       return []

  size = len(a)

  newMatrix = []
  zeroArrays = []
  nonZeros = []

  for i in range( size ):
    allZeros = 0
    for k in range ( len(a[i])):
      if a[i][k] != 0:
        allZeros += a[i][k]

    if not allZeros:
      zeroArrays.append( i )
    else:
      nonZeros.append( {'index': i, 'denominator': allZeros} )

  # insert terminal rows in front
  for z in range(len(zeroArrays)):
    newMatrix.append( createMatrix( size, size, 0 ))
    newMatrix[z][z] = 1

  terminalEnd = z + 1

  # insert rest of the rows
  for r in nonZeros:
    for num in range( len(a[r['index']])):
      a[r['index']][num] = fractions.Fraction( a[r['index']][num], r['denominator'])
      r['denominator']
    z += 1
    shift = z - r['index']
    newMatrix.append( shiftRow( a[r['index']], shift ))

  I =  createMatrix( len(nonZeros), len(nonZeros), fractions.Fraction(0, 1) )

  for row in range(len(I)):
    I[row][row] = fractions.Fraction(1, 1)

  Q = [row[terminalEnd:] for row in newMatrix[terminalEnd:]]

  IminusQ = createMatrix( len(Q), len(Q), fractions.Fraction(0, 1) )

  for rr in range(len(Q)):
    for cc in range(len(Q)):
      IminusQ[rr][cc] = I[rr][cc] - Q[rr][cc]

  F = getMatrixInverse(IminusQ)

  R = [row[:terminalEnd] for row in newMatrix[terminalEnd:]]

  res = muliply( F, R )

  if res:
     res = res[0]

  denominator = 1

  final = []

  for n in res:
    if n.denominator > denominator:
      denominator = n.denominator

  for x in res:
    final.append( denominator/x.denominator * x.numerator )
  final.append(denominator)

  return final
