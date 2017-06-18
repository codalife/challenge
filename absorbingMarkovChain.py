# Stable matrix for an Absorbing Matrix

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

    allZeros = True
    for k in a[i]:
      if k != 0:
        allZeros = False

    if allZeros:
      zeroArrays.append( i )
    else:
      nonZeros.append( i )
  # insert terminal rows in front
  for z in range(len(zeroArrays)):
    newMatrix.append( numpy.zeros( size ))
    newMatrix[z][z] = 1
  # insert rest of the rows
  for r in range( len( nonZeros ) ):
    z += 1
    shift = z - nonZeros[r]
    newMatrix.append( shiftRow( a[ nonZeros[r]], shift ))
