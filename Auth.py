import requests
import json
import loggdetails




class Auth():

    def __init__(self):
        self.logfile = loggdetails.logzfile()
        fileobject = open(self.logfile, 'r+')
        loggdetails.deleteContent(fileobject)
        self.desc = "Auth-Test"
        self.datype = {'Content-type': 'application/json'}
        self.fullpath = self._url('/Auth/SignAppin')

        self.headers = {'Authorization': 'PS-Auth key=004FFC75-565B-41D2-ABA4-12B76CD331A7; runas=stacia;'}
        self.session = requests.Session()
        self.session.headers.update(self.headers)



    def _url(self, path):
        fullpath = 'https://bi-serv/eEye.RetinaCS.Server/api/public/v3' + path
        return fullpath

    def _signin(self):
        response = self.session.post(self.fullpath, verify=False)
        self.data = str(response)
        d = json.loads(response.text)
        loggdetails.logg(self.logfile, mess="Signed in as" + " " + d['UserName'])
        loggdetails.logg(self.logfile, response, response.text,desc=self.desc)

    def _signout(self):
        url = self._url('/Auth/Signout')
        self.session.post(self.fullpath, verify=False)
        response=self.session.post(url,verify=False)
        loggdetails.logg(self.logfile, response, response.text, desc=self.desc)





auth_obj=Auth()
auth_obj._signout()
#auth_obj._signin()
