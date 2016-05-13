import requests
import json
import os
import loggdetails
import csv


class ManagedAcc():
    def __init__(self):
        self.logfile = loggdetails.logzfile()
        fileobject = open(self.logfile, 'r+')
        loggdetails.deleteContent(fileobject)
        self.desc = "ManagedAcc-Test"
        self.datype = {'Content-type': 'application/json'}
        self.fullpath = self._url('/Auth/SignAppin')
        self.headers = {'Authorization': 'PS-Auth key=004FFC75-565B-41D2-ABA4-12B76CD331A7; runas=stacia;'}
        self.session = requests.Session()
        self.session.headers.update(self.headers)



        #creates url
    def _url(self, path):
        fullpath = 'https://bi-serv/eEye.RetinaCS.Server/api/public/v3' + path
        return fullpath


    #gets Managed Accounts
    def get_MAccounts(self):
        url=self._url('/ManagedAccounts')
        self.session.post(self.fullpath, verify=False)
        response=self.session.get(url)
        loggdetails.logg(self.logfile, response, mess=response.text, desc=self.desc)

    #Returns a requestable Managed Account by Managed System name and Managed Account name.
    def get_MAccounts_by(self,sysname,accountname):
        url = self._url('/ManagedAccounts?systemName=%s&accountName=%s' %(sysname,accountname))
        self.session.post(self.fullpath, verify=False)
        response = self.session.get(url)
        loggdetails.logg(self.logfile, response, mess=response.text, desc=self.desc)

       #Returns a Managed Account by ID.
    def get_MnAccounts_by(self,m_id):

        url = self._url('/ManagedAccounts/{}'.format(m_id))
        self.session.post(self.fullpath, verify=False)
        response = self.session.get(url)
        loggdetails.logg(self.logfile, response, mess=response.text, desc=self.desc)


    #Returns a list of Managed Accounts by Managed System ID.
    def get_MnSystems_by(self,sys_id):
        url=self._url('/ManagedSystems/{}/ManagedAccounts'.format(sys_id))
        self.session.post(self.fullpath, verify=False)
        response = self.session.get(url)
        loggdetails.logg(self.logfile, response, mess=response.text, desc=self.desc)


        #POST(Creates a new Managed Account in the Managed System referenced by ID.)
    def creT_MnAcc(self,mng_id):
        body={"AccountName":"leaseMay_local","Password":"btlab16*"}
        data = json.dumps(body)
        url = self._url('/ManagedSystems/{}/ManagedAccounts'.format(mng_id))
        self.session.post(self.fullpath, verify=False)
        response = self.session.post(url,data=data,headers=self.datype)
        loggdetails.logg(self.logfile, response, mess=response.text, desc=self.desc)



    #deletes managed account by managedaccount id

    def del_MnAcc_by(self,mng_id):
        url = self._url('/ManagedAccounts/{}'.format(mng_id))
        self.session.post(self.fullpath, verify=False)
        response = self.session.delete(url)
        loggdetails.logg(self.logfile, response, mess=response.text, desc=self.desc)


        # Deletes a Managed Account by Managed System ID and Managed Account name.
    def del_MngAcc_by(self,sysid,accntname):
        url = self._url('/ManagedSystems/{}/ManagedAccounts/{}'.format(sysid,accntname))
        self.session.post(self.fullpath, verify=False)
        response = self.session.delete(url)
        loggdetails.logg(self.logfile, response, mess=response.text, desc=self.desc)





manobj=ManagedAcc()
manobj.get_MAccounts()


