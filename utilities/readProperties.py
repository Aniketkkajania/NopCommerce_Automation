import configparser
import random 
import string 

config = configparser.RawConfigParser()

config.read(".//Configurations/config.ini")

class ReadConfig:

    @staticmethod
    def random_mail_generator():
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(8)) + "@gmail.com"
    
    @staticmethod #if we use @staticmethod we can directly get this function data without needing to create the object of class
    def getApplicationURL():
        base_URL = config.get('common data', 'BASE_URL')
        return base_URL
    
    @staticmethod
    def getUseremail():
        username = config.get('common data', 'USERNAME')
        return username 
    
    @staticmethod
    def getPassword():
        password = config.get('common data', 'PASSWORD')
        return password