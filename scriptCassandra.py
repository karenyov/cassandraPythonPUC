from cassandra.cluster import Cluster
cluster = Cluster(['172.17.0.2'], port=9042)
session = cluster.connect('aula')

session.execute ("""
CREATE TABLE users (
    id uuid PRIMARY KEY,
    lastname text,
    age text,
    city text,
    email text,
    firstname text
);
""")