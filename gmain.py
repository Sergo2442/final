import os


def create_combined_list(directory):
    combined_list = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                combined_list.append([filename, 0, []])
                for line in file:
                    combined_list[-1][2].append(line.strip())
                    combined_list[-1][1] += 1

    return sorted(combined_list, key=lambda x: x[2], reverse=True)


def write_combined_list_to_file(combined_list, output_file):
    with open(output_file, 'w', encoding='utf-8') as last_file:
        for item in combined_list:
            last_file.write(f'File name: {item[0]}\n')
            last_file.write(f'Length: {item[1]} string(s)\n')
            for string in item[2]:
                last_file.write(string + '\n')
            last_file.write('-------------------\n')


def create_file_from_directory(directory, filename):
    combined_list = create_combined_list(directory)
    write_combined_list_to_file(combined_list, filename)


create_file_from_directory("C:\\Users\\HYPERPC\\Desktop\\final", 'result')







