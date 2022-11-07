def sumIntervals(intervals):

    # myRange = set()

    # for i in intervals:
    #     myRange.update(set(list(range(i[0], i[1]))))

    # return len(myRange)

    intervals.sort()

    lim,res=intervals[0][0],0

    for i in range(len(intervals)):  
        res+=max(intervals[i][1],lim)-max(intervals[i][0],lim)
        lim=max(lim,intervals[i][1])
    
    return res
