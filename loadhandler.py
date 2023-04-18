import pickle
import json     
class Persistent:
    
    @staticmethod
    def serialize(path, obj):
        file = None      
        try:
            file = open(path, 'bw')
            # source, destination
            pickle.dump(obj, file)
            
        except IOError as error:  
            print(error) #  visible only if console is open
        finally :
            if file :
                file.close()
                

    @staticmethod
    def restore(path, cls):
        file = None
        obj = None
        try :
            file = open(path, 'br')
            g = pickle.load(file)
            if g and isinstance(g, cls):
                obj = g
                
        except IOError as error :                             
            print(error) #  visible only if console is open
        finally:
            if file :
                file.close()
        
        return obj
                
    @staticmethod           
    def serjson(path, obj):
        d = obj
        try:
            file = open(path, 'w')
            json.dump(d, file, indent=4)
            
        except Exception as error:  
            print(error) #  visible only if console is open
        finally :
            if file :
                file.close()            

    @staticmethod
    def resjson(path):
        file = None
        d = None
        try :
            file = open(path, 'br')
            g = json.load(file)
            if g and isinstance(g, dict):
                d =  g
        except IOError as error :                             
            print(error) #  visible only if console is open
        finally:
            if file :
                file.close()
        return d
                