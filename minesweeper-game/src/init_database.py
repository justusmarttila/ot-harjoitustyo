from connect_database import get_database_connection

def drop_tables(connection):
    db = connection.cursor()

    db.execute("""
        drop table if exists users;
    """)
    connection.commit()

def create_tables(connection):
    db = connection.cursor()

    db.execute("""
        create table users (
            username text primary key,
            password text
        );
    """)

    connection.commit()

def init_database():

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    init_database()
