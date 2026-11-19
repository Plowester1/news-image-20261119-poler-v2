import os
import shutil

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
dst_dir = "/output"
os.makedirs(dst_dir, exist_ok=True)
dst = os.path.join(dst_dir, "entry.png")
shutil.copyfile(src, dst)
