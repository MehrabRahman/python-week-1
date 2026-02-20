chunk_size = 500

def chunk_writer(size, lines):
    with open('part_' + str(size) + '.txt', 'w') as out:
        out.write(header)
        out.writelines(lines)

with open('hitch3.txt', "r") as file:
    count = 0
    header = file.readline()
    lines = []
    for line in file:
        count += 1
        lines.append(line)
        if count % chunk_size == 0:
            chunk_writer(count // chunk_size, lines)
            lines = []
        if len(lines) > 0:
            chunk_writer((count // chunk_size) + 1, lines)