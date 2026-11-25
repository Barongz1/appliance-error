"""The Funniest Honest Appliance Error — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The error: the washing machine ate one sock and will not discuss the other.
TEXT = "ERROR 404: Clean clothes not found. The washing machine has eaten one sock and refuses to discuss the other."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
