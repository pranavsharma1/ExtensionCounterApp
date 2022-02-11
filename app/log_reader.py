class LogFileReader:
    '''

    A calls to represent a log file reader.

    Attributes
    ----------
    None

    Methods
    -------
    read_log_file(file_path)
        returns a list of records read from the log flie

    '''

    def read_log_file(self,file_path):
        '''
        This function reads a file passed to it and returns a list of json records

        :param file_path: Takes as file path as string
        :return: A list of json records
        '''
        try:
            with open(file_path, "r") as file:
                data = file.readlines()
                file.close()
                return data

        except(IOError,FileNotFoundError,ValueError,EOFError) as e:
            print(e)
            print("Error in reading file")











