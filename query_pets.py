import sqlite3 

def main():
    conn = sqlite3.connect('pets.db') 
    cursor = conn.cursor 
    while True: 
        if person_id == '-1':
            break 
    cursor.execute("SELECT*FROM person WHERE id =?", (person_id))
    person = cursor.fetchone()

    if person:
        print (f"{person[1]}, {person[2]}, {person[3]} years old")
        cursor.execute("SELECT p.name, p.breed, p.age FROM pet p"
                       "JOIN person_pet pp ON p.id = pp.pet_id"
                       "WHERE pp.person_id =?", (person_id))
        pets = cursor.fetchall()

        if pets: 
            for pet in pets:
                print(f"{person[1]} {person[2]} owned {pet[0]}, a {pet[1]}, that was {pet[2]} years old")
        else:
                print(f"{person[1]} {person[2]} has no pets")

    else: 
        print(f"Error: Person not found")

    conn.close() 

if __name__ == "__main__":
    "main"

