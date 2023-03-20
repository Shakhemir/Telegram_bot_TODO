STOP_TIME = "12:55"

database_file = 'todo_db.db'
log_file = 'logs.txt'

menu = ['start', 'add', 'edit', 'done', 'delete', 'show', 'stop']
menu_edit_status = '01. Завершить дело', '02. Удалить'

fields = 'Задача', 'Дедлайн', 'Статус'  # Названия полей списка задач"
todo_status = '📝', '✔️', 'Удалено', 'Зарезервировано'

welcome_text = 'Добро пожаловать бот "Планировщик задач"'
help_text = f'Выберите команду из списка:\n' \
            f'/{menu[1]} – добавить задачу\n' \
            f'/{menu[2]} – редактировать задачу\n' \
            f'/{menu[3]} – завершить задачу\n' \
            f'/{menu[4]} – удалить задачу\n' \
            f'/{menu[5]} – показать список дел'
show_list_tail = f'\n_Показать список дел /{menu[5]}_'
add_task_tail = f'\n_Добавить новую задачу /{menu[1]}_'
text_enter_task = 'Введите задачу'
text_whats_deadline = 'Какой крайний срок? _(можно проигнорировать)_'
text_OK = f'Готово!' + show_list_tail
text_wrong_id = 'Вы ввели неправильный ID!'
text_enter_4_done = 'Введите ID задачи для завершения'
text_enter_4_edit = 'Введите ID задачи для изменения'
text_enter_4_delete = 'Введите ID задачи для удаления'
text_task_done = 'Запись под номером {} завершена' + show_list_tail
text_task_deleted = 'Запись под номером {} удалена' + show_list_tail
