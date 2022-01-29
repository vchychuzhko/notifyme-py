import sys
import os
import subprocess
from time import time

import telebot
from src.logger import Logger

from config.credentials import bot_token, user_id


class App:
    __MAX_NUMBER_OF_CHARS = 250

    def __init__(self):
        self.logger = Logger()
        self.bot = telebot.TeleBot(bot_token)

    def run(self):
        try:
            path = os.getcwd()
            args = sys.argv[1::]
            command = ' '.join(args)

            if not command:
                print('No command was specified.')
                exit(1)

            start_time = time()
            # @TODO: Keep console output alongside
            result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=path)
            total_time = self.__format_execution_time(round(time() - start_time, 3))

            success = result.returncode == 0
            output = result.stdout.decode('utf-8')

            if not output:
                output = result.stderr.decode('utf-8')
            if len(output) > self.__MAX_NUMBER_OF_CHARS:
                output = '...' + output[-(self.__MAX_NUMBER_OF_CHARS - 3):]

            self.bot.send_message(
                user_id,
                'Command "<code>' + command + '</code>" has completed <i><u>'
                + ('successfully' if success else 'with an error') + '</u></i>.' + "\n"
                + '<b>Execution time:</b> ' + total_time + "\n"
                + (('<b><u>Output:</u></b>' + "\n" + '<pre>' + output + '</pre>') if output else 'No output.'),
                parse_mode='HTML',
            )

            self.logger.info(str({
                'command': command,
                'directory': path,
                'status': 'OK' if success else 'ERROR',
                'execution_time': total_time,
                'output': output,
            }))
        except Exception as e:
            self.logger.error(
                type(e).__name__,
                e.args[0] + str({
                    'command': command if 'command' in locals() else '',
                    'directory': path if 'path' in locals() else '',
                    'status': ('OK' if success else 'ERROR') if 'success' in locals() else 'NOT_STARTED',
                    'output': output if 'output' in locals() else '',
                })
            )
            exit(1)

    @staticmethod
    def __format_execution_time(timestamp):
        remain = timestamp
        formatted = ''

        if remain // 3600 > 0:
            h = int(remain // 3600)
            formatted = formatted + str(h) + 'h '
            remain = remain - (h * 3600)
        if remain // 60 > 0:
            m = int(remain // 60)
            formatted = formatted + str(m) + 'm '
            remain = remain - (m * 60)
        s = int(remain)

        return formatted + str(s) + 's ' + format(int((remain - s) * 1000), '03') + 'ms'


app = App()
app.run()
