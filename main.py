from datetime import datetime

try:
    import pyperclip
except ImportError:
    pyperclip = None


def get_dt_from_input():
    print('Next birthday format: YYYY-MM-DD')
    inp = input('> ')
    try:
        dt = datetime.strptime(inp, '%Y-%m-%d')
    except ValueError:
        print('Invalid format')
        get_dt_from_input()
    else:
        return dt


def discord_formatting(dt):
    timestamp = int(dt.timestamp())
    return '<t:%d:R>' % timestamp


def main():
    dt = get_dt_from_input()
    df = discord_formatting(dt)

    print('Add the following to your about me:', end='\n')
    print('**Birthday**: %s' % df)

    try:
        pyperclip.copy('**Birthday**: %s' % df)
    except AttributeError:
        pass
    else:
        print('It\'s been copied to your clipboard')


if __name__ == '__main__':
    main()
