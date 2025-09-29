import random
import time
import matplotlib.pyplot as plt
import heapq
import matplotlib.pyplot as plt

# ========== 优化后的快速排序 ==========
def quicksort_optimized(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # 中间元素作为基准
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_optimized(left) + middle + quicksort_optimized(right)


# ========== 堆排序 ==========
def heapsort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]


# ========== 测试函数 ==========
def test_performance():
    sizes = [1000, 5000, 10000, 20000, 50000, 100000]  # 数组规模
    quicksort_times = []
    heapsort_times = []

    for n in sizes:
        # 生成随机数组
        arr = [random.randint(0, 100000) for _ in range(n)]

        # 快速排序时间
        start = time.time()
        quicksort_optimized(arr.copy())
        end = time.time()
        quicksort_times.append(end - start)

        # 堆排序时间
        start = time.time()
        heapsort(arr.copy())
        end = time.time()
        heapsort_times.append(end - start)

        print(f"数组规模: {n}, 快排时间: {quicksort_times[-1]:.6f}s, 堆排时间: {heapsort_times[-1]:.6f}s")

    # ========== 绘制折线图 ==========
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 或者 ['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, quicksort_times, marker='o', label='优化快速排序')
    plt.plot(sizes, heapsort_times, marker='s', label='堆排序')
    plt.title('排序算法性能对比 (运行时间 / 数组规模)')
    plt.xlabel('数组规模 n')
    plt.ylabel('运行时间 (秒)')
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    test_performance()