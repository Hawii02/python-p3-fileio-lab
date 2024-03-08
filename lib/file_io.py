# def write_file(file_name, file_content):
#    with open(f'lib/{file_name}.txt', mode ='w', encoding = 'utf-8') as file:
#     file.write(file_content)

# def append_file(file_name, append_content):
#     with open(f'lib/{file_name}.txt', mode='a', encoding='utf-8') as file:
#         file.write(append_content)

# def read_file(file_name):
#     with open(f'lib/{file_name}.txt', encoding='utf-8') as file:
#         content = file.read()
#     return content

def write_file(file_name, file_content):
    with open(str (file_name) + '.txt' , 'w')as f:
        f.write(file_content)

def append_file(file_name, append_content):
    with open(str (file_name) + '.txt', 'a')as f:
        f.write(append_content)

def read_file(file_name):
    with open(str (file_name)+ '.txt', 'r')as f:
        return f.read()