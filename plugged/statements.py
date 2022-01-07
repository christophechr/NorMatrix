from source.file_parser import CFileParse
from source.file_parser import TypeLine
import re

def check(file: CFileParse) -> int:
    nb_error = 0
    for i in range(len(file.sub_parsedline)):
        line = file.sub_parsedline[i]
        if line[0] != TypeLine.COMMENT:
            ll = re.sub(".*?\*\/", '', line[1])
            ll = re.sub("\/\*.*", '', ll)
            ll = re.sub("//.*", '', ll)
            nb = ll.count(';')
            if nb > 1 and 'for' not in ll:
                print(f"{file.basename}:{i + 1}: only one statement per line")
                nb_error += 1
    return nb_error