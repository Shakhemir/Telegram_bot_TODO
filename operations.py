from config import fields, todo_status


def form_todo_list(todo_list):
    result = '*Список задач:*\n\n'
    size = len(str(todo_list[-1][0]))  # узнаем какого размера должен быть ID контакта
    if size == 1:
        size = 2
    for todo in todo_list:
        if todo[-1] < 2:
            id = str(todo[0]).zfill(size)
            result += f'*{id}* _{fields[0]}:_ *{todo[1]}*\n' \
                      f'_{fields[1]}:_ *{todo[2]}*\n' \
                      f'_{fields[2]}:_ *{todo_status[int(todo[3])]}*\n'
            if todo[3] == 0:
                result += f'_Завершить /done{id}_\n'
            if todo[3] == 1:
                result += f'_Удалить /delete{id}_\n'
            result += '\n'
    return result
