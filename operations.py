from config import fields, todo_status


def form_todo_list(todo_list):
    result = ''
    width = sum([f[1] for f in fields]) + len(fields) * 2  # ширина записи дела
    result += '-' * width + '\n'
    size = len(str(todo_list[-1][0]))  # узнаем какого размера должен быть ID контакта для выравнивания
    result += f'{"ID".ljust(size)}  {"  ".join([f[0].ljust(f[1]) for f in fields])}\n'  # Заголовки
    result += '-' * width + '\n'
    for todo in todo_list:
        if todo[-1] < 2:
            result += str(todo[0]).zfill(size) + '  '
            for i, element in enumerate(fields[:-1]):
                result += str(todo[i + 1]).ljust(element[1]) + '  '
            result += todo_status[int(todo[-1])].ljust(fields[-1][1]) + '\n'
    result += '-' * width
    return result
