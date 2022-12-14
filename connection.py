import ssl
import configparser
import sqlalchemy

config = configparser.ConfigParser()
config.read('config.ini')

DB_HOST = config['PostgreSQL']['INSTANCE_HOST']  # e.g. '127.0.0.1' ('172.17.0.1' if deployed to GAE Flex)
DB_USER = config['PostgreSQL']['DB_USER']  # e.g. 'my-db-user'
DB_PASS = config['PostgreSQL']['DB_PASS']  # e.g. 'my-db-password'
DB_NAME = config['PostgreSQL']['DB_NAME']  # e.g. 'my-database'
DB_PORT = config['PostgreSQL']['DB_PORT']  # e.g. 5432

def connect_tcp_socket() -> sqlalchemy.engine.base.Engine:

    # [END cloud_sql_postgres_sqlalchemy_connect_tcp]
    connect_args = {}
    db_root_cert = 'pem/server-ca.pem'  # e.g. '/path/server-ca.pem'
    db_cert = 'pem/client-cert.pem'  # e.g. '/path/client-cert.pem'
    db_key = 'pem/client-key.pem'  # e.g. '/path/client-key.pem'

    ssl_context = ssl.SSLContext()
    ssl_context.verify_mode = ssl.CERT_REQUIRED
    ssl_context.load_verify_locations(db_root_cert)
    ssl_context.load_cert_chain(db_cert, db_key)
    connect_args["ssl_context"] = ssl_context

    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL.create(
            drivername="postgresql+pg8000",
            username=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
        ),
        connect_args=connect_args,
        pool_timeout=30,  # 30 seconds
    )
    return pool


def test():
    db = connect_tcp_socket()
    with db.connect() as db_conn:
        results = db_conn.execute("SELECT NOW()").fetchone()
        return results[0]