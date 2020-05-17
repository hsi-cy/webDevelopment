import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engin = create_engine(os.getenv("DATABASE_URL"))
"""the engin is an object created by SQL alchemy to manage the connection of the data. This object can talk to database and making sure python is able to send commands to the database. database can be local (in the computer) or online. """

db = scoped_session(sessionmaker(bind=engine))
"""To ensure when A is using the database B cannot interupt the work. db is the object that allows us to run sql commands."""

def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    """.fetchall() function can get all the result from your query."""
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes ")

def __name__ == "__main__":
    main()