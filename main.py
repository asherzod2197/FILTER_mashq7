# 31-35
roy = [6, 12, 18]
print(list(filter(lambda x: x % 6 == 0, roy)))

roy = ["car", "bus", "bike"]
print(list(filter(lambda x: x.startswith("b"), roy)))

roy = [21, 22, 23]
print(list(filter(lambda x: x % 2 == 1, roy)))

roy = ["aa", "ab", "ba"]
print(list(filter(lambda x: x.endswith("a"), roy)))

roy = [0, -1, -2]
print(list(filter(lambda x: x < 0, roy)))
