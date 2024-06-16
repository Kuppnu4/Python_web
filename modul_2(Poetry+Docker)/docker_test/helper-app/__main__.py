from CLIBot import CLIBot

if __name__ == "__main__":
    print('Hello. I am your contact-assistant. What should I do with your contacts?')
    bot = CLIBot()
    bot.book.load("auto_save")
    commands = {'Add': bot.add, 'Search': bot.search,
                'Edit': bot.edit, 'Load': bot.load, 'Remove': bot.remove, 'Save': bot.save,
                'Congratulate': bot.congratulate, 'View': bot.view, 'Exit': bot.exit}

    while True:
        action = input('Type help for list of commands or enter your command\n').strip().lower()

        if action == 'help':
            format_str = str('{:%s%d}' % ('^', 20))
            for command_key in commands.keys():
                print(format_str.format(command_key))
            continue

        for comand in filter(lambda c: c.lower() == action, commands):
            commands[comand]()
