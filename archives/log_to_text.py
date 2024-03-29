class Tee:
    def __init__(self, *files):
        self.files = files

    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush()

    def flush(self):
        for f in self.files:
            f.flush()

#
# in file printing:
# import sys
# import THIS_FILE_NAME
# log_file_path = "save_logs.txt"
# log_file = open(log_file_path, "w")
# sys.stdout = Tee(sys.stdout, log_file)
#
# read file:
# filename = r"n_r_q_n_iter.txt"
# try:
#     with open(filename, "r") as file:
#         data_text = file.read()
# except FileNotFoundError:
#     print(f"filename{filename} not found")


