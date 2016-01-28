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
            sql="INSERT INTO reports(REPORT_ID,REPORT_NO,VERSION_NO,DATRECEIVED,DATINRECEIVED,MAH_NO,REPORT_TYPE_CODE,REPORT_TYPE_ENG,REPORT_TYPE_FR,GENDER_CODE,GENDER_ENG,GENDER_FR,AGE,AGE_Y,AGE_UNIT_ENG,AGE_UNIT_FR,OUTCOME_CODE,OUTCOME_ENG,OUTCOME_FR,WEIGHT,WEIGHT_UNIT_ENG,WEIGHT_UNIT_FR,HEIGHT,HEIGHT_UNIT_ENG,HEIGHT_UNIT_FR,SERIOUSNESS_CODE,SERIOUSNESS_ENG,SERIOUSNESS_FR,DEATH,DISABILITY,CONGENITAL_ANOMALY,LIFE_THREATENING,HOSP_REQUIRED,OTHER_MEDICALLY_IMP_COND,REPORTER_TYPE_ENG,REPORTER_TYPE_FR,SOURCE_CODE,SOURCE_ENG,SOURCE_FR) VALUES('%d','%s','%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','CAST(%s AS DECIMAL(6,3))','CAST(%s AS DECIMAL(6,3))','%s','%s','%s','%s','%s','CAST(%s AS DECIMAL(7,3))','%s','%s','CAST(%s AS DECIMAL(7,3))','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(int(data[0]),data[1],int(data[2]),data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],data[21],data[22],data[23],data[24],data[25],data[26],data[27],data[28],data[29],data[30],data[31],data[32],data[33],data[34],data[35],data[36],data[37],data[38]);
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
