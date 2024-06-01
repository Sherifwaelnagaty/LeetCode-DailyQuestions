class Solution:
    def interpret(self, command: str) -> str:
        str1 = ""
        for i in command:
            str1 += i
        return(str1.replace("()","o").replace("(al)","al"))