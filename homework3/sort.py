def solve_set_partition(A):
    # 对集合元素降序排序
    A_sorted = sorted(A, reverse=True)
    n = len(A)
    # 计算两个子集的元素个数，n1为ceil(n/2)，n2为floor(n/2)
    n1 = (n + 1) // 2
    n2 = n // 2
    # 划分两个子集：A1取前n1个最大的元素，A2取剩下的
    A1 = A_sorted[:n1]
    A2 = A_sorted[n1:]
    # 计算两个子集的和
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
    print("|n1-n2|:", abs(len(A1)-len(A2)))
    print("|S1-S2|:", abs(S1-S2))