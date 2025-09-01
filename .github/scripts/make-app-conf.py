from sys import argv, exit, stdout, stderr
from json import dumps

def perror(*args):
  print(*args, file=stderr)

if __name__ != '__main__':
  perror('script cannot be used as a module')
  exit(1)

try:
  prog_name, tag_name, *_ = argv
  conf = {
    'name': 'rel',
    'identifier': 'com.test.rel',
    'version': tag_name,
    'deps': [
      'com.io.io',
      'org.test.tester'
    ]
  }
  
  stdout.write(dumps(conf))
except ValueError:
  perror('missing parameters', file=stderr)
  exit(2)

exit(0)
