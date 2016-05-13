import requests
import json
import loggdetails


class ManagedSys():
    def __init__(self):
        self.logfile = loggdetails.logzfile()
        fileobject = open(self.logfile, 'r+')
        loggdetails.deleteContent(fileobject)
        self.desc = "ManagedSystems-Test"
        self.datype = {'Content-type': 'application/json'}
        self.fullpath = self._url('/Auth/SignAppin')
        self.headers = {'Authorization': 'PS-Auth key=004FFC75-565B-41D2-ABA4-12B76CD331A7; runas=stacia;'}
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    #creates url
    def _url(self, path):
        fullpath = 'https://bi-serv/eEye.RetinaCS.Server/api/public/v3' + path
        return fullpath


#Returns all managed systems
    def get_MngSys(self):
        url=self._url('/ManagedSystems')
        self.session.post(self.fullpath,verify=False)#sign in as authorized user
        response=self.session.get(url)
        loggdetails.logg(self.logfile, response, mess=response.text, desc=self.desc)


    #Returns a Managed System by ID.
    def get_MngSys_by(self,mgs_id):
        url = self._url('/ManagedSystems/{}'.format(mgs_id))
        self.session.post(self.fullpath, verify=False)
        response = self.session.get(url)
        loggdetails.logg(self.logfile, response, mess=response.text, desc=self.desc)


    #Returns a Managed System for the Asset referenced by ID.
    def get_Mngs_Ass_by(self,ass_id):
        url = self._url('/Assets/{}/ManagedSystems'.format(ass_id))
        self.session.post(self.fullpath, verify=False)
        response = self.session.get(url)
        loggdetails.logg(self.logfile, response, mess=response.text, desc=self.desc)

     #Returns a list of Managed Systems auto-managed by the Functional Account referenced by ID.
    def get_FunAcc_by(self,func_id):
        url = self._url('/FunctionalAccounts/{}/ManagedSystems'.format(func_id))
        self.session.post(self.fullpath, verify=False)
        response = self.session.get(url)
        loggdetails.logg(self.logfile, response, mess=response.text, desc=self.desc)


    #Creates a Managed System for the Asset referenced by ID.
    def cre_MngSys_by(self,asset_id):
        url = self._url('/Assets/{}/ManagedSystems'.format(asset_id))
        self.session.post(self.fullpath, verify=False)
        response = self.session.post(url,headers=self.datype)
        loggdetails.logg(self.logfile, response, mess=response.text, desc=self.desc)


        #Deletes a Managed System (unmanages the associated Asset) by ManagedSystem ID.
    def del_MSys_by(self, mnsys_id):
        url = self._url('/ManagedSystems/{}'.format(mnsys_id))
        self.session.post(self.fullpath, verify=False)
        response = self.session.delete(url)
        loggdetails.logg(self.logfile, response, mess=response.text, desc=self.desc)


Msys=ManagedSys()
Msys.get_MngSys()


