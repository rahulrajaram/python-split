"""
Script is a partial implementation of the `split` program that
splits regular text files by newline.
"""
import time
import argparse


EOF_REACHED = False


def __seek_back_to_start_of_chunk(file, start_pos):
    """
    Function captures the intent to rewind file pointer
    to the position identified by `start_pos`
    """
    file.seek(start_pos)


def __print_chunk(file, start_pos, end_pos):
    """
    Function prints the contents of the file between byte
    numbers/character positions, `start_pos` and `end_pos`.
    """
    chunk = file.read(end_pos - start_pos)
    print(chunk)


def __print_start_and_end_character_positions(file, start_pos, end_pos):
    print(
        'Start Byte Position: {}, '
        'End Byte Position: {}'.format(
            start_pos,
            end_pos
        )
    )
    print()
    print('*********')
    print()


def __handle_chunk(file, start_pos, end_pos):
    """
    Function implements a strategy to handle a chunk of the file.
    In the case of this example, this is to simply print it
    """
    __seek_back_to_start_of_chunk(file, start_pos)
    __print_chunk(file, start_pos, end_pos)
    __print_start_and_end_character_positions(file, start_pos, end_pos)
    

def __throttle_read():
    time.sleep(1)


def __find_next_newline(file, lines):
    """
    Function reads `file` one character at a time until `lines`
    number of lines are read or the EOF is reached. Function has
    the side-effect of winding forward `file` by so many characters
    as are found within `lines` number of lines.
    """
    newlines_count = 0
    while newlines_count < lines:
        current_char = file.read(1)
        if current_char == '\n':
            newlines_count += 1
        if current_char == '':
            global EOF_REACHED
            EOF_REACHED = True
            return


def __parse_arguments():
    parser = argparse.ArgumentParser(
        description="Partial implementation of the Unix `split` program in Python",
    )
    parser.add_argument(
        'file',
        help='file to split'
    )
    parser.add_argument(
        '-l', '--lines',
        help='max number of lines a chunk can have',
        type=int
    )
    return parser.parse_args()


def split(file_name, lines):
    """
    Function captures the driver code
    """
    split_count = 1
    with open(file_name, 'r') as file:
        while EOF_REACHED is False:
            current_start = file.tell()
            __find_next_newline(file, lines)
            current_end = file.tell()
            __handle_chunk(file, current_start, current_end)
            current_start = current_end
            __throttle_read()


if __name__ == '__main__':
    arguments = __parse_arguments()
    split(arguments.file, arguments.lines)
