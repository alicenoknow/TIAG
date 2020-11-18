with open("test.txt") as file_in:
    with open("graph.dot", "w") as graph:

        line = file_in.readline()
        while line != "\n":
            graph.write(line)
            line = file_in.readline()

        line = file_in.readline()
        n = int(line)
        with open("osadzenia.txt", "w") as settleFile:

            for i in range(n):
                name_L = "L%s.dot" % str(i)
                name_P = "P%s.dot" % str(i)
                with open(name_L, "w") as file_L:
                    line = file_in.readline()
                    while line != "\n":
                        file_L.write(line)
                        line = file_in.readline()
                with open(name_P, "w") as file_P:
                    line = file_in.readline()
                    while line != "\n":
                        file_P.write(line)
                        line = file_in.readline()
                line = file_in.readline()
                while line != "\n" and line != '':
                    settleFile.write(line)
                    line = file_in.readline()
                settleFile.write("\n")

