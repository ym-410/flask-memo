from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path

instance_dir = Path(__file__).resolve().parent / "instance"
instance_dir.mkdir(exist_ok=True)

# 初期化 1
app: Flask = Flask(__name__, instance_path=str(instance_dir))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///memo_edit.sqlite"
db:SQLAlchemy = SQLAlchemy(app)

# スキーマ定義 2
class MemoItem(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    title: str = db.Column(db.Text, nullable=False)
    body: str = db.Column(db.Text, nullable=False)

# DB初期化 
with app.app_context():
    db.create_all()

# メモ一覧表示
@app.route("/")
def index():
    items = MemoItem.query.order_by(MemoItem.title).all()
    return render_template("list.html", items=items)

@app.route("/memo/new", methods=["GET", "POST"])
def new_memo():
    it = MemoItem(title="無題", body="")

    if request.method == "POST":
        it.title = request.form.get("title", "")
        it.body = request.form.get("body", "")

        if not it.title.strip():
            return render_template(
                "memo.html",
                it=it,
                error="タイトルは空にできません"
            ), 400

        db.session.add(it)
        db.session.commit()
        return redirect(url_for("index"))
    
    return render_template("memo.html", it=it)

@app.route("/memo/<int:id>", methods=["GET", "POST"])
def memo(id: int):
    # DBからメモ取得 5
    it = db.session.get(MemoItem, id)

    if it is None:
        return "メモが見つかりません", 404

    if request.method == "POST":
        it.title = request.form.get("title", "")
        it.body = request.form.get("body", "")

        if not it.title.strip():
            return render_template(
                "memo.html",
                it=it,
                error="タイトルは空にできません",
            ), 400

        db.session.commit()
        return redirect(url_for("index"))

    # メモの編集画面を表示 8
    return render_template(
        "memo.html",
        it=it
    )

@app.post("/memo/<int:id>/delete")
def delete_memo(id):
    it = db.get_or_404(MemoItem, id)

    db.session.delete(it)
    db.session.commit()

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port=8888)
