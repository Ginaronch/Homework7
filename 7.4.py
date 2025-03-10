def common_elements():
    kr_3 = {num for num in range(0, 100) if num % 3 == 0}
    kr_5 = {num for num in range(0, 100) if num % 5 == 0}
    return kr_3.intersection(kr_5) #можно просто использовать "&"
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")