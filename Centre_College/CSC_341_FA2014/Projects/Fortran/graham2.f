c A program to implement Radix sort in Fortran 77
c This was done for CSC 341.
c Sorts the numbers in file "data.txt"
c By Daniel Graham
c version 1.0 9/28/2014

      subroutine enqueue(queueEndIndex, queue, item, queueSize)
      
c     Input Params: Takes the queue as an input. The queue must have
c     < 100 items already on it. 
c     It also takes the index as input, so it does not have to recopy 
c     The array each time.
c     It also takes the item to enqueue. queueEndIndex is first availabl
c     e opening.

c     Output: increments the queue end index by one and if the index is 
c      at 100 already, returns it to 1. Also updates the queue itself.

c     Other condition: If the queue is full, indicated by a non negative
c     int, the routine prints an error. It goes to 101 so it can always
c     store at least one -1 value. 

      integer queueEndIndex, queue(*), item, queueSize
      
      if(queue(queueEndIndex).NE.-1) then
        write(*,*) "Queue Full!"
      else
        queue(queueEndIndex) = item
        queueSize = queueSize + 1
        if(queueEndIndex.GE.101) then
            queueEndIndex = 1
        else
            queueEndIndex = queueEndIndex + 1
        endif
      endif
      
      return
      end
      
      integer function dequeue(queueStartIndex, queue, queueSize)
c     This is a function because it returns the dequeued item.
c
c     Input Params: The queueStartIndex and the queue as an array. 
c     Queue must have at least 1 item on it, or will return -1 and a 
c     message of error.

c     Output: Returns the dequeued integer and increments the start 
c     index. Also removes the item from the queue.

      integer queueStartIndex, queue(*), queueSize
      
      if(queue(queueStartIndex).EQ.-1) then
        write(*,*) "No Items On Queue"
        dequeue = -1
      else
        dequeue = queue(queueStartIndex)
        queue(queueStartIndex) = -1
        queueSize = queueSize - 1
        if(queueStartIndex.GE.101) then
            queueStartIndex = 1
        else
            queueStartIndex = queueStartIndex + 1
        endif
      endif
      return
      end
      
      subroutine inputArray(n, x, array)
c     Taken from graham1.f For full documentation, see there.
      Character(len = 100) x
      integer n, array(*)
      open(54, File = x, Status = 'OLD')
      do 20 i = 1 , n
          read(54, *) line
          array(i) = line
 20   continue
      close(54)
      return
      end
      
      subroutine initializeQueue(queue)
      integer queue(*)
      do 60 i = 1, 101
        queue(i) = -1
 60   continue
      return
      end
      
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
      
      subroutine oneSort(m, queue, queueStartIndex, queueEndIndex, 
     + queueSize)
c     Input Params: The queue to be sorted, and m, which digit to sort.
c     example m is 1000 to sort by thousands place. 
c     Output: returns the queue sorted by the digit specified in m

      integer queueSort(101), queue(*)
      integer m, queueStartIndex, queueSortStartIndex
      integer queueEndIndex, queueSortEndIndex, queueSize
      integer queueSortSize, dequeueItem, modValue, dequeue, toMod
      call initializeQueue(queueSort)
      queueSortStartIndex = 1
      queueSortEndIndex = 1
      queueSortSize = 0
      do 70 i = 0, 9
        do 80 j = 1, (queueSize)
            dequeueItem = dequeue(queueStartIndex, queue, queueSize)
            toMod = dequeueItem / m
            modValue = mod(toMod,10)
            if(modValue.EQ.i) then
                call enqueue(queueSortEndIndex, queueSort, dequeueItem, 
     + queueSortSize)
            else
                call enqueue(queueEndIndex, queue, dequeueItem,
     + queueSize)
            endif
c      This if statement determines where in the sort queue items willgo
 80     continue
 70    continue
       do 90 i = 1, queueSortSize
        call enqueue(queueEndIndex, queue, 
     + dequeue(queueSortStartIndex, queueSort, queueSortSize),queueSize)
 90    continue
       return
       end

      subroutine printQueue(queueStartIndex, queue, queueSize)
c     Input: This takes the queue, queueSize and QueueStartingPoint, and
c      a template queueToPrint
c     Output: No parameters are changed, the queue is just printed in 
c     order.
      integer queueStartIndex, queueSize, queue(*), printPoint
      integer queueToPrint(101), queueToPrintStartIndex
      integer queueToPrintEndIndex, queueToPrintSize
      call initializeQueue(queueToPrint)
      queueToPrintEndIndex = 1
      queutToPrintSize = 0
      queueToPrintStartIndex = 1
      printPoint = queueStartIndex
      do 110 i = 1, 101
        if(printPoint.GE.102) then
            printPoint = 1
        endif
        call enqueue(queueToPrintEndIndex, queueToPrint,  
     + queue(printPoint), queueToPrintSize)
      printPoint = printPoint + 1
 110  continue
      write(*,*) queueToPrint
      return
      end
      
      
      program radixSort
      integer queue(101), queueStartIndex, queueEndIndex, queueSize
      integer arraySize, dequeue
      Character(len = 100) fileName
      fileName = "data.txt"
      call initializeQueue(queue)
      queueStartIndex = 1
      queueSize = arraySize(fileName)
      call inputArray(queueSize, fileName, queue)
      queueEndIndex = queueSize + 1
      call oneSort(1, queue, queueStartIndex, queueEndIndex,
     +  queueSize)
      call oneSort(10, queue, queueStartIndex, queueEndIndex,
     +  queueSize)
      call oneSort(100, queue, queueStartIndex, queueEndIndex,
     +  queueSize)
      call oneSort(1000, queue, queueStartIndex, queueEndIndex,
     +  queueSize)
c    I would have done the above as a loop, however the loops do not
c    allow multiplication incrementation. :(
      call printQueue(queueStartIndex, queue, queueSize)
      
c I also would have just printed each number on its own line, however 
c the terminal runs out of lines to print on so I opted for the print
c as an array method. Ignore any trailing zeros.
      stop
      end
      
      
      
