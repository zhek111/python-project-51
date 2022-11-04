def write_data_to_file(data, file, mode):
    with open(file, mode) as file:
        file.write(data)
