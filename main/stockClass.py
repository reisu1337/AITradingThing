class Stock:
    __filepath = None
    __dataframe = None

    def __init__(self):
        pass

    def setFilePath(self, filepath):
        self.__filepath = filepath

    def setDataFrame(self, dataframe):
        self.__dataframe = dataframe

    def getFilePath(self):
        return self.__filepath

    def getDataFrame(self):
        return self.__dataframe
