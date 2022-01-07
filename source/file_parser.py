import re
from enum import Enum

class TypeLine(Enum):
    FUNCTION = 1
    MACRO = 2
    STRUCT = 3
    ENUM = 4
    GLOBAL = 5
    COMMENT = 6
    NONE = 7

class CFileParse:
    def __init__(self, filepath, name):
        """an object of a file 'parsed'"""
        self.basename = filepath[len(name) + 1:] # the relative path
        self.filepath = filepath # the absolute path
        self.real_filelines: list[str] = [] # list of each line
        self.sub_filelines: list[str] = [] # list of each line without str ("text here will be removed")
        self.sub_parsedline: list[tuple[TypeLine, str]] = []# sub_filelines but with the type line
        self.real_parsedline: list[tuple[TypeLine, str]] = []# real_filelines but with the type line

    def get_filelines(self):
        with open(self.filepath) as fd:
            lines = fd.read()
        self.real_filelines = lines.split('\n')
        lines = re.sub(r'".+?"', '', lines)
        self.sub_filelines = lines.split('\n')

def get_status(lines: str) -> int:
    reg = [
        '\w{1,}(\*){0,} (\*){0,}\w{1,}\(((void)|(\n{0,1} *\w{1,}(\*){0,} (\*){0,}\w{1,}(, {0,1}\n{0,1} *\w{1,}(\*){0,} (\*){0,}\w{1,}){0,3})\n{0,1} {0,})\)\n{\n(.*\n)*?}',
        ' {0,}#\w{1,}.*',
        '(typedef ){0,1}(struct )(\w{1,} ){0,1}{\n {4}\w{1,} \w{1,};(\n {4}\w{1,} \w{1,};){0,}\n}( \w{1,}){0,1};',
        '(typedef ){0,1}(enum )(\w{1,} ){0,1}{\n {4}\w{1,} \w{1,};(\n {4}\w{1,} \w{1,};){0,}\n}( \w{1,}){0,1};',
        '(static ){0,1}(const ){0,1}\w{1,} \*{0,}\w{1,}(\[[0-9]{0,}\]){0,1} = ((\w{0,})|({\n{0,1} {0,}\w{0,}(,\n{0,1} {0,}\w{0,}){0,})|)\n{0,1}}{0,1};',
        '^\/\*(.*?\n{0,}){0,}\*\/',
        '^\W{1,}\/\*(.*?\n{0,}){0,}\*\/'
        '^\/\/',
        '^\W{1,}\/\/'
    ]
    status = [
        TypeLine.FUNCTION,
        TypeLine.MACRO,
        TypeLine.STRUCT,
        TypeLine.ENUM,
        TypeLine.GLOBAL,
        TypeLine.COMMENT,
        TypeLine.COMMENT,
        TypeLine.COMMENT,
        TypeLine.COMMENT
    ]
    for i in range(len(reg)):
        res = re.search(reg[i], lines, re.MULTILINE)
        if res != None and res.start() <= len(lines.split('\n')[0]):
            return (status[i], lines[res.start():res.end()])
    return (TypeLine.NONE, lines.split('\n')[0])

def parse(filepath: str, dirname: str) -> CFileParse:
    obj = CFileParse(filepath, dirname)
    obj.get_filelines()
    i = 0
    while i < len(obj.sub_filelines):
        rest = "\n".join(obj.sub_filelines[i:])
        (status, lines) = get_status(rest)
        for line in lines.split('\n'):
            obj.sub_parsedline.append((status, line))
            obj.real_parsedline.append((status, obj.real_filelines[i]))
            i += 1
    return obj