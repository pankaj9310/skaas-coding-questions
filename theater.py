import sys
def seatsInTheater(nCols, nRows, col, row):
  	return (nCols - col+1) * (nRows - row)
nCols,nRows,col,row = map(int,sys.stdin.readline().split())
print('Given input in formate of nCols nRows col row \n')
print seatsInTheater(nCols,nRows,col,row)

