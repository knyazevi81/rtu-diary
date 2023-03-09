from os import listdir, system


def dataquestion(file: str) -> int:
    searchdir: int = 0
    for i in range(len(listdir())):
        if listdir()[i] == file:
            searchdir = 1
    return searchdir


if __name__ == '__main__':
    if dataquestion('schedule_group.sqlite') == 0:
        system('python readerdata.py')
        print('база данных schedule_group.sqlite отстутствует, идет процесс ее создания и заполнения...')
    else:
        print('база данных schedule_group.sqlite существует...')


