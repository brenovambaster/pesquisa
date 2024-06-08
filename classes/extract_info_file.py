class FileProcessor:
    """
    A class to process files.

    Attributes:
    file_path : str
        The path to the file to be processed

    Methods:
    read_file():
        Reads a file and returns its lines.
    process_line(line):
        Processes a line and returns a dictionary.
    parse_list(value):
        Parses a string list and returns a list.
    process_file():
        Processes a file and returns a list of dictionaries.
    """

    def __init__(self, file_path):
        """
        Constructs all the necessary attributes for the FileProcessor object.

        Parameters
        ----------
            file_path : str
                the path to the file to be processed
        """
        self.file_path = file_path

    def read_file(self):
        """
        This method reads a file and returns its lines as a list.

        Returns:
        list: A list of lines in the file.

        Raises:
        IOError: If the file cannot be opened.
        """
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
            return lines
        except IOError:
            print(f"Error opening file: {self.file_path}")
            return []

    def process_line(self, line):
        """
        This method processes a line from the file and returns a dictionary of key-value pairs.

        Parameters:
        line (str): The line to be processed.

        Returns:
        dict: A dictionary where the keys are the identifiers before the '=' character and the values are the corresponding
        values after the '=' character.
        """
        line_data = {}
        parts = line.strip().split('|')

        for part in parts:
            key, value = part.split('=', 1)
            key = key.strip()
            value = value.strip()

            if value.startswith('[') and value.endswith(']'):
                value = self.parse_list(value)
            elif value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif '.' in value:
                value = float(value)
            else:
                value = int(value)

            line_data[key] = value

        return line_data

    def parse_list(self, value):
        """
        This method parses a string representation of a list and returns a list of integers or floats.

        Parameters:
        value (str): The string representation of a list.

        Returns:
        list: A list of integers or floats.
        """
        value = value[1:-1].split(',')
        return [float(v) if '.' in v else int(v) for v in value]

    def process_file(self):
        """
        This method processes a file and returns a list of dictionaries. Each dictionary represents a line in the file.

        Returns:
        list: A list of dictionaries. Each dictionary represents a line in the file.
        """
        lines = self.read_file()
        data = [self.process_line(line) for line in lines]
        return data


