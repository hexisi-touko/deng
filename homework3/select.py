import random


def quickselect(nums, k):
    """
    快速选择算法：找到nums中第k大的元素（k从1开始）
    平均时间复杂度O(n)，最坏O(n²)，通过随机化 pivot 降低最坏情况概率
    """

    def select(left, right, target):
        if left == right:
            return nums[left]
        # 随机选择pivot，避免最坏情况
        pivot_idx = random.randint(left, right)
        # 将pivot交换到当前区间末尾
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        pivot = nums[right]
        # 分区：将大于pivot的元素放左边，小于的放右边
        store_idx = left
        for i in range(left, right):
            if nums[i] > pivot:  # 降序分区（找第k大）
                nums[store_idx], nums[i] = nums[i], nums[store_idx]
                store_idx += 1
        # 将pivot放到最终位置
        nums[store_idx], nums[right] = nums[right], nums[store_idx]
        # 递归查找
        if store_idx == target:
            return nums[store_idx]
        elif store_idx < target:
            return select(store_idx + 1, right, target)
        else:
            return select(left, store_idx - 1, target)

    return select(0, len(nums) - 1, k - 1)  # k-1转为0基索引


def solve_set_partition(A):
    A = A.copy()  # 避免修改原数组
    n = len(A)
    n1 = (n + 1) // 2  # 较大子集的元素个数
    # 找到第n1大的元素，以此为界划分前n1个最大元素
    quickselect(A, n1)
    # 前n1个元素为A1（无需完全排序，只需确保它们是最大的n1个）
    A1 = A[:n1]
    A2 = A[n1:]
    S1 = sum(A1)
    S2 = sum(A2)
    return A1, A2, S1, S2


# 测试示例
if __name__ == "__main__":
    A = [1, 5, 3, 8, 2]
    A1, A2, S1, S2 = solve_set_partition(A)
    print("子集A1:", A1)
    print("子集A2:", A2)
    print("A1和S1:", S1)
    print("A2和S2:", S2)
    print("|n1-n2|:", abs(len(A1) - len(A2)))
    print("|S1-S2|:", abs(S1 - S2))