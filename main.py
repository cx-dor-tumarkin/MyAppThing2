import sys
from step1 import step1

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <command>")
        sys.exit(1)
    cmd = sys.argv[1]
    step1(cmd)

if __name__ == "__main__":
    main()
