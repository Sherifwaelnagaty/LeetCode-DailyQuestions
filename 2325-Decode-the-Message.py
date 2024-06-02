
class Solution:
    def decodeMessage(self, key, message) -> str:
        
        alphabets = list('abcdefghijklmnopqrstuvwxyz')
        message_chars = []
        res = ""

        for letter in key:
          if letter not in message_chars and letter != " ":
            message_chars.append(letter)

        len_message_chars = len(message_chars)
        zipped = dict(zip(message_chars, alphabets[:len_message_chars+1]))

        for letter in message:
          res += zipped.get(letter, " ")

        return res