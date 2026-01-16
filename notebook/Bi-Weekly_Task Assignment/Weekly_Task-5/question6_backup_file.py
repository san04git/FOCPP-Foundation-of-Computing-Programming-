import sys
import shutil

def main():
    if len(sys.argv) < 2:
        print("Please provide a filename as argument.")
        return

    original = sys.argv[1]
    backup = original + ".bak"

    try:
        shutil.copyfile(original, backup)
        print(f"Backup created: {backup}")
    except FileNotFoundError:
        print(f"File not found: {original}")
    except Exception as e:
        print(f"Error creating backup: {e}")

if __name__ == "__main__":
    main() 