"""Module providing json I/O"""
import json

class Persistent:
    '''Class used for json input/output'''

    @staticmethod
    def serjson(path, obj):
        '''Turns object into json'''
        dic = obj
        try:
            with open(path, 'w', encoding='UTF-8') as file:
                json.dump(dic, file, indent=4)
        except IOError as error:
            print(error) #  visible only if console is open
        finally :
            if file :
                file.close()

    @staticmethod
    def resjson(path):
        '''Turns json into object'''
        file = None
        dic = None
        try :
            with open(path, 'br') as file:
                temp = json.load(file)
            if temp and isinstance(temp, dict):
                dic =  temp
        except IOError as error :
            print(error) #  visible only if console is open
        finally:
            if file :
                file.close()
        return dic
                