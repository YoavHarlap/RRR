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


# # write in your specific code
# import sys
# from print_to_txt_file import Tee
# log_file_path = "stamm4.txt"
# log_file = open(log_file_path, "w")
# sys.stdout = Tee(sys.stdout, log_file)
# print("hi")
