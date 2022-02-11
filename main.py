from os import path
import json

import log_reader
import extension_counter

if __name__ == '__main__':

    basePath = path.abspath(path.curdir)
    print(basePath)
    jsonList = log_reader.LogFileReader().read_log_file(basePath + '/data/sampleMissingKeyData.json')
    resultDict = {}
    try:
        resultDict = extension_counter.ExtensionCounter().get_extension_count(jsonList)
    except json.decoder.JSONDecodeError as e:
        print("Json does not have proper structure")
        print(e)

    print(resultDict)











