'''
Add your next birthday on the about me
section on your Discord profile.
'''

from datetime import datetime

try:
    import pyperclip
except ImportError:
    class pyperclip:
        @staticmethod
        def copy(text: str) -> None:
            print('Add the following to your about me:' + '\n' + text)
            raise ImportError("pyperclip not found")


def get_datetime_object_from_input() -> datetime:
    '''Get a datetime object from user input.'''
    print('Next birthday format: YYYY-MM-DD')
    inp = input('> ')
    try:
        datetime_object = datetime.strptime(inp, '%Y-%m-%d')
    except ValueError:
        print('Invalid format')
        return get_datetime_object_from_input()
    else:
        return datetime_object


def get_discord_formatting(datetime_object: datetime) -> str:
    '''Get the discord formatting from a datetime object.'''
    timestamp = int(datetime_object.timestamp())

    return f'<t:{timestamp}:R>'


def main() -> None:
    '''Main function.'''
    datetime_object = get_datetime_object_from_input()
    discord_formatting = get_discord_formatting(datetime_object)

    try:
        pyperclip.copy(f'**Birthday**: {discord_formatting}')
    except ImportError:
        pass
    else:
        print('It\'s been copied to your clipboard')


if __name__ == '__main__':
    main()
