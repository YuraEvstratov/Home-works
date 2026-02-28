# Все 5-⁠буквенные слова, составленные из букв А, О, У, записаны в алфавитном порядке. Вот начало списка:
# 1.  ААААА
# 2.  ААААО
# 3.  ААААУ
# 4.  АААОА
# ...
#  
# Укажите номер первого слова, которое начинается с буквы У.
arr = {0: "А", 1: "О", 2: "У"}
k = 0
size = len(arr)
for i in range(0, size):
    for g in range(0, size):
        for j in range(0, size):
            for m in range(0, size):
                for q in range(0, size):
                    k += 1
                    if arr[i] == "У":
                        print(k)
                        break
