n, k = map(int, input().split())

pop_index = 0
round_list = []
answer = []
answer_str = ''

for i in range(n):
    round_list.append(i + 1)

for j in range(n):
    pop_index = k - 1

if pop_index >= len(round_list):
    pop_index = pop_index % len(round_list)

    answer.append(str(round_list.pop(pop_index)))
    answer_str = "<", ", ".join(answer), ">"

    print(answer_str)