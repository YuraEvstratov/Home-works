def find_max_profit(count_days: int, coins: list) -> int:
    profit = 0
    if count_days <= 1:
        return profit
    for i in range(1, count_days):
        if coins[i - 1] < coins[i]:
            profit += coins[i] - coins[i - 1]
    return profit

print(find_max_profit(6, [7, 1, 5, 3, 6, 4]))
print(find_max_profit(5, [1, 2, 3, 4, 5]))
print(find_max_profit(6, [1, 12, 12, 16, 1, 8]))