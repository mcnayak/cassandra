from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query  import tuple_factory



cloud_config= {
        'secure_connect_bundle': 'secure-connect-learndtx.zip'
}
auth_provider = PlainTextAuthProvider('chandra', 'Welcome1')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()
session.row_factory = tuple_factory

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")

shows = session.execute("SELECT * FROM simpleds.movies_and_tv LIMIT 5 ")

for show in shows:
     print(show[5] + ' made ' + show[10]);
    

try:
    session.execute("INSERT INTO simpleds.movies_and_tv (show_id,director,title) values (08022020,'Rajamouli','Baahubali')")

except Exception as e:
    print(e)
    print('Failure')
else:
    print('New Row Inserted')
finally: 
    cluster.shutdown()
    session.shutdown()