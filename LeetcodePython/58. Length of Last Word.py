class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        clear_text = s.strip()
        list_text = clear_text.split(" ")
        return len(list_text[-1])

        
