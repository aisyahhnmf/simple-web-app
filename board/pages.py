from flask import Blueprint, render_template, request, redirect, url_for
from board.database import get_pg_db_conn

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    return render_template("pages/about.html")

# 🆕 Tambah post
@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        author = request.form["author"]
        message = request.form["message"]

        conn = get_pg_db_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO post (author, message) VALUES (%s, %s)",
            (author, message)
        )
        conn.commit()
        cur.close()
        conn.close()

        return redirect(url_for("pages.posts"))

    return render_template("pages/create.html")

# 🆕 List posts
@bp.route("/posts")
def posts():
    conn = get_pg_db_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, created, author, message FROM post ORDER BY id DESC")
    posts = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("ppsts/posts.html", posts=posts)

