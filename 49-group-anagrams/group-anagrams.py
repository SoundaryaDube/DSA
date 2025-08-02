class Solution(object):
    def groupAnagrams(self, strs):
        anagram = defaultdict(list)
        for word in strs:
            sorted_words = ''.join(sorted(word))
            anagram[sorted_words].append(word)
        return list(anagram.values())
        