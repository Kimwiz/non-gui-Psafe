import requests
import json
import loggdetails

# The test below is tests for import queues '''

class Imports():

    def __init__(self):
        self.logfile = loggdetails.logzfile()
        fileobject = open(self.logfile, 'r+')
        loggdetails.deleteContent(fileobject)
        self.desc = "Imports-Test"
        self.datype = {'Content-type': 'application/json'}
        self.fullpath = self._url('/Auth/SignAppin')
        self.headers = {'Authorization': 'PS-Auth key=004FFC75-565B-41D2-ABA4-12B76CD331A7; runas=stacia;'}
        self.session = requests.Session()#create session
        self.session.headers.update(self.headers) #update the session with the required headers



    def _url(self, path):
        fullpath = 'https://bi-serv/eEye.RetinaCS.Server/api/public/v3' + path
        return fullpath


     #Queues a Password Safe Import or imports an xml file
    def post_imports(self):
        file=open("PasswordSafe.xml",'r')
        filecontents=file.read()
        bar = [ord(item) for item in str(filecontents)] #list of bytes from file
        print(bar)
        body = {'WorkgroupID': 3, 'FileName':'PasswordSafe.xml','FileContents':bar}
        data = json.dumps(body)
        url = self._url('/Imports')
        self.session.post(self.fullpath, verify=False)#Signing in
        response = self.session.post(url, data=data, headers=self.datype)
        print(response)
        loggdetails.logg(self.logfile, response, response.text, desc=self.desc)





impobj=Imports()
impobj.post_imports()


















c=Imports()
#c.post_imports()