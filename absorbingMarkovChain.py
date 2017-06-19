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

def shiftRow(sub, steps):
  sub = list(reversed( sub ))
  sub[:steps] = sub[:steps][::-1]
  sub[steps:] = sub[steps:][::-1]

  return sub

def answer(a):

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
    newMatrix.append( numpy.zeros( size ))
    newMatrix[z][z] = 1

  terminalEnd = z + 1

  # insert rest of the rows
  for r in nonZeros:
    # print (r['index'], r['denominator'])
    for num in range( len(a[r['index']])):
      a[r['index']][num] = Fraction( a[r['index']][num], r['denominator'])
      r['denominator']
    z += 1
    shift = z - r['index']
    newMatrix.append( shiftRow( a[r['index']], shift ))


  I = numpy.identity( len(nonZeros), dtype= Fraction )

  Q = [row[terminalEnd:] for row in newMatrix[terminalEnd:]]


  IminusQ = numpy.matrix(I - Q)
  # print Q
  # print IminusQ
  F = getMatrixInverse(IminusQ.tolist())

  R = [row[:4] for row in newMatrix[4:]]

  res = ( numpy.matrix(F)*R ).tolist()[0]

  return res
