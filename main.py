import os

TEXT = "I calculated a 97% chance of winning, which means I was wrong in the most statistically confident way possible."

assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
