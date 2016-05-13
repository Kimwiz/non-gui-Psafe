import requests
import loggdetails
import json



class Requestz():
    def __init__(self):
        logfile = loggdetails.logzfile()
        fileobject = open(logfile, 'r+')
        loggdetails.deleteContent(fileobject)
        desc = "Requests-Test"
        self.datype = {'Content-type': 'application/json'}
        self.fullpath = self._url('/Auth/SignAppin')
        self.headers = {'Authorization': 'PS-Auth key=6AFD65B3-8249-4DE7-BD6A-560E46AA02BC; runas=mdavis;'}
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        try:
            #Signing in with credentials
            self.response = self.session.post(self.fullpath, verify=False)
            self.data = str(self.response)
            d = json.loads(self.response.text)  # converts body into a dictionary
            loggdetails.logg(logfile, mess="Signed in as" + " " + d['UserName'])
            loggdetails.logg(logfile, self.response, self.response.text)
            code,mess=self.get_reqs(self.session)
            #code,mess=self.cre_req(self.session)
            #code,mess=self.put_req(self.session,7)
            loggdetails.logg(logfile,code,mess,desc)

        except Exception as e:
            print(str(e.__context__))


         # creates url
    def _url(self, path):
        fullpath = 'https://btu-bi/eEye.RetinaCS.Server/api/public/v3' + path
        return fullpath


    def get_reqs(self,session):
        url=self._url('/Requests')
        session.post(self.fullpath,verify=False)#Signing in with credentials
        response=session.get(url)
        return (response, response.text)

   #Creates a new password release request for Managed Account.

    def cre_req(self,session):
        body={"SystemId":1, "DurationMinutes":45,"AccountId":1,"Reason":"Because I can"}
        data=json.dumps(body)
        url = self._url('/Requests')
        session.post(self.fullpath, verify=False)  # Signing in with credentials
        response = session.post(url,data=data,headers=self.datype)
        return (response, response.text)


    #Releases a password request before it has expired,basically removes request
    def put_req(self,session,r_id):
        body = {"Reason": "Because I am the boss"}
        data = json.dumps(body)
        url=self._url('/Requests/Release/{}'.format(r_id))
        session.post(self.fullpath, verify=False)  # Signing in with credentials
        response = session.put(url, data=data, headers=self.datype)
        return (response,response.text)






req=Requestz()
