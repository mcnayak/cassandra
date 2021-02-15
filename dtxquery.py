from connect_learndtx import Connection
from cassandra.query  import tuple_factory


try:
    connection = Connection()
    shows = connection.session.execute(
        "SELECT * FROM simpleds.movies_and_tv ORDER BY release_year LIMIT 5"
    )
    for show in shows:
     print(show[5] + ' made ' + show[10]);     

except Exception as e:
    print(e)
    print('Failure')
else:
    print('5 Top Shows displayed')
finally:
    connection.close()


