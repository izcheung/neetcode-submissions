class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */

    // [5]
    search(nums, target) {
        let i = 0
        let j = nums.length -1
        while (i <= j){
            let m = Math.floor((i + j) / 2)
            if (nums[m] === target){
                return m
            } else if (nums[m] < target){
                i = m + 1
            } else {
                j = m - 1
            }
        }
        return -1
    }
}
