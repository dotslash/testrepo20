import sys
from pathlib import Path
nfiles = int(sys.argv[1])

for i in range(nfiles):
  # 123 => 1/2/3.txt
  fname = '/'.join(list(str(i))) + ".txt"
  p = Path(fname)
  p.parent.mkdir(exist_ok=True)
  p.write_text(fname + "\n")
