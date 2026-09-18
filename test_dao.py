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


# TEST PUBLISHER
def test_publisher_dao():
    print()
    dao = PublisherDao()

    publisher = Publisher(
        id_publisher=50,
        name="Editeur Test"
    )
    # CREATE
    result = dao.create(publisher)
    print("CREATE Publisher :", result)

    # READ
    publisher_read = dao.read(50)
    print("READ Publisher :", publisher_read)

    # UPDATE
    publisher.name = "Editeur Test Updated"
    result = dao.update(publisher)
    print("UPDATE Publisher :", result)

    # READ après UPDATE
    publisher_read = dao.read(50)
    print("READ aprés UPDATE Publisher :", publisher_read)

    # DELETE
    result = dao.delete(publisher)
    print("DELETE Publisher :", result)

# TEST AUTHOR
def test_author_dao():
    print()
    person_dao = PersonDao()
    author_dao = AuthorDao()

    person = Person(
        id_person=51,
        first_name="Auteur",
        last_name="Test"
    )

    author = Author(
        id_person=51,
        first_name="Auteur",
        last_name="Test",
        id_author=50,
        biographie="Biographie de test"
    )

    # CREATE Person
    result = person_dao.create(person)
    print("CREATE Person pour Author :", result)

    # CREATE Author
    result = author_dao.create(author)
    print("CREATE Author :", result)

    # READ Author
    author_read = author_dao.read(50)
    print("READ Author :", author_read)

    # UPDATE Author
    author.biographie = "Biographie de test modifiée"
    result = author_dao.update(author)
    print("UPDATE Author :", result)

    # READ après UPDATE
    author_read = author_dao.read(50)
    print("READ aprés UPDATE Author :", author_read)

    # DELETE Author
    result = author_dao.delete(author)
    print("DELETE Author :", result)

    # DELETE Person
    result = person_dao.delete(person)
    print("DELETE Person :", result)

# TEST Selection
def test_selection_dao():
    print()
    dao = SelectionDao()

    selection = Selection(
        id_selection=50,
        date_selection=date(2026, 9, 20),
        round=1
    )

    # CREATE
    result = dao.create(selection)
    print("CREATE Selection :", result)

    # READ
    selection_read = dao.read(50)
    print("READ Selection :", selection_read)

    # UPDATE
    selection.date_selection = date(2026, 9, 25)
    selection.round = 2
    result = dao.update(selection)
    print("UPDATE Selection :", result)

    # READ après UPDATE
    selection_read = dao.read(50)
    print("READ aprés UPDATE Selection :", selection_read)

    # DELETE
    result = dao.delete(selection)
    print("DELETE Selection :", result)

# TEST Character
def test_character_dao():
    print()
    person_dao = PersonDao()
    author_dao = AuthorDao()
    publisher_dao = PublisherDao()
    book_dao = BookDao()
    character_dao = CharacterDao()

    person = Person(
        id_person=52,
        first_name="Auteur",
        last_name="Character Test",
    )
    person_dao.create(person)

    author = Author(
        id_person=52,
        first_name="Auteur",
        last_name="Character Test",
        id_author=51,
        biographie="Biographie Character Test"
    )
    author_dao.create(author)

    publisher = Publisher(
        id_publisher=51,
        name="Publisher Character Test",
    )
    publisher_dao.create(publisher)

    book = Book(
        isbn=9780000000051,
        title="Book Character Test",
        summary="Livre de test pour CharacterDao",
        publication_date=date(2026, 9, 18),
        number_pages=100,
        publisher_price=Decimal("15.00"),
        publisher=publisher,
        author=author
    )
    book_dao.create(book)

    character = Character_(
        id_character=50,
        name="Personnage Test",
        isbn=9780000000051
    )

    # CREATE
    result = character_dao.create(character)
    print("CREATE Character :", result)

    # READ
    character_read = character_dao.read(50)
    print("READ Character :", character_read)

    #UPDATE
    character.name = "Personnage Test Updated"
    result = character_dao.update(character)
    print("UPDATE Character :", result)

    character_read = character_dao.read(50)
    print("READ après UPDATE Character :", character_read)

    # DELETE
    result = character_dao.delete(character)
    print("DELETE Character :", result)

    book_dao.delete(book)
    author_dao.delete(author)
    person_dao.delete(person)
    publisher_dao.delete(publisher)


if __name__ == "__main__":
    test_person_dao()
    test_publisher_dao()
    test_author_dao()
    test_selection_dao()
    test_character_dao()
