def write_data(data, file, type):
    with open(file, type) as file:
        file.write(data)
