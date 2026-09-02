class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        // Use a set to keep track of what is in the window

/**
 * "pwwkew"
 *    ^^
 *  seen = {w}
 *  maxLength = 2
 * 
 * 
 */ 
  

        let left = 0
        let i = 0
        let seen = new Set()
        let maxLength = 0
        while (left < s.length && i < s.length){
            while (seen.has(s[i])){
                seen.delete(s[left])
                left += 1
            }
            seen.add(s[i])
            maxLength = Math.max(maxLength, i-left+1)
            i += 1
        }
        return maxLength
    }
}
