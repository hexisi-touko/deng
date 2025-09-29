import random

#快速选择算法（Quickselect），用来在 O(n) 平均时间复杂度内找到数组中第 k 大（或第 k 小）的元素。
class Solution:
    def quickselect(self, nums, l, r, k):
        if l == r:
            return nums[k]
        # 随机选择基准值，避免最坏情况
        pivot_idx = random.randint(l, r)
        pivot = nums[pivot_idx]
        nums[l], nums[pivot_idx] = nums[pivot_idx], nums[l]

        i, j = l - 1, r + 1
        while i < j:
            while True:
                i += 1
                if nums[i] >= pivot:
                    break
            while True:
                j -= 1
                if nums[j] <= pivot:
                    break
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        if k <= j:
            return self.quickselect(nums, l, j, k)
        else:
            return self.quickselect(nums, j + 1, r, k)

    def findKthLargest(self, nums, k):
        n = len(nums)
        return self.quickselect(nums, 0, n - 1, n - k)