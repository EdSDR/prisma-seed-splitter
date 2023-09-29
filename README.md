# Prisma File Splitter Script

This script allows you to split a large prisma seed file into multiple smaller seeds, each containing a specified number of lines.

## Installation

1. Ensure you have Python installed on your system.
2. Clone or download this repository.
3. Place the input file you want to split in a location accessible by the script.

## Usage

Run the script with the following command:

```bash
python script.py input_file lines_per_file
```

## Example

Suppose you have a file named `data.txt` with 5000 lines and you want to split it into files with 1000 lines each.

Run the following command:

```bash
python3 script.py data.txt 1000

```

## Author

Ed Castro (@EdSDR)
