from sys import argv, exit, stdin, stdout, stderr
from json import dump, load

def eprint(*args):
  print(*args, file=stderr)

if __name__ != '__main__':
  eprint('script cannot be used as a module')
  exit(1)

_program, version, *_ = argv
conf = load(stdin)
conf['version'] = version
dump(conf, stdout, indent=2)

exit(0)
