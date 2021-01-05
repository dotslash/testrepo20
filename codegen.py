import sys
from pathlib import Path
import uuid

def make_file_content(fname):
  ret = [fname]
  rand_str = lambda: uuid.uuid4().hex
  len_rand_str = len(rand_str())
  for i in range(1000//len_rand_str):
      ret.append(rand_str())
  return '\n'.join(ret) + '\n'

if __name__ == '__main__':
  nfiles = int(sys.argv[1])
  for i in range(nfiles):
    # 123 => 1/2/3.txt
    fname = '/'.join(list(str(i))) + ".txt"
    p = Path(fname)
    p.parent.mkdir(exist_ok=True)
    p.write_text(make_file_content(fname))
