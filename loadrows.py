from connect_learndtx import Connection
import uuid

try:
    connect = Connection()
    connect.session.execute("INSERT INTO simpleds.movies_and_tv (show_id, director,title) values (15022021,'%s','%s')")
except Exception as e:
    print(e)
    print('Failure')
else:
    print('New Row Inserted')
finally: 
    connect.close()



#cursor.execute('SELECT * FROM salesforce.contact WHERE SFID = %(rec_id)s',{'rec_id':'00305000007YAJqAAO'})
    