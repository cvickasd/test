import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Создаем телеграмм бота
bot = telegram.Bot(token='6149703984:AAERkO3wEQOxCDSO30sm-mYORbQL6TBox_Q')
updater = Updater(token='6149703984:AAERkO3wEQOxCDSO30sm-mYORbQL6TBox_Q', use_context=True)
dispatcher = updater.dispatcher

# Функция для начала игры
def start_game(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Добро пожаловать в игру крестики-нолики! Чтобы начать игру, введите /play.")

# Функция для игры
def play_game(update, context):
    # Инициализация игрового поля
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    # Отправляем сообщение с инструкциями для игрока
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Вы играете за {player}. Чтобы поставить свой знак, введите номер строки (от 1 до 3) и номер столбца (от 1 до 3), разделенные пробелом.")

    # Основной цикл игры
    while True:
        # Отправляем сообщение с текущим состоянием игрового поля
        board_str = '\n'.join(['|'.join(row) for row in board])
        context.bot.send_message(chat_id=update.effective_chat.id, text=board_str)

        # Получаем следующий ход от игрока
        user_input = update.message.text.split()
        if len(user_input) != 2:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Некорректный ввод. Попробуйте еще раз.")
            continue

        row, col = user_input
        if not row.isdigit() or not col.isdigit():
            context.bot.send_message(chat_id=update.effective_chat.id, text="Некорректный ввод. Попробуйте еще раз.")
            continue

        row, col = int(row) - 1, int(col) - 1
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != ' ':
            context.bot.send_message(chat_id=update.effective_chat.id, text="Некорректный ход. Попробуйте еще раз.")
            continue

        # Ставим знак на игровое поле
        board[row][col] = player

        # Проверяем, есть ли победитель или ничья
        if any(all(board[i][j] == player for j in range(3)) for i in range(3)) \
                or any(all(board[i][j] == player for i in range(3)) for j in range(3)) \
                or all(board[i][i] == player for i in range(3)) \
                or all(board[i][2-i] == player for i in range(3)):
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"Поздравляем! Игрок {player} победил!")
            break
        elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            context.bot.send_message(chat_id=update.effective_chat.id, text="Ничья!")
            break

        # Смена игрока
        player = 'O' if player == 'X' else 'X'
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Ходит игрок {player}.")

# Обработчики команд
start_handler = CommandHandler('start', start_game)
play_handler = CommandHandler('play', play_game)

# Добавляем обработчики команд
dispatcher.add_handler(start_handler)
dispatcher.add_handler(play_handler)

# Запускаем бота
updater.start_polling()