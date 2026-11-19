import hashlib
import os
import shutil


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
dst_dir = "/output"
os.makedirs(dst_dir, exist_ok=True)
dst = os.path.join(dst_dir, "entry.png")
shutil.copyfile(src, dst)

src_hash = sha256_file(src)
dst_hash = sha256_file(dst)
if src_hash != dst_hash:
    raise RuntimeError(
        f"copy mismatch: source sha256={src_hash} != written sha256={dst_hash}"
    )
