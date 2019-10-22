


class InputFormatter:
    @staticmethod
    def formatToCaseSensitiveLower(inputString):
        # convert string to lower case format
        if (isinstance(inputString, str)):
            return inputString.lower()
        else:
            return None

    @staticmethod
    def formatToCaseSensitiveUpper(inputString):
        # convert string to upper case format
        if (isinstance(inputString, str)):
            return inputString.upper()
        else:
            return None