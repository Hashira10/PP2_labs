def file_lengthy(fname, cnt):
    f = open(fname, "r")
    for i in enumerate(f):
        cnt += 1
    print(cnt)
file_lengthy("test.txt", 0)