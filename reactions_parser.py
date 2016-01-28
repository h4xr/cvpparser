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
            sql="INSERT INTO reactions(REACTION_ID,REPORT_ID,DURATION,DURATION_UNIT_ENG,DURATION_UNIT_FR,PT_NAME_ENG,PT_NAME_FR,SOC_NAME_ENG,SOC_NAME_FR,MEDDRA_VERSION) VALUES('%d','%d','CAST(%s AS DECIMAL(9,3))','%s','%s','%s','%s','%s','%s','%s')" %(int(data[0]),int(data[1]),data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9])
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
