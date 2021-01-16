# kcua-virtual
https://kcua-virtual.netlify.app/

## Usage

```bash
# flaskサーバーを立ち上げる
$ python run.py

# 静的サイト化
$ python freeze.py

# sassファイルを監視
$ sass --watch static/scss/main.scss:static/css/main.css
```

## 構成
- build: frozen-flaskで静的化した時の生成場所
- static: 
  - css: cssファイル置き場 (scssで生成するので直接編集しない)
  - images: 画像置き場
  - js: javascriptファイル置き場
  - scss: scssファイル置き場
- templates: 動的なHTMLファイル置き場
  - partials: HTMLの部品系 (例:ナビゲーションバー)
  - sections: トップページのセクションのためのHTMLファイル
  - base.html: 全てのページのベースとなるHTMLファイル
  - index.html: トップページのHTMLファイル
- .gitignore: gitで追跡しないファイルを記述
- README.md: (このファイル)
- freeze.py: 静的化するためのpythonファイル
- run.py: flaskサーバーを立ち上げるためのpythonファイル (最終的には静的化するのでテスト時に立ち上げる)
