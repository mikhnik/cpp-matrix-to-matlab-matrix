import sys
import re
from math import *

def main():
    if len(sys.argv) != 3:
        print('Wrong arguments: first argument must be path to input XML!')
        print('Wrong arguments: second argument must be output path for XML!')
        return

    in_path = sys.argv[1]
    out_path = sys.argv[2]
    
    f = open(in_path, 'r')
    data = f.read()
    f.close()
    
    mappings = {}
    
    for index in range(20):
        mappings[re.compile('J' + str(index))] = 'obj.J(' + str(index + 1) + ')'
        mappings[re.compile('l' + str(index))] = 'obj.l(' + str(index + 1) + ')'
        mappings[re.compile('m' + str(index))] = 'obj.m(' + str(index + 1) + ')'
        mappings[re.compile('c' + str(index))] = 'obj.c(' + str(index + 1) + ')'
        mappings[re.compile('q' + str(index) + '\[t\]')] = 'obj.qa(' + str(index + 1) + ')'
    
    mappings[re.compile('Sin')] = 'sin'
    mappings[re.compile('Cos')] = 'cos'
    mappings[re.compile('Sqrt')] = 'sqrt'
    mappings[re.compile('\n')] = ''
    mappings[re.compile('\[')] = '('
    mappings[re.compile('\]')] = ')'
    mappings[re.compile('\{\{')] = '[('
    mappings[re.compile('\}\}')] = ')]'
    mappings[re.compile('\}\,')] = ');\n'
    mappings[re.compile('\{')] = '('
    mappings[re.compile('\,')] = ') ('
    
    for regex, replace in mappings.items():
        data = re.sub(regex, replace, data)
    
    f = open(out_path, 'w')
    f.write(data)
   
if __name__ == '__main__':
    main()
