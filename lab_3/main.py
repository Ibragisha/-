from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///World_Music.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50))

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.Date)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    artist = db.relationship('Artist', backref='albums')

with app.app_context():
    db.create_all()

# Маршрут: Получить всех исполнителей
@app.route("/artists", methods=["GET"])
def get_artists():
    artists = Artist.query.all()
    return jsonify([{"id": a.id, "name": a.name, "genre": a.genre} for a in artists])

# Маршрут: Создать нового исполнителя
@app.route("/artists", methods=["POST"])
def create_artist():
    data = request.get_json()
    artist = Artist(
        name=data["name"],
        genre=data.get("genre")
    )
    db.session.add(artist)
    db.session.commit()
    return jsonify({"id": artist.id, "name": artist.name}), 201

# Маршрут: Получить все альбомы
@app.route("/albums", methods=["GET"])
def get_albums():
    albums = Album.query.all()
    return jsonify([
        {
            "id": a.id,
            "title": a.title,
            "release_date": a.release_date.strftime("%Y-%m-%d") if a.release_date else None,
            "artist": a.artist.name if a.artist else "Неизвестен"
        } for a in albums
    ])

# Маршрут: Создать новый альбом
@app.route("/albums", methods=["POST"])
def create_album():
    data = request.get_json()
    release_date = datetime.strptime(data["release_date"], "%Y-%m-%d").date() if "release_date" in data else None

    album = Album(
        title=data["title"],
        release_date=release_date,
        artist_id=data.get("artist_id")
    )
    db.session.add(album)
    db.session.commit()
    return jsonify({"id": album.id, "title": album.title}), 201

# Маршрут: Обновить альбом по ID
@app.route("/albums/<int:album_id>", methods=["PUT"])
def update_album(album_id):
    data = request.get_json()
    album = Album.query.get(album_id)
    if not album:
        return jsonify({"error": "Album not found"}), 404

    if "title" in data:
        album.title = data["title"]
    if "release_date" in data:
        try:
            album.release_date = datetime.strptime(data["release_date"], "%Y-%m-%d").date()
        except ValueError:
            return jsonify({"error": "Invalid date format, should be YYYY-MM-DD"}), 400

    db.session.commit()
    return jsonify({"id": album.id, "title": album.title})

# Маршрут: Удалить альбом по ID
@app.route("/albums/<int:album_id>", methods=["DELETE"])
def delete_album(album_id):
    album = Album.query.get(album_id)
    if not album:
        return jsonify({"error": "Album not found"}), 404
    db.session.delete(album)
    db.session.commit()
    return jsonify({"message": "Album deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)