import os
import sys

if len(sys.argv) < 2:
    print("Usage: python split_unityweb.py <file> [chunk_mb]")
    sys.exit(1)

INPUT_FILE = sys.argv[1]
CHUNK_MB = int(sys.argv[2]) if len(sys.argv) > 2 else 20
CHUNK_SIZE = CHUNK_MB * 1024 * 1024

def split_file(filename, chunk_size):
    size = os.path.getsize(filename)
    index = 0

    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break

            out = f"{filename}.part{index}"
            with open(out, "wb") as w:
                w.write(chunk)

            print(f"Wrote {out} ({len(chunk)//1024//1024} MB)")
            index += 1

    print(f"\nDone! {index} parts created.")

split_file(INPUT_FILE, CHUNK_SIZE)
