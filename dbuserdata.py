class userdata():
    user='root'
    password='root'
    host='localhost'
    port='3306'
    database='mytaildb01'

    def __init__(self,user,password,host,port,database) -> None:
        self.user=user
        self.password=password
        self.host=host
        self.port=port
        self.database=database

    def getdata(self) :
        return [self.user,self.password,self.host,self.port,self.database]
    
    # data=getdata()
    print(user,password,host,port,database)