import sys

from homework.src.wordcount import wordcount


def main() -> None:
    """Main function"""
    if len(sys.argv) != 3:
        print("Usage: python -m homework <input_folder> <output_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    wordcount(folder=input_folder, output_folder=output_folder)


if __name__ == "__main__":
    main()