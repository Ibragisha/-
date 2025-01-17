from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Artist(Base):
    __tablename__ = 'Artist'
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

    
    albums = relationship('Album', back_populates='artist')


class Album(Base):
    __tablename__ = 'Album'
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey('Artist.ArtistId'))

    
    artist = relationship('Artist', back_populates='albums')
    
    tracks = relationship('Track', back_populates='album')


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

    
album = relationship('Album', back_populates = 'tracks')
media_type = relationship('MediaType', back_populates = 'tracks')
genre = relationship('Genre', back_populates = 'tracks')

class MediaType(Base):
    __tablename__ = 'MediaType'
    MediaTypeId = Column(Integer, primary_key=True)



