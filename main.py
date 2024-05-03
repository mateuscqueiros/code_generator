import sys
import argparse
import re

with open('data.txt', 'r', encoding='utf-8') as data:
    with open('result.ts', 'w') as result:
        try:
            parser = argparse.ArgumentParser()
            parser.add_argument('-g', dest="g", type=str, help="Specifiy generators for conversion")
            args = parser.parse_args()
            commands = __import__(args.g, globals=None, locals=None, fromlist=(), level=0)
        except:
            print('No such file on root')
            sys.exit(1)

        result.write('')

        for line_no, line in enumerate(data):
            arg = ''
            first_char = line[:1]

            if first_char == '#':           arg = commands.comment(line)
            elif first_char == 'M':         arg = commands.start_message(line)
            elif first_char == '\n':        arg = commands.blank_line()
            elif first_char == 'F':         arg = commands.field(line)
            elif first_char == 'E':         arg = commands.end_message()
            elif re.search(line, r'/^F\s*(\w+)\s+(\w+)\[(\d+)\]$/'):    arg = commands.array_type(line)
            elif re.search(line, r'/^F\s*(\w+)\s+(\w+)$/'):             arg = commands.simple_type(line)
            else:
                print('Invalid line at: ', line_no)
                continue

            result.write(arg)
