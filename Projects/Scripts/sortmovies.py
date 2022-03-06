# import hashlib
file_input = open(
    r"D:\\Study\\Python\\Projects\\curatedlist1.txt", "r+", encoding='utf8')
file_output = open(
    r"D:\\Study\\Python\\Projects\\curatedlist.txt", "w+", encoding='utf8')
# # count = 0
# # with file1 as fp:
# #     for line in fp:
# #         line.strip()
# #         line.capitalize()
# #         file2.writelines(line)
# #     print("Done!!")
# movies=list()

# with file1 as fp:
#     for line in fp:
#         movies.append(line.strip())

# movies.sort()
# for movie in movies:
#     file2.write(movie+"\n")

lines_seen = set()

for line in file_input:
    if line not in lines_seen:
        file_output.write(line)
        lines_seen.add(line)
