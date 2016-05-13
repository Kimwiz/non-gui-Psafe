import requests
import json
import csv
import loggdetails


class UserTest():
    def __init__(self):
        self.logfile = loggdetails.logzfile()
        fileobject = open(self.logfile, 'r+')
        loggdetails.deleteContent(fileobject)
        self.desc="UserTest"
        self.datype = {'Content-type': 'application/json'}
        self.fullpath=self._url('/Auth/SignAppin')
        self.headers={'Authorization':'PS-Auth key=004FFC75-565B-41D2-ABA4-12B76CD331A7; runas=stacia;'}
        self.session=requests.Session()
        self.session.headers.update(self.headers)



    #CSV Filemaker
    def to_csv(self,dres):
        dicx = {}
        keys=dres.keys() #store json data dict keys

        for key in keys:
            dicx[key]=dres[key]

        with open('people.csv', 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerow(dicx)

    #creates url
    def _url(self,path):
        fullpath = 'https://bi-serv/eEye.RetinaCS.Server/api/public/v3' + path
        return fullpath


    def get_U_by_GID(self,gr_id):
        snum = str(gr_id)
        url = self._url('/UserGroups/{}/Users'.format(snum))
        self.session.post(self.fullpath, verify=False)
        response=self.session.get(url,verify=False)
        loggdetails.logg(self.logfile, response, mess=response.text, desc=self.desc)



    def get_U_by_UID(self,user_id):
        snum=str(user_id)
        url=self._url('/Users/{}'.format(snum))
        self.session.post(self.fullpath,verify=False)
        response=self.session.get(url)
        loggdetails.logg(self.logfile, response, mess=response.text, desc=self.desc)

    def create_user_for_group(self,group_id):
        body = {'UserName': 'Madaoo', 'Firstname': 'bazz', 'Lastname': ' Thompson', 'EmailAddress': 'pyhom@btu.local',
                'Password': 'btlab16*'}
        data = json.dumps(body)
        snum = str(group_id)
        url = self._url('/UserGroups/{}/Users'.format(snum))
        self.session.post(self.fullpath, verify=False)
        response = self.session.post(url, data=data, headers=self.datype)
        loggdetails.logg(self.logfile, response, mess=response.text, desc=self.desc)

    def update_user(self,user_id):
        body = {'UserName': 'Madaoo', 'Firstname': 'bazz', 'Lastname': ' Thompson', 'EmailAddress': 'pyhom@btu.local',
                'Password': 'btlab16*'}
        data = json.dumps(body)
        snum = str(user_id)
        url = self._url('/Users/{}'.format(snum))
        self.session.post(self.fullpath, verify=False)
        response=self.session.put(url,data=data,headers=self.datype)
        loggdetails.logg(self.logfile, response, mess=response.text, desc=self.desc)

    def del_user(self,user_id):
        snum=str(user_id)
        url = self._url('/Users/{}'.format(snum))
        self.session.post(self.fullpath, verify=False)
        response = self.session.delete(url)
        loggdetails.logg(self.logfile, response, mess=response.text, desc=self.desc)






Userobj=UserTest()
Userobj.get_U_by_GID(4)