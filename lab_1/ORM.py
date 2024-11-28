from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Базовый класс для всех моделей
Base = declarative_base()

# Таблица Artist
class Artist(Base):
    __tablename__ = 'Artist'
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

    # Связь один ко многим с таблицей Album
    albums = relationship('Album', back_populates='artist')

# Таблица Album
class Album(Base):
    __tablename__ = 'Album'
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey('Artist.ArtistId'))

    # Связь с таблицей Artist
    artist = relationship('Artist', back_populates='albums')
    # Связь один ко многим с таблицей Track
    tracks = relationship('Track', back_populates='album')

# Таблица Track
class Track(Base):
    __tablename__ = 'Track'
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey('Album.AlbumId'))
    MediaTypeId = Column(Integer, ForeignKey('MediaType.MediaTypeId'))
    GenreId = Column(Integer, ForeignKey('Genre.GenreId'))
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Float)

    # Связи
    album = relationship('Album', back_populates='tracks')
    media_type = relationship('MediaType', back_populates='tracks')
    genre = relationship('Genre', back_populates='tracks')

# Таблица MediaType
class MediaType(Base):
    __tablename__ = 'MediaType'
    MediaTypeId = Column(Integer, primary_key=True)
    Name = Column(String)

    # Связь один ко многим с таблицей Track
    tracks = relationship('Track', back_populates='media_type')

# Таблица Genre
class Genre(Base):
    __tablename__ = 'Genre'
    GenreId = Column(Integer, primary_key=True)
    Name = Column(String)

    # Связь один ко многим с таблицей Track
    tracks = relationship('Track', back_populates='genre')

# Таблица Customer
class Customer(Base):
    __tablename__ = 'Customer'
    CustomerId = Column(Integer, primary_key=True)
    FirstName = Column(String)
    LastName = Column(String)
    Company = Column(String)
    Address = Column(String)
    City = Column(String)
    State = Column(String)
    Country = Column(String)
    PostalCode = Column(String)
    Phone = Column(String)
    Fax = Column(String)
    Email = Column(String)
    SupportRepId = Column(Integer, ForeignKey('Employee.EmployeeId'))

    # Связь с таблицей Employee
    support_rep = relationship('Employee', back_populates='customers')

# Таблица Employee
class Employee(Base):
    __tablename__ = 'Employee'
    EmployeeId = Column(Integer, primary_key=True)
    LastName = Column(String)
    FirstName = Column(String)
    Title = Column(String)
    ReportsTo = Column(Integer, ForeignKey('Employee.EmployeeId'))
    BirthDate = Column(DateTime)
    HireDate = Column(DateTime)
    Address = Column(String)
    City = Column(String)
    State = Column(String)
    Country = Column(String)
    PostalCode = Column(String)
    Phone = Column(String)
    Fax = Column(String)
    Email = Column(String)

    # Связь один ко многим с Customer
    customers = relationship('Customer', back_populates='support_rep')
    # Связь один ко многим с самим собой (менеджеры)
    subordinates = relationship('Employee', backref='manager', remote_side=[EmployeeId])

# Таблица Invoice
class Invoice(Base):
    __tablename__ = 'Invoice'
    InvoiceId = Column(Integer, primary_key=True)
    CustomerId = Column(Integer, ForeignKey('Customer.CustomerId'))
    InvoiceDate = Column(DateTime)
    BillingAddress = Column(String)
    BillingCity = Column(String)
    BillingState = Column(String)
    BillingCountry = Column(String)
    BillingPostalCode = Column(String)
    Total = Column(Float)

    # Связь с таблицей Customer
    customer = relationship('Customer', back_populates='invoices')

# Добавление связей, пропущенных ранее
Customer.invoices = relationship('Invoice', back_populates='customer')

# Настройка подключения к базе данных
def setup_database(database_path="sqlite:///World_Music.sqlite"):
    engine = create_engine(database_path)
    Base.metadata.create_all(engine)
    return engine

# Создание сессии
def create_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()


engine = setup_database("sqlite:///World_Music.sqlite"), session = create_session(engine)
# Добавить нового артиста
new_artist = Artist(Name="New Artist")
session.add(new_artist)
session.commit()
print(f"Added artist with ID: {new_artist.ArtistId}")
# Получить все альбомы артиста 
artist = session.query(Artist).filter_by(Name="New Artist").first()
if artist:
    print(f"Albums by {artist.Name}: {[album.Title for album in artist.albums]}")
# Удалить трек
track = session.query(Track).filter_by(Name="Some Track").first()
if track:
    session.delete(track)
    session.commit()
    print("Track deleted.")