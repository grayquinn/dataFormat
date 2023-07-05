def transpose_file_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().split()

    transposed_data = [data[i:i+25] for i in range(0, len(data), 25)]

    with open(file_path, 'w') as file:
        for row in transposed_data:
            file.write(' '.join(row) + '\n')

    print("Data transposed and saved successfully.")

# Usage example:
transpose_file_data('path/to/your/file.txt')