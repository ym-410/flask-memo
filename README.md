# Memo App

FlaskとSQLiteを用いたシンプルなメモアプリ。
メモの一覧表示・新規作成・編集ができます。

## 必要なもの

- Python 3.10 以上
- `requirements.txt` に記載したパッケージ

## 起動方法

リポジトリのルートから `memo` ディレクトリに移動し、仮想環境を作成して依存パッケージをインストールします。

```bash
cd memo
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

ブラウザで <http://127.0.0.1:8888/> を開いてください。停止するには、起動したターミナルで `Ctrl+C` を押します。

## 使い方

- ヘッダー右側の「新規作成」からメモを追加できます。
- 一覧に表示されたタイトルを押すと、メモを編集できます。
- 保存後は一覧画面に戻ります。

## データの保存先

メモは `instance/memo_edit.sqlite` に保存されます。初回起動時にディレクトリとテーブルが自動作成されます。

## データベース構造

データベースの構造は [schema.dbml](schema.dbml)を参照してください。

## デザイン
画面の装飾には、外部 CDN から読み込む Bulma を使用しています。ネットワークに接続できない場合、装飾は適用されません。
