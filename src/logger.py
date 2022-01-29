from src.datetime import DateTime
from src.filemanager import FileManager


class Logger:
    __LOG_DIR = '/var/log/'
    __INFO_LOG_FILE = 'info.log'
    __ERROR_LOG_FILE = 'exception.log'

    def __init__(self):
        self.datetime = DateTime()
        self.filemanager = FileManager()

    def info(self, message):
        self.__write(self.__INFO_LOG_FILE, message)

    def error(self, error_type, message):
        self.__write(self.__ERROR_LOG_FILE, error_type + ': ' + message)

    def __write(self, log_file, message):
        self.filemanager.write_file(
            self.__LOG_DIR + log_file,
            '[' + self.datetime.get_current_time() + '] ' + message + "\n",
            True
        )
