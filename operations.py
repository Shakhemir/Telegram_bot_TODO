from config import fields, todo_status, add_task_tail


def form_todo_list(todo_list):
    """
    Формируем список текущих и завершенных задач для вывода в чат
    """

    result = '*Список задач:*\n\n'
    done_list = ''
    size = len(str(todo_list[-1][0]))  # узнаем какого размера должен быть ID
    if size == 1:
        size = 2
    for todo in todo_list:
        if todo[-1] < 2:
            id = str(todo[0]).zfill(size)
            if todo[3] == 0:
                result += f'{todo_status[int(todo[3])]} *{id}* _{fields[0]}:_ *{todo[1]}*\n'
                if len(todo[2]) > 0:
                    result += f'_{fields[1]}:_ *{todo[2]}*\n'
                result += f'_Завершить /done{id}_\n\n'
            if todo[3] == 1:
                done_list += f'{todo_status[int(todo[3])]} _{id} {fields[0]}: {todo[1]}_\n'
                if len(todo[2]) > 0:
                    done_list += f'_{fields[1]}: {todo[2]}_\n'
                done_list += f'_Удалить /delete{id}_\n\n'
    result += done_list
    result += add_task_tail
    return result


if __name__ == "__main__":
    print(form_todo_list.__doc__)