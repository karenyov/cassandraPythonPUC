from cassandra.cluster import Cluster
cluster = Cluster(['172.17.0.2'], port=9042)
session = cluster.connect('aula')

session.execute ("""
INSERT INTO users (id, lastname, age, city, email, firstname)
VALUES (uuid(), 'Jones', '35', 'Austin', 'bob@example.com', 'Bob');

""")

result = session.execute("""
SELECT * FROM users WHERE lastname = 'Jones' ALLOW FILTERING;
""")[0]

print(result.age, result.lastname)