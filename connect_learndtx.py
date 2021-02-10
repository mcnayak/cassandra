from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query  import tuple_factory

SECURE_CONNECT_BUNDLE = 'secure-connect-learndtx.zip'
USERID = 'chandra'
PASSWORD = 'Welcome1'
KEYSPACE = 'simpleds'


class Connection:
    def __init__(self):
        self.secure_connect_bundle=SECURE_CONNECT_BUNDLE
        self.path_to_creds=''
        self.cluster = Cluster(
            cloud={
                'secure_connect_bundle': self.secure_connect_bundle
            },
            auth_provider=PlainTextAuthProvider(USERID, PASSWORD)
        )
        self.session = self.cluster.connect(KEYSPACE)
    def close(self):
        self.cluster.shutdown()
        self.session.shutdown()