import os

INPUT_FILE = INPUT_FILE = "AVHPort.wasm.code.unityweb"
CHUNK_SIZE = 20 * 1024 * 1024  # 20 MB

def split_file(filename, chunk_size):
    size = os.path.getsize(filename)
    print(f"Splitting {filename} ({size / (1024*1024):.2f} MB)")

    with open(filename, "rb") as f:
        index = 0
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break

            out = f"{filename}.part{index}"
            with open(out, "wb") as o:
                o.write(chunk)

            print(f"✔ wrote {out} ({len(chunk) / (1024*1024):.2f} MB)")
            index += 1

    print(f"\nDone! Total parts: {index}")

if __name__ == "__main__":
    split_file(INPUT_FILE, CHUNK_SIZE)
