class Solution:
    # I need something to represent a break in a string

    def encode(self, strs: List[str]) -> str:
        '''
        str = ["yes", "no"]
        ans = ["3#yes", "2#no"]
        return "3#yes2#no"
        current_word = [2, #, "no"]
        current_string = "2#no"

        '''
        ans = []
        for word in strs:
            current_word = []
            current_word.append(str(len(word)))
            current_word.append("#")
            current_word.append(word)
            current_string = "".join(current_word)
            ans.append(current_string)
        return "".join(ans)


    def decode(self, s: str) -> List[str]:
        '''
        s = "5#Hello5#World"
                      ^
        pointer = 3
        ans = ["Hello",
        number = [5,
        word = [H,e,l,l,o
        word_string = "hello"
        3 < 7
        '''
        pointer = 0
        ans = []
        while pointer < len(s):
            number = []
            while s[pointer] != "#" and pointer < len(s):
                number.append(s[pointer])
                pointer += 1
            word = []
            pointer += 1
            end = (pointer + int("".join(number)))
            while pointer < end and pointer < len(s):
                word.append(s[pointer])
                pointer += 1
            word_string = "".join(word)
            ans.append(word_string)

        return ans


