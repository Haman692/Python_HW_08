with open('pipe.txt', 'r', encoding='utf=8') as file:
    text_file_pipe = file.read().splitlines()
    all_pipe = 0
    for i in range(len(text_file_pipe[-1].replace(' ', ''))):
        all_pipe += 1/int(text_file_pipe[i])
    all_pipe = 60/all_pipe
    with open('time.txt', 'w',encoding='utf=8')as file1:
        file1.write(str(all_pipe))