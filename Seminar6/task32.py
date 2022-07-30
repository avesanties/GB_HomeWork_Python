# 30.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

def print_operation_table(operation, num_rows=9, num_columns=9):
    result = [[operation(x,y) for y in range(1,num_rows+1)] for x in range(1,num_columns+1)]
    for n in result:
        print(*n)

print_operation_table(lambda x,y: x + y, num_rows=9,num_columns=9)