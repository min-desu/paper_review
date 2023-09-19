import os

if __name__ == "__main__":
    os.system("python -m cProfile -o result.prof main.py text1.txt text2.txt output.txt")
    os.system("snakeviz result.prof")