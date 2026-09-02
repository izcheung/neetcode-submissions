class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        if (strs.length === 0) return ""
        const encodeStr = []
        for (let str of strs){
            const lenStr = str.length
            encodeStr.push(lenStr)
            encodeStr.push("#")
            encodeStr.push(str)
        }
        console.log(encodeStr.join(""))
        return encodeStr.join("")
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        if (str.length === 0) return []
        let i = 0
        let strLen = str.length
        const ans = []
       
        while (i < strLen) {
            const numberStr = []
            while (i < strLen && str[i] !== '#'){
                numberStr.push(str[i])
                i+= 1
            }
            let length = Number(numberStr.join(""))

            i += 1 // Skip #
            ans.push((str.slice(i, i+length)))
            i = i + length
            
        }
    return ans
    }
    
}
