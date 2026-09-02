class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        // "AAABABB"
        //  ^    ^
        // count = {A:4, B:2}
        // res = 0
        //  l = 0
        //  r = 4
        // len = 6
        const count = {}
        let res = 0

        let l = 0
        for (let r = 0; r < s.length; r++){
            count[s[r]] = (count[s[r]] || 0 ) + 1

            while ((r-l+1) - Math.max(...Object.values(count)) > k){
                count[s[l]] -= 1
                l += 1
            }
            res = Math.max(r-l+1, res)
        }
        return res

    }
}
