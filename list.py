import os
import sys

# 1. Check for arguments
if len(sys.argv) < 2:
    print("Usage: python list.py (path)")
    sys.exit(1)

TARGET_DIR = sys.argv[1]

def list_files_with_sizes(directory):
    # 2. Check if directory exists
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        return

    print(f"Scanning: {directory}\n")
    
    # Header for readability
    # < under 50 aligns left, >10 aligns right for numbers
    print(f"{'Filename':<50} | {'Size (MB)':>10}")
    print("-" * 65)

    try:
        # 3. Scan the directory
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    # Get size in bytes and convert to MB
                    size_bytes = entry.stat().st_size
                    size_mb = size_bytes / (1024 * 1024)
                    
                    # Print formatted: filename truncated if too long, size to 2 decimals
                    # The :<50 formats the name to take up 50 chars of space
                    print(f"{entry.name:<50} | {size_mb:>10.2f} MB")
                    
    except PermissionError:
        print(f"Error: Permission denied accessing '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    list_files_with_sizes(TARGET_DIR)