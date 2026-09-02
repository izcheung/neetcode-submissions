class Solution {

    isAlphaNum(char){
        return (
            ('a' <= char && char <= 'z') ||
            ('A' <= char && char <= 'Z') ||
            ('0' <= char && char <= '9')
        )
    }
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let newString = s.split('').filter((letter) => this.isAlphaNum(letter)).join('').toLowerCase()     
        
        let i = 0
        let j = newString.length - 1
        while (i < j){
            if (newString[i]!==newString[j]){
                return false
            }
            i += 1
            j -= 1
        }
        return true
    }

}
