import os, sys, pathlib

EXE = pathlib.Path(__file__).resolve()
COUNTER = EXE.with_name('.' + EXE.stem + '.cnt')   # 隐藏文件 .xxx.cnt

MAX_RUN = 5          # 允许次数

def _read():
    return int(COUNTER.read_text()) if COUNTER.exists() else 0

def _write(n):
    COUNTER.write_text(str(n))

# 主逻辑
count = _read()
if count >= MAX_RUN:
    sys.exit('试用次数已用完')
_write(count + 1)

print(f'第 {count+1} 次运行，还可运行 {MAX_RUN-count-1} 次')
# ↓↓↓ 你的真正代码写在这里
