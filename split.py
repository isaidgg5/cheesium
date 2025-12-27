import os
import sys

# 1. Simplified argument check (only needs file path now)
if len(sys.argv) < 2:
    print("Usage: python split_unityweb.py <file>")
    sys.exit(1)

INPUT_FILE = sys.argv[1]

# 2. Hardcoded to 20 MB
CHUNK_MB = 20
CHUNK_SIZE = CHUNK_MB * 1024 * 1024

def split_file(filename, chunk_size):
    # Safety check: ensure file exists
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        return

    index = 0
    
    try:
        with open(filename, "rb") as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break

                # Naming convention: filename.part0, filename.part1, etc.
                out = f"{filename}.part{index}"
                
                with open(out, "wb") as w:
                    w.write(chunk)

                # Calculate actual size written for the log
                size_mb = len(chunk) / (1024 * 1024)
                print(f"Wrote {out} ({size_mb:.2f} MB)")
                index += 1

        print(f"\nDone! {index} parts created.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    split_file(INPUT_FILE, CHUNK_SIZE)