c      A program to determine highest number in a file, lowest number in
c      a file, and the average value.
c      By Daniel Graham
c      9/28/2014

      integer function arraySize(x)
c     Input Params: A string < 100 chars that contains the array file.
c     Output: returns the size of the array in that file.
c     This function is useful for determining the total array size
c     one will be working with.
      Character(len = 100) x
      arraySize = 0
      open(44, File = x, Status = 'OLD')
      read(44, *) line
 10   if (line.NE.-1) then
        arraySize = arraySize + 1
        read(44,*) line
        goto 10
      endif
c     I know I shouldn't use goto, but my compiler does not support a 
c     while loop.
      close(44)
      return 
      end
      
      subroutine findMaxValue(maxLocation, maxValue, n, array)
      
c     Input Parameters: requires maxLocation and maxValue 
c     to be passed from the main
c     program, but they do not need to be initialized to a value.
c     Also, n is the size of the array and array is the array itself.
c     
c     Output: Changes maxLocation to be the location of the max value
c     in the array. Also changes maxValue to be the maximum value in the
c     array. No other parameters are changed. 

      integer n,array(*),maxLocation, maxValue
      maxValue = array(1)
      maxLocation = 1
      do 30 i = 2, n
        if(array(i).GT.maxValue) then
            maxValue = array(i)
            maxLocation = i
        endif
 30   continue
      return
      end
      
      subroutine findMinValue(minLocation, minValue, n, array)

c     Input Parameters: requires minLocation and minValue
c     to be passed from the main
c     program, but they do not need to be initialized to a value.
c     Also, n is the size of the array and array is the array itself.
c     
c     Output: Changes minLocation to be the location of the min value
c     in the array. Also changes minValue to be the minimum value in the
c     array. No other parameters are changed. 

      integer n, array(*), minLocation, minValue
      minValue = array(1)
      minLocation = 1
      do 40 i = 2, n
        if(array(i).LT.minValue) then
            minValue = array(i)
            minLocation = i
        endif
 40   continue
      return
      end
      
      real function average(n, array)
      
c     Input Params: Requires the size of the array, n, and the array 
c     as input.

c     Output: returns the average of the array values.

      integer n, array(*)
      real totalSum
      totalSum = array(1)
       do 50 i = 2, n
        totalSum = totalSum + array(i)
 50   continue
      average = totalSum / n
      return
      end
      
      
      subroutine inputArray(n, x, array)
c     Input Params: Takes, n, the size of the array, x, the name of the
c     array file path, and an array to fill from the file.

c     Output: Changes only the array to be filled with values from file.
c     Keeps the -1 at the end, in order to keep track of the end of the 
c     array.
      Character(len = 100) x
      integer n, array(*)
      open(54, File = x, Status = 'OLD')
      do 20 i = 1 , (n + 1)
          read(54, *) line
          array(i) = line
 20   continue
      close(54)
      return
      end
      

      
      program sortAndReturn
      
c     This is the main body of the program. It calls above subprograms
c     on the file test123.txt. If you wish to test another file,
c     change the string to the file path, as long as the string is < 100
c     chars.

c     Max array size is 100 integers.

      Character(100) inputFile
      Integer totalSize, arraySize, location, maxValue, minValue
      Integer newArray(100)
      real average
      inputFile = "test123.txt"
      
      totalSize = arraySize(inputFile)
      call inputArray(totalSize, inputFile, newArray)
      call findMaxValue(location, maxValue,totalSize, newArray)
      write (*,*) "The max value is:", maxValue
      write(*,*) "The location of the max is:", location
      call findMinValue (location, minValue, totalSize, newArray)
      write(*,*) "The min value is:", minValue
      write(*,*) "The location of the min is:", location
      write(*,*) "The average is:", average(totalSize, newArray)
      stop
      end
      
