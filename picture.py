class Picture:
    """A Picture class"""

    def __init__(self, filename, size, description):
        self.filename = filename
        self.size = size
        self.description = description

    @property
    def info(self):
        return '{}{}{}'.format((self.filename, self.size, self.description))