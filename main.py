from pathlib import Path
import re

character_file_path = Path.cwd() / "characters.txt"

regex_character_name = "^([0-9])?([A-Z][a-z]+ ){1,}([A-Z][a-z]+-|[A-Z][a-z]+)?([A-Z][a-z]+)|^[A-Z][a-z]+"

data_entry_list = []


def has_int(string):
    if string[0].isdigit():
        string = string[1:]
    elif string[len(string) - 1].isdigit():
        string = string[:len(string) - 1]

    return string


if character_file_path.exists():
    data_list = []
    with character_file_path.open() as character_file:
        for line in character_file.readlines():
            data_list.append(line.strip())

    for entry in data_list:
        entry_list = [re.search("[0-9]", entry).group()]
        character_name = re.search(regex_character_name, entry).group()
        entry_list.append(has_int(character_name))
        actor_name = re.sub(character_name, "", entry)
        entry_list.append(has_int(re.sub("\|", "", actor_name).strip()))
        data_entry_list.append(entry_list)

total_seasons = 0
for data_entry in data_entry_list:
    if data_entry[0].isdigit():
        season_num = int(data_entry[0])
        total_seasons = total_seasons + season_num
average_seasons_per_actor = total_seasons / len(data_entry_list)

input = int(input("Are you grading:\n"
                  "1. Lab A\n"
                  "2. Lab B\n"))

if input == 1:
    print(f'\nThe total seasons of all actors is {total_seasons}\n'
          f'The average season per actor is {average_seasons_per_actor.__round__(2)}')
elif input == 2:
    for data_entry in data_entry_list:
        print(f'Seasons: {data_entry[0]}\n'
              f'Character Name: {data_entry[1]}\n'
              f'Actor Name: {data_entry[2]}\n')
