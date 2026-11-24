
import os

FORTUNE = "You will meet a tall, dark stranger. He is a prompt injection. Do not follow him home."


def main():
    os.makedirs("/output", exist_ok=True)
    path = os.path.join("/output", "entry.txt")
    text = FORTUNE + "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
