# NotifyMe Telegram Bot

Telegram bot to keep you in touch with running console commands.  

## Deploy

Based on [this article](https://www.toptal.com/python/telegram-bot-tutorial-python).

1) Create local credentials file and fill it with generated [bot API Token](https://core.telegram.org/bots#6-botfather) and [target user id](https://t.me/userinfobot):

```shell
cp config/credentials.py.sample config/credentials.py   # Linux
copy config/credentials.py.sample config/credentials.py # Windows
```

2) Install virtual environment (if not yet installed):

```shell
pip install virtualenv
```

3) Initialize virtual environment (run in project root):

```shell
python -m venv botenv/
```

4) Login/activate virtual environment in current terminal:

```shell
source botenv/bin/activate  # Linux
botenv\Scripts\activate.bat # Windows
```

5) Install project dependencies using requirements.txt

```shell
pip install -r requirements.txt
```

## Usage

After deploy, run your commands as:

```shell
/path/to/notifyme/botenv/bin/python3 /path/to/notifyme/app.py php bin/magento indexer:reindex
```

**NOTE:** To receive messages, you have to write at least one message to your bot (have chat available).

## Alias

For more comfortable usage add this line to `~/.bash_aliases` file:

```shell
alias NM="/path/to/notifyme/botenv/bin/python3 /path/to/notifyme/app.py"
```

**NOTE:** Do not forget to replace `/path/to/notifyme/` with your real path.

After reopening the terminal, aliased command will be available as:

```shell
NM php bin/magento indexer:reindex
```

## Development

* Before running any python-related command, activate virtual environment:

```shell
source botenv/bin/activate  # Linux
botenv\Scripts\activate.bat # Windows
```

* Save your project dependencies to file:

```shell
pip freeze > requirements.txt # dump project dependencies
```

### PyCharm notes:

To set up PyCharm to map your local virtualenv, search for "Python Interpreter" in settings and set project python as an interpreter.

---

**For ShellScript implementation check [notifyme](https://github.com/vchychuzhko/notifyme/) repo**
