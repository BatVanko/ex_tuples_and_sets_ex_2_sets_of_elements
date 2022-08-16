first, second = input().split()
first_set = set()
second_set = set()

for _ in range(int(first)):
    num = int(input())
    first_set.add(num)
for _ in range(int(second)):
    num = int(input())
    second_set.add(num)
print(*first_set.intersection(second_set), sep='\n')

