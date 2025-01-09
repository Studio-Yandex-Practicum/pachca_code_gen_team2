import errno
import os
import os.path
import pathlib


# presented_code = set()


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass


def safe_open_w(path, mode: str):
    ''' Open "path" for writing, creating any parent directories as needed.
    '''
    mkdir_p(os.path.dirname(path))
    return open(path, mode, encoding='utf-8')


def write_to_file(
    file_name: str, text_to_write: str,
    open_file_mode: str = 'a'
):
    with safe_open_w(
        pathlib.Path(__file__).parent.parent.resolve() / f'models/{file_name}.py',
        open_file_mode
    ) as f:
        f.write(text_to_write)
        # if text_to_write not in presented_code:
        #     f.write(text_to_write)
        #     presented_code.add(text_to_write)


if __name__ == '__main__':
    write_to_file('model_users.py', '\n\nANOTHER CODE HERE')
