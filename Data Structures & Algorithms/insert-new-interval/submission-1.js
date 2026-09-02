class Solution {
    /**
     * @param {number[][]} intervals
     * @param {number[]} newInterval
     * @return {number[][]}
     */
    insert(intervals, newInterval) {

        const res = []
   
        for (let i = 0; i < intervals.length; i ++){
            let newStart = newInterval[0]
            let newEnd = newInterval[1]
            let currStart = intervals[i][0]
            let currEnd = intervals[i][1]

            if (newEnd < currStart) {
                res.push(newInterval)
                return res.concat(intervals.slice(i))
            }
            else if (currEnd < newStart){
                res.push(intervals[i])
            }
            else {
                newInterval = [Math.min(currStart, newStart), Math.max(currEnd, newEnd)]
            }
   

        }
        res.push(newInterval)
        return res


    }
}
