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
            #for i,s in enumerate(data):
            if(data[2]==''):
                data[2]='0'
            print data
            sql="INSERT INTO report_drug(REPORT_DRUG_ID,REPORT_ID,DRUG_PRODUCT_ID,DRUGNAME,DRUGINVOLV_ENG,DRUGINVOLV_FR,ROUTEADMIN_ENG,ROUTEADMIN_FR,UNIT_DOSE_QTY,DOSE_UNIT_ENG,DOSE_UNIT_FR,FREQUENCY,FREQ_TIME,FREQUENCY_TIME_ENG,FREQUENCY_TIME_FR,FREQ_TIME_UNIT_ENG,FREQ_TIME_UNIT_FR,THERAPY_DURATION,THERAPY_DURATION_UNIT_ENG,THERAPY_DURATION_UNIT_FR,DOSAGEFORM_ENG,DOSAGEFORM_FR) VALUES('%d','%d','%d','%s','%s','%s','%s','%s','CAST(%s AS DECIMAL(20,9))','%s','%s','CAST(%s AS INT(3))','CAST(%s AS DECIMAL(10,5))','%s','%s','%s','%s','CAST(%s AS DECIMAL(10,5))','%s','%s','%s','%s')" %(int(data[0]),int(data[1]),int(data[2]),data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21])
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
