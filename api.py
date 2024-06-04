from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "movie_lens"

app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


@app.route("/")
def hello_world():
    return "<p>Welcome, Kendrick!</p>"


def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return data


@app.route("/movies", methods=["GET"])
def get_movies():
    data = data_fetch("""select * from movies""")
    return make_response(jsonify(data), 200)


@app.route("/movies/<int:id>", methods=["GET"])
def get_movie_by_id(id):
    data = data_fetch("""SELECT * FROM movies where movieId = {}""".format(id))
    return make_response(jsonify(data), 200)


@app.route("/movies/<int:id>/UserHist", methods=["GET"])
def get_UserHist_by_movie(id):
    data = data_fetch(
        """
        SELECT movies.title, movies.genres, movies.movieId, ratings.Idrating, tags.Id 
        FROM movies
        INNER JOIN ratings
        ON movies.movieId = ratings.Idrating 
        INNER JOIN tags
        ON ratings.Idrating = tags.Id 
        WHERE movies.movieId = {}
    """.format(
            id
        )
    )
    return make_response(
        jsonify({"movieId": id, "count": len(data), "title": data}), 200
    )
    
    @app.route("/movies", methods=["POST"])
def add_movie():
    cur = mysql.connection.cursor()
    info = request.get_json()
    title = info["title"]
    genre = info["genres"]
    cur.execute(
        """ INSERT IGNORE INTO movies (title, genres) VALUE (%s, %s)""",
        (title, genre),
    )
    mysql.connection.commit()
    print("row(s) affected :{}".format(cur.rowcount))
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "the movie was added successfully", "rows_affected": rows_affected}
        ),
        201,
    )


@app.route("/movies/<int:id>", methods=["PUT"])
def update_movie(id):
    cur = mysql.connection.cursor()
    info = request.get_json()
    title = info["title"]
    genre = info["genres"]
    cur.execute(
        """ UPDATE movies SET title = %s, genres = %s WHERE movieId = %s """,
        (title, genre, id),
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "The movie was updated successfully", "rows_affected": rows_affected}
        ),
        200,
    )@app.route("/movies", methods=["POST"])
def add_movie():
    cur = mysql.connection.cursor()
    info = request.get_json()
    title = info["title"]
    genre = info["genres"]
    cur.execute(
        """ INSERT IGNORE INTO movies (title, genres) VALUE (%s, %s)""",
        (title, genre),
    )
    mysql.connection.commit()
    print("row(s) affected :{}".format(cur.rowcount))
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "the movie was added successfully", "rows_affected": rows_affected}
        ),
        201,
    )
    


@app.route("/movies/<int:id>", methods=["PUT"])
def update_movie(id):
    cur = mysql.connection.cursor()
    info = request.get_json()
    title = info["title"]
    genre = info["genres"]
    cur.execute(
        """ UPDATE movies SET title = %s, genres = %s WHERE movieId = %s """,
        (title, genre, id),
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "The movie was updated successfully", "rows_affected": rows_affected}
        ),
        200,
    )