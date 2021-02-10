from connect_learndtx import Connection


try:
    connect = Connection()
    connect.session.execute("INSERT INTO simpleds.movies_and_tv (show_id,director,title) values (08022021,'Rajamouli','Baahubali 2')")
except Exception as e:
    print(e)
    print('Failure')
else:
    print('New Row Inserted')
finally: 
    connect.close()