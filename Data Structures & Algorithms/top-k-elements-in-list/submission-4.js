class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const count = {}
        for (let num of nums){
            count[num] = (count[num] || 0) + 1
        }
        // console.log(Object.entries(count))
        const arr = Object.entries(count)
        arr.sort((a,b) => b[1] - a[1])
        const ans = arr.map((ele) => Number(ele[0])).slice(0,k)
        return ans


    }
}
