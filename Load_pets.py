import sqlite3 

conn = sqlite3.connect('pets.db')
cursor = conn.cursor() 

persons = [
    (1, 'James', 'Smirth, 41'),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'Willaim', 'Gibson', 23)
];

cursor.executemany("INSERRT INTO person VALUES (?, ?, ?, ?)", persons)

pets = [
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'AlaskinMalamute', 3, 0),
    (3, 'Max', 'CockerSpaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'CockerSpaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
];

cursor.executemany("INSERT INTO pet VALUES (?, ?, ?, ?)", pets)

person_pets = [
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4,6)
];

conn.commit()
conn.close()
