import sys

task_counter = 0


def read_input(file):
    global task_counter
    for line in file:
        task_counter += 1
        # split the line into words
        yield line.split()


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        with open(f'file{task_counter}', 'w') as file:
            for word in words:
                print('%s%s%d' % (word, separator, 1), file=file)
    # Put number of files in stdin for shuffler
    print(task_counter)


if __name__ == "__main__":
    main()
