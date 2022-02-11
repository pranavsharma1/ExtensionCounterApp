import json

class ExtensionCounter:
    '''
    A class to represent a extension counter

    Attributes
    ---------
    None

    Methods
    ------
    get_extension_counter(json_list)
        returns the count of each extension with a unique filename
    '''
    def get_extension_count(self, json_list):
        '''
        This method iterates over the json record one at a time. Checks the name of of the files, maintains the count of
        extensions seen. Finally, returns the result in a dictionary.

        :param jsonList: This is a list of json records after reading the log file
        :return: A dictionary with the count of extensions seen having unique filename.
        '''

        filename_set = set()
        extension_map = {}

        for json_element in json_list:
            try:
                filename = json.loads(json_element)['nm']
            except KeyError as e:
                print(f'nm key not found in the Json element: {json_element}')
                print(e)
                raise

            if filename not in filename_set:
                filename_set.add(filename)
                extension = filename.split(".")[-1]
                if extension not in extension_map:
                    extension_map[extension] = 1
                else:
                    extension_map[extension] = extension_map[extension] + 1


        return extension_map
