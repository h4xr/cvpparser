import MySQLdb as sql
import time

        
def create_query(tb_name,field_num,field_name,field_type,field_range):    
    res=' '
    ls=["CREATE","TABLE"]
    ls.append(tb_name)
    ls.append("(")
    for i in range(field_num):
        ls.append(field_name[i])
        ls.append(field_type[i])
        ls.append("(")
        ls.append(field_range[i])
        ls.append(")")
        if(i==(field_num-1)):
            ls.append(")")
        else:
            ls.append(",")
    query=res.join(ls)
    return query
        
def create_table(csr):
    field_name=[]
    field_type=[]
    field_range=[]
    tb_name=raw_input("Enter the name of the table:")
    print "Enter the number of fields in table:"
    field_num=int(raw_input())
    for i in range(field_num):
        print ("Enter the name of field %d"%(i+1))
        inp=raw_input()
        field_name.append(inp)
        print ("Enter the type of :  %s  ;(VARCHAR OR INT)"%(inp))
        field_t=raw_input()
        field_type.append(field_t)
        print ("Enter the limit of digits or characters")
        field_lim=raw_input()
        field_range.append(field_lim)
        print ""
    qry=create_query(tb_name,field_num,field_name,field_type,field_range)
    csr_execute(qry,csr)

def csr_execute(qry,cursor):
    print qry    
    try:
        cursor.execute(qry)
        print "Query Succesfully Executed"
        print ""
        begin(cursor)
    except:
        print "Error in query detected!!"
        print "Try againnn"
        tb_insert(cursor)
        
def db_connect(db_host,db_user,db_pass,db_name):
    try:
        #db=sql.connect("%s","%s","%s","%s"%(db_host,db_user,db_pass,db_name))
        db=sql.connect("localhost","root","MYNET696",db_name)
        print "Succesfully Connected"
        return db
    except:
        print "Error Occured"
        print "Try again"
        db_connect(db_host,db_user,db_pass,db_name)
               
def get_db_cursor(db):
    try:
        return db.cursor()
    except:
        print "Error Occured"

def insert_qry(qry,csr):
    try:
        csr.execute(qry)
        print "Query Executed"
    except:
        print "Insert Query Error"

def tb_insert1(siz,tb_field1):
    tb_data1=[]
    for i in range(0,siz):
        inp=str(raw_input("Enter field %d Data :  "%(i+1)))
        tb_data1.append(inp)
    return tb_data1
        
def tb_insert(cursor):
    tb_data=[]    
    tb_field=[]
    tb_data=[]
    ls=[]    
    tb_name=str(raw_input("Enter the table name:"))
    print "Enter the number of fields in table:"
    field_num=int(raw_input())
    for i in range(field_num):
        print ("Enter the name of field %d"%(i+1))
        inp=raw_input()
        tb_field.append(inp)
    print tb_field
    print "Please check the fields and press 1 to confirm"
    rep=int(raw_input())
    if(rep == 1):
        print "Insert Data"
        tb_data=tb_insert1(len(tb_field),tb_field)
    else:
        tb_insert(cursor)
    ls=["INSERT","INTO",]
    ls.append(tb_name)
    ls.append("(")
    for i in range(len(tb_field)):
        ls.append(tb_field[i])
        if(i == (len(tb_field)-1)):
            ls.append(")")
        else:
            ls.append(",")
    ls.append("VALUES")
    ls.append("(")
    for i in range(len(tb_data)):
        ls.append("'")        
        ls.append(tb_data[i])
        ls.append("'")
        if(i == (len(tb_data)-1)):
            ls.append(")")
        else:
            ls.append(",")
    res = ' '
    qry=res.join(ls)
    print qry
    insert_qry(qry,cursor)

def begin(cursor):
    print "1. CREATE A TABLE"
    print "2. INSERT DATA INTO EXISTING TABLE"
    print "3. EXIT"
    choice=int(raw_input("Enter Your choice:"))
    if(choice == 1):
        create_table(cursor)        
    else:
        tb_insert(cursor)
        

#def insert_data(tb_nam):    
start_time=time.time()
print "This is a GENERALISE DATABASE PARSING PROGRAM:"
db_host1=str(raw_input("Enter the host for database: "))
db_user1=str(raw_input("Enter the username for database: "))
db_pass1=str(raw_input("Enter the password for database: "))
db_name=str(raw_input("Enter the Name of Database going to be used:"))
db=db_connect(db_host1,db_user1,db_pass1,db_name)    
cursor=get_db_cursor(db)
begin(cursor)
db.commit()
db.close()
print "Total Time taken in seconds: %d" % ((time.time()-start_time))





