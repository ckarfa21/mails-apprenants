class read_file:
    def __init__(self, text):
        with open(text, "r", newline=None) as self.file:
            self.lignes = self.file.read().splitlines()