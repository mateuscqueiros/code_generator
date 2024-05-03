def comment(line):
    line_content = line[2:]
    return '// ' + line_content

def blank_line():
    return '\n'

def start_message(line):
    line_content = line[2:]
    return 'type ' + line_content[:-1] + " = {\n"

def end_message():
    return '};\n'

def field(line):
    line_content = line[2:]
    split = line_content.split(' ')
    key = split[0]
    value = split[-1][:-1]
    return '  ' + key + ": " + value + '\n'

def array_type(line):
    # Todo
    print('Array')
    pass

def simple_type(line):
    # Todo
    print('Simple')
    pass
