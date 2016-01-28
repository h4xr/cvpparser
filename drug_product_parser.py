import time,MySQLdb
'''
txt to database converter
'''
def read_records(file_path,cursor):
    counter=0
    with open(file_path,"r") as txt_file:
        for line in txt_file:
            line=line.replace('"','').replace("'","").strip('\n')
            data=line.split("$")
            print data
            sql="INSERT INTO drug_product(DRUG_PRODUCT_ID,DRUGNAME) VALUES('%d','%s')" %(int(data[0]),data[1])
            cursor.execute(sql)
            counter+=1
    return counter

def database_connector():
    db=MySQLdb.connect("localhost","root","MYNET696","medcare")
    return db
    
def get_db_cursor(db):
    return db.cursor()
    
def close_db(db):
    db.close()

start_time=time.time()
file_path=input("File path: ")
db=database_connector()
cursor=get_db_cursor(db)
rec=read_records(file_path,cursor)
db.commit()
close_db(db)
print "Total %d records processed in %s seconds" % (rec,(time.time()-start_time))
