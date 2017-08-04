nums=[1,2,3,5, 8]

def find_missing(array):
    missing=""
    for i in range(len(nums)-1):
        dif=array[i+1]-array[i]
        #print "Difference is: " + str(dif)
        count=1
        if dif>1:
            print "Last number was: %s."%(array[i]) 
        while dif>1:
            missing=array[i]+count
            print "You're missing: %s."%(missing)
            dif-=1
            count +=1
find_missing(nums)
