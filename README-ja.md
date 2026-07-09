---

# # 🐣 日本語Python（Python-Japanese）初心者向けインストール＆使い方ガイド  
※ GitHub の内容を初心者向けに再構成したものです（）

---

# ## 🎯 結論：この日本語Pythonは「ビルド不要」で使える  
GitHubには CPython の大量のソースが入っているけれど、  
**日本語でPythonを書くために必要なのはたった2つのファイルだけ**。

- `japanese_keyword.py`  
- `japanese_preprocessor.py`  

この2つが「日本語 → 普通のPython」に変換してくれる。

---

# ## 📥 1. 必要なファイルをダウンロードする

### GitHubページ  
`https://github.com/rabbit-hand/Python-Japanese（）` [(github.com in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fgithub.com%2Frabbit-hand%2FPython-Japanese%25EF%25BC%2588%25EF%25BC%2589")

### ダウンロードするファイル  
- `Lib/japanese_keyword.py`  
- `Tools/japanese_preprocessor.py`

👉 **同じフォルダに置くだけでOK**  
Python本体のビルドは不要。

---

# ## 📝 2. 日本語でプログラムを書く

例：`hello.py` を作る

```python
もし 1 < 2:
    表示("こんにちは")
```

---

# ## ▶️ 3. 日本語のまま実行する

ターミナル（コマンドプロンプト）で次を実行：

```bash
python japanese_preprocessor.py hello.py
```

すると内部で日本語が英語のPythonに変換され、普通のPythonとして実行される。

---

# ## 🔧 仕組み（初心者向けに超ざっくり）

- 「もし → if」「表示 → print」などの変換ルールが  
  **`japanese_keyword.py` に入っている**
- `japanese_preprocessor.py` が日本語コードを読み取り  
  **英語のPythonコードに書き換える**
- 最後に普通のPythonとして実行される

だから **Python本体を改造したりビルドする必要はない**。

---

# ## 📚 4. よく使う日本語キーワード一覧（初心者向け）

| 日本語 | Python |
|-------|--------|
| もし | if |
| あるいは | elif |
| それ以外 | else |
| 繰り返し | for |
| 関数 | def |
| 戻る | return |
| 表示 | print |
| 読み込み | import |

（GitHubの一覧を初心者向けに簡略化したものです ）

---

# ## 🧪 5. もう少し実用的な例

`calc.py`

```python
関数 足し算(a, b):
    戻る a + b

表示( 足し算(5, 3) )
```

実行：

```bash
python japanese_preprocessor.py calc.py
```

---

# ## 🚫 注意点（初心者向け）

- 日本語キーワードは **コードの外（文字列やコメント）では変換されない**
- Python本体をビルドする必要はない  
- 標準ライブラリの関数名は日本語化されていない  
- 変換後のコードは普通のPythonとして動く

（GitHubの注意事項を初心者向けに要約したものです ）

---

# ## 🎉 これで日本語Pythonは使えるようになるはずです

初心者がつまずきやすいポイントを全部取り除いてあるから、  
この手順どおりに進めれば **確実に日本語Pythonを動かせる**よ。

---
