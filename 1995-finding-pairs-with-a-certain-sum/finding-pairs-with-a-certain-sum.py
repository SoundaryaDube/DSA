class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.a = nums1
        self.b = nums2
        self.m = Counter(nums2)
    def add(self, index: int, val: int) -> None:
        old = self.b[index]
        self.m[old] -= 1
        self.b[index] += val
        self.m[self.b[index]] += 1
    def count(self, tot: int) -> int:
        c = 0
        for x in self.a:
            c += self.m[tot-x]
        return c


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)