from icecream import ic

N, M, Q = map(int, input().split())
column_names = input().split()
table = [list(map(int, input().split())) for _ in range(N)]
constraints = [input().split() for _ in range(Q)]

column_indices = {name: index for index, name in enumerate(column_names)}


def check_constraints(row: list[int], constraints: list[list[str]]):
    ic(row, constraints)
    for column_name, operator, constraint_value in constraints:
        ic(column_name, operator, constraint_value)
        column_value = row[column_indices[column_name]]
        if operator == '>' and not column_value > int(constraint_value):
            return False
        if operator == '<' and not column_value < int(constraint_value):
            return False
    return True


total_sum = 0
for row in table:
    if check_constraints(row, constraints):
        total_sum += sum(row)

print(total_sum)
