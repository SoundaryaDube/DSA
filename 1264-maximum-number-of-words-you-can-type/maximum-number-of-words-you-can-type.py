class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        words = text.split()
        broken_set = set(brokenLetters)
        count = 0
        for word in words:
            valid = True
            for char in word:
                if char in broken_set:
                    valid = False
                    break
            if valid:
                count += 1
        return count