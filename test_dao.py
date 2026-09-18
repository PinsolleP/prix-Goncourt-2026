from datetime import date
from decimal import Decimal

from goncourt.daos.person_dao import PersonDao
from goncourt.daos.publisher_dao import PublisherDao
from goncourt.daos.author_dao import AuthorDao
from goncourt.daos.character_dao import CharacterDao
from goncourt.daos.book_dao import BookDao
from goncourt.daos.selection_dao import SelectionDao
from goncourt.daos.jury_dao import JuryDao
from goncourt.daos.user_dao import UserDao
from goncourt.daos.vote_dao import VoteDao

from goncourt.models.person import Person
from goncourt.models.publisher import Publisher
from goncourt.models.author import Author
from goncourt.models.character_ import Character_
from goncourt.models.book import Book
from goncourt.models.selection import Selection
from goncourt.models.jury import Jury
from goncourt.models.user_ import User_
from goncourt.models.vote import Vote


# TEST Person
def test_person_dao():
    dao = PersonDao()

    person = Person(
        id_person=50,
        first_name="Paul",
        last_name="Test",
    )
    # CREATE
    result = dao.create(person)
    print("CREATE :", result)

    # READ
    person_read = dao.read(50)
    print("READ :", person_read)

    # UPDATE
    person.first_name = "Paul Updated"
    result = dao.update(person)
    print("UPDATE :", result)

    # READ après UPDATE
    person_read = dao.read(50)
    print("READ aprés UPDATE :", person_read)

    # DELETE
    result = dao.delete(person)
    print("DELETE :", result)

"""
# TEST PUBLISHER
def test_publisher_dao():
    dao = PublisherDao()

    publisher = Publisher(
        id_person=50,
        name="Editeur Test"
    )
    # CREATE
    result = dao.create(publisher)
    print("CREATE :", result)

    # READ
    person_read = dao.read(50)
    print("READ :", person_read)

    # UPDATE
    person.first_name = "Paul Updated"
    result = dao.update(person)
    print("UPDATE :", result)

    # READ après UPDATE
    person_read = dao.read(50)
    print("READ aprés UPDATE :", person_read)

    # DELETE
    result = dao.delete(person)
    print("DELETE :", result)"""

if __name__ == "__main__":
    test_person_dao()
