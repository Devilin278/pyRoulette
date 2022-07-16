# Python3 program to demonstrate the use of
# circular array without using extra memory space
 
# function to print circular list starting
# from given index ind.
def prints(roulette, n, ind, Range):
    i = ind
    count = 0 
    #print from ind-th index to (n+i)th index.
    print ('Forwarind counting starting: ')
    while i < n + ind :
        print( roulette[(i % n)], end = " ")
        i = i + 1
        count += 1
        if (count == int(Range)):
            break

    #while i < n + ind :
    #    print( roulette[(i % n)], end = " ")
    #    i -= 1
    #    if i == ind:
    #        break

def reverseCircularArray(roulette, n, ind, Range):
    K = int(ArrIndex)
    start, end = K, K - 1
    
    count = n // 1
    sheep = 0
    print('\n')
    print ('Backward counting starting: ')
    while (count):
    
        temp = roulette[start % n]
        roulette[start % n] = roulette[end % n]
        roulette[end % n] = temp
        print(roulette[K], end = " ")
        #start += 1
        end -= 1
        
        if (count == StartIndex):
            #end = n - 1
            break
        count -= 1
        
        sheep += 1
        if (sheep == int(Range)):
            break
    
    #print from ind-th index to (n+i)th index.
    #print ('Forwarind counting starting: ')
    #while i < n + ind :
 
# Driver Code
roulette = ['00',27,10,25,29,12,8,19,31,18,6,21,33,16,4,23,35,14,2,0,28,9,26,30,11,7,20,32,17,5,22,34,15,3,24,36,13,1]
n = len(roulette);

#asking to find the number and reverse index location
selection = input('Please select a number: ')

#asking for how wide of selection from starting number selection
Range = input('Please select a range size: ')


ArrIndex = roulette.index(int(selection))
StartIndex = ArrIndex
prints(roulette, n, int(ArrIndex), Range);

reverseCircularArray(roulette, n, int(ArrIndex), Range)

