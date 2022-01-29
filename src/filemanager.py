import os


class FileManager:
    def __init__(self):
        self.base_path = os.path.dirname(os.path.dirname(__file__))

    def create_dir(self, path):
        path = self.base_path + '/' + path.lstrip('/')

        if os.path.exists(path) and not os.path.isdir(path):
            raise RuntimeError('File with provided directory name "%s" already exists' % path)

        os.makedirs(path, exist_ok=True)

    def create_file(self, path, content=''):
        path = '/' + path.lstrip('/')
        folder = os.path.dirname(path)

        if os.path.isdir(self.base_path + path):
            raise RuntimeError('Requested path "%s" is a directory and cannot be recreated' % path)
        if not os.path.isdir(self.base_path + folder):
            self.create_dir(folder)
        path = self.base_path + path

        file = open(path, 'w')
        file.write(content)
        file.close()

    def write_file(self, path, content, append=False):
        path = '/' + path.lstrip('/')

        if not os.path.exists(self.base_path + path):
            self.create_file(path)
        path = self.base_path + path

        file = open(path, 'a' if append else 'w')
        file.write(content)
        file.close()
