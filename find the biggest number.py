list = [10, 240, 500, 67890, 123456,
       7890123,
       1000000,
       987654321,
       88888888,
       111111,
       987,
       8765432,
       12345678901234,
       777777,
       54321

]


def sort_the_numbers():
 sort_max = max(list)
 sort_min = min(list)
 return sort_max, sort_min

print(sort_the_numbers())
