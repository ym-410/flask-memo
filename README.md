# Memo App

FlaskとSQLiteでメモを作成・編集・削除するアプリです。Python 3.10以上が必要です。

## 起動方法

```bash
cd memo
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

ブラウザで <http://127.0.0.1:8888/> を開きます。

## 使い方

- 一覧画面から新規作成、タイトルを選ぶと詳細情報表示・編集ができます。
- 編集画面で保存・削除できます。削除時は確認が表示されます。

メモは `instance/memo_edit.sqlite` に保存されます。テーブル定義は [schema.dbml](schema.dbml)、CSSは `static/css/style.css` にあります。
