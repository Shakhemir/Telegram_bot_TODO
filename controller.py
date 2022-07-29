import operations as op
import config
from database import BotDB

BotDB = BotDB(config.database_file)


def func(index):
    func_list = send_start, add_todo, edit_todo, change_status, delete_todo, show_todo_list
    return func_list[index]


def command_handler(chat_id, txt):
    command, *args = txt.split()
    args = ' '.join(args)
    command = command[1:]  # оголяем команду от аргументов и первого слеша /
    index = config.menu.index(command)
    return func(index)(chat_id, args)


def message_handler(chat_id, txt):
    for item in config.menu:
        if txt[1:] .startswith(item):  # превращаем команды вида /done01 в /done 01
            return command_handler(chat_id, txt[:len(item)+1] + ' ' + txt[len(item)+1:])
    last_command = BotDB.check_command(chat_id).split()
    if last_command:
        index = config.menu.index(last_command[0])
        return func(index)(chat_id, txt)
    else:
        return config.help_text


def send_start(chat_id, args):
    BotDB.new_user(chat_id)
    return config.welcome_text + '\n\n' + config.help_text


def add_todo(chat_id, args):
    if args:
        last_command = BotDB.check_command(chat_id).split()
        if len(last_command) > 1:
            BotDB.add_deadline(chat_id, args, last_command[1])
            BotDB.update_command(chat_id, '')
            message = config.text_OK
        else:
            id = BotDB.add_task(chat_id, args)
            BotDB.update_command(chat_id, f'add {id}')
            message = config.text_whats_deadline
    else:
        BotDB.update_command(chat_id, 'add')
        message = config.text_enter_task
    return message


def edit_todo(chat_id, args):
    if args:
        last_command = BotDB.check_command(chat_id).split()
        if len(last_command) > 1:
            id = last_command[1]
            BotDB.change_task(chat_id, args, id)
            BotDB.update_command(chat_id, f'add {id}')
            message = config.text_whats_deadline
        else:
            if args.isdigit():
                BotDB.update_command(chat_id, f'edit {args}')
                message = config.text_enter_task
            else:
                BotDB.update_command(chat_id, '')
                message = config.text_wrong_id
    else:
        BotDB.update_command(chat_id, 'edit')
        message = config.text_enter_4_edit
    return message


def change_status(chat_id, args):
    if args:
        if args.isdigit():
            BotDB.change_status(chat_id, args, 1)
            message = config.text_task_done.format(args)
        else:
            message = config.text_wrong_id
        BotDB.update_command(chat_id, '')
    else:
        BotDB.update_command(chat_id, 'done')
        message = config.text_enter_4_done
    return message


def delete_todo(chat_id, args):
    if args:
        if args.isdigit():
            BotDB.change_status(chat_id, args, 2)
            message = config.text_task_deleted.format(args)
        else:
            message = config.text_wrong_id
        BotDB.update_command(chat_id, '')
    else:
        BotDB.update_command(chat_id, 'delete')
        message = config.text_enter_4_delete
    return message


def show_todo_list(chat_id, args):
    result = BotDB.get_table(chat_id)
    result = op.form_todo_list(result)
    return result
