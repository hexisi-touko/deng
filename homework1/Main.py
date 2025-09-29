import random
import time
from quickselect import Solution  # 假设你的代码在 quickselect.py 文件中

if __name__ == "__main__":
    sol = Solution()

    # 1. 小数据测试
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    print("--- 小数据测试 ---")
    print(f"数组: {nums1}")
    print(f"查找第{k1}大元素")

    start_time = time.time()
    result1 = sol.findKthLargest(nums1, k1)
    end_time = time.time()

    print(f"结果: {result1}")
    print(f"运行时间: {end_time - start_time:.8f} 秒")
    print("-" * 30)

    # 2. 大数据测试
    n = 1000000  # 100万数据
    k = random.randint(1, n)
    nums2 = [random.randint(0, 100000) for _ in range(n)]

    print("--- 大数据测试 ---")
    print(f"数据规模: {n}, k: {k}")

    start_time = time.time()
    result2 = sol.findKthLargest(nums2, k)
    end_time = time.time()

    print(f"结果: {result2}")
    print(f"运行时间: {end_time - start_time:.8f} 秒")

    # 验证结果（用Python内置排序）
    nums2_sorted = sorted(nums2, reverse=True)
    expected = nums2_sorted[k - 1]
    print(f"验证结果是否正确: {result2 == expected}")