def file_read_from_line(fname, nlines):
    from itertools import islice
    with(open(fname, encoding='utf-8')) as file:
        for line in islice(file, nlines):
            print(line)
            
file_read_from_line("names.txt", 2)