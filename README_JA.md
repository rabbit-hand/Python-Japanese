# Python 日本語版 - 非公式改造版

## ⚠️ 重要な免責事項

**これは非公式のPython日本語化改造プロジェクトです。**

- 本プロジェクトはPython Software Foundation（PSF）によって公式にサポート、承認、または認可されていません。
- 本プロジェクトはCPythonソースコードをベースにしていますが、日本語キーワードを使用するための変更が加えられています。
- 本ソフトウェアの使用により生じたいかなる損害、データの損失、またはその他の問題についても、開発者は一切の責任を負いません。
- 本ソフトウェアは「現状のまま」提供され、いかなる保証も含まれていません。
- 本プロジェクトは教育目的および実験的な使用のみを意図しています。
- 本ソフトウェアを本番環境で使用することは推奨されません。
- 本プロジェクトを使用することで、上記の条件に同意したものとみなされます。

---

## 概要

このプロジェクトは、日本語キーワードを使用してPythonプログラミングができるようにするための非公式の改造版です。

表面的には日本語でコードを記述できますが、内部的には標準のPythonコードに変換されて実行されます。これにより、英語に不慣れな日本の開発者でもより安心してPythonを使用できるようになります。

## 特徴

- **日本語キーワード**: `もし`、`繰り返し`、`関数` などの日本語キーワードが使用可能
- **自動変換**: 日本語コードを標準Pythonコードに自動変換
- **完全互換**: 変換後のコードは標準Pythonと完全互換
- **Pythonモジュール**: `japanese_keyword` モジュールをインポートして使用可能

## インストール方法

### 前提条件

- Python 3.6以上がインストールされていること
- CPythonソースコードがビルドされていること

### インストール手順

1. このリポジトリをクローンまたはダウンロードします
2. `Lib/japanese_keyword.py` モジュールがPythonのライブラリパスに含まれていることを確認します
3. `Tools/japanese_preprocessor.py` スクリプトを使用して日本語コードを変換します

## 使用方法

### 方法1: Pythonモジュールを使用する

`japanese_keyword` モジュールをインポートして使用します：

```python
import japanese_keyword

# 日本語キーワードを含むコードを実行
japanese_keyword.exec_japanese('''
もし x > 0:
    表示("正の数です")
あるいは x < 0:
    表示("負の数です")
それ以外:
    表示("ゼロです")
''', {'x': 5})
```

**実践的な使用例:**

```python
import japanese_keyword

# 電卓プログラムの例
japanese_keyword.exec_japanese('''
関数 足し算(a, b):
    戻る a + b

関数 引き算(a, b):
    戻る a - b

関数 掛け算(a, b):
    戻る a * b

関数 割り算(a, b):
    もし b == 0:
        戻る "ゼロで割ることはできません"
    戻る a / b

# 関数を使用
表示("計算結果:")
表示(f"5 + 3 = {足し算(5, 3)}")
表示(f"10 - 4 = {引き算(10, 4)}")
表示(f"6 * 7 = {掛け算(6, 7)}")
表示(f"15 / 3 = {割り算(15, 3)}")
''')
```

### 方法2: プリプロセッサスクリプトを使用する

日本語で書かれたPythonファイルを変換して実行します：

```bash
python Tools/japanese_preprocessor.py my_script.py
```

これにより、`my_script_converted.py` という変換済みファイルが生成されます。

出力ファイル名を指定する場合：

```bash
python Tools/japanese_preprocessor.py my_script.py output.py
```

変換後のファイルを実行：

```bash
python output.py
```

**実践的な使用例:**

まず、`my_script.py` というファイルを作成します：

```python
# my_script.py - 日本語で書かれたPythonプログラム

読み込み random

関数 おみくじ():
    運勢 = random.choice(["大吉", "中吉", "小吉", "凶"])
    表示(f"今日の運勢は: {運勢}")
    もし 運勢 == "大吉":
        表示("素晴らしい一日になります！")
    あるいは 運勢 == "凶":
        表示("気を落とさず頑張りましょう！")
    それ以外:
        表示("良い一日になります！")

# プログラムを実行
表示("おみくじプログラム")
表示("-" * 20)
おみくじ()
```

次に、このファイルを変換して実行します：

```bash
# 変換
python Tools/japanese_preprocessor.py my_script.py

# 実行
python my_script_converted.py
```

### 方法3: 直接実行する

プリプロセッサを使用して直接実行することもできます：

```bash
python Tools/japanese_preprocessor.py --exec my_script.py
```

**実践的な使用例:**

`my_script.py` を直接実行：

```bash
python Tools/japanese_preprocessor.py --exec my_script.py
```

### 日本語キーワードの例

#### 基本的な制御構造

```python
# 日本語で書かれたコード
もし x > 0:
    表示("正の数です")
あるいは x < 0:
    表示("負の数です")
それ以外:
    表示("ゼロです")
```

変換後：

```python
# 標準Pythonコード
if x > 0:
    print("正の数です")
elif x < 0:
    print("負の数です")
else:
    print("ゼロです")
```

#### 関数定義

```python
# 日本語で書かれたコード
関数 足し算(a, b):
    戻る a + b

結果 = 足し算(5, 3)
print(結果)
```

変換後：

```python
# 標準Pythonコード
def 足し算(a, b):
    return a + b

結果 = 足し算(5, 3)
print(結果)
```

#### 繰り返し処理

```python
# 日本語で書かれたコード
繰り返し i 中に range(10):
    print(i)
```

変換後：

```python
# 標準Pythonコード
for i in range(10):
    print(i)
```

#### クラス定義

```python
# 日本語で書かれたコード
クラス 人:
    関数 __init__(自己, 名前):
        自己.名前 = 名前
    
    関数 紹介(自己):
        print(f"私は{自己.名前}です")

田中 = 人("田中")
田中.紹介()
```

変換後：

```python
# 標準Pythonコード
class 人:
    def __init__(自己, 名前):
        自己.名前 = 名前
    
    def 紹介(自己):
        print(f"私は{自己.名前}です")

田中 = 人("田中")
田中.紹介()
```

#### import文

```python
# 日本語で書かれたコード
読み込み random
読み込み math として m
読み込み datetime から datetime

# randomモジュールを使用
乱数 = random.randint(1, 100)
print(乱数)

# mathモジュールを使用（asで別名）
円周率 = m.pi
print(円周率)

# datetimeモジュールを使用（fromでインポート）
現在時刻 = datetime.now()
print(現在時刻)
```

変換後：

```python
# 標準Pythonコード
import random
import math as m
from datetime import datetime

# randomモジュールを使用
乱数 = random.randint(1, 100)
print(乱数)

# mathモジュールを使用（asで別名）
円周率 = m.pi
print(円周率)

# datetimeモジュールを使用（fromでインポート）
現在時刻 = datetime.now()
print(現在時刻)
```

### サポートされている日本語キーワード

#### 制御構造

- `もし` → `if`
- `それ以外` → `else`
- `あるいは` → `elif`
- `繰り返し` → `for`
- `その間` → `while`
- `抜ける` → `break`
- `続ける` → `continue`

#### 関数・クラス

- `関数` → `def`
- `クラス` → `class`
- `戻る` → `return`
- `生成する` → `yield`
- `無名関数` → `lambda`

#### モジュール

- `読み込み` → `import`
- `から` → `from`
- `として` → `as`

#### 例外処理

- `試す` → `try`
- `例外` → `except`
- `最後に` → `finally`
- `発生させる` → `raise`

#### 論理演算子

- `かつ` → `and`
- `または` → `or`
- `ではない` → `not`
- `中に` → `in`
- `である` → `is`

#### その他

- `何もしない` → `pass`
- `表明する` → `assert`
- `グローバル` → `global`
- `非ローカル` → `nonlocal`
- `削除` → `del`
- `共有して` → `with`
- `非同期` → `async`
- `待機する` → `await`

#### 定数

- `偽` → `False`
- `真` → `True`
- `無` → `None`

#### ソフトキーワード

- `一致` → `match`
- `場合` → `case`
- `型` → `type`
- `遅延` → `lazy`

### サポートされている日本語組み込み関数

#### 入出力関数

- `表示` → `print`
- `入力` → `input`

#### 型変換関数

- `整数` → `int`
- `浮動小数` → `float`
- `文字列` → `str`
- `論理値` → `bool`
- `リスト` → `list`
- `辞書` → `dict`
- `集合` → `set`
- `タプル` → `tuple`
- `バイト列` → `bytes`

#### シーケンス操作関数

- `長さ` → `len`
- `範囲` → `range`
- `列挙` → `enumerate`
- `圧縮` → `zip`
- `反転` → `reversed`
- `ソート済み` → `sorted`

#### 数学関数

- `絶対値` → `abs`
- `最小` → `min`
- `最大` → `max`
- `合計` → `sum`
- `累乗` → `pow`
- `四捨五入` → `round`

#### 関数型プログラミング関数

- `写像` → `map`
- `フィルター` → `filter`
- `任意` → `any`
- `全て` → `all`

#### オブジェクト操作関数

- `種類` → `type`
- `ID` → `id`
- `ハッシュ` → `hash`
- `属性取得` → `getattr`
- `属性設定` → `setattr`
- `属性削除` → `delattr`
- `属性有無` → `hasattr`

#### ファイル操作関数

- `開く` → `open`

#### その他の関数

- `助言` → `help`
- `実行` → `exec`
- `評価` → `eval`
- `コンパイル` → `compile`

## カスタマイズ

`Lib/japanese_keyword.py` ファイルの `JAPANESE_KEYWORD_MAP` 辞書と `JAPANESE_BUILTIN_MAP` 辞書を編集することで、独自のキーワードマッピングと組み込み関数マッピングを追加できます。

```python
JAPANESE_KEYWORD_MAP = {
    # 既存のマッピング...
    'あなたのキーワード': 'english_keyword',
}

JAPANESE_BUILTIN_MAP = {
    # 既存のマッピング...
    'あなたの関数': 'builtin_function',
}
```

## 制限事項

- 文字列リテラル内の日本語キーワードは置換されません
- コメント内の日本語キーワードは置換されません
- すべてのPythonキーワードが日本語化されているわけではありません
- 標準ライブラリの関数名は日本語化されていません
- 変数名や関数名は日本語のまま使用できますが、キーワードとの競合に注意してください

## トラブルシューティング

### 変換が正しく行われない場合

1. `Lib/japanese_keyword.py` モジュールが正しくインポートできることを確認してください
2. 入力ファイルのエンコーディングがUTF-8であることを確認してください
3. キーワードのスペルが正しいことを確認してください

### 実行時エラーが発生する場合

1. 変換後のコードを確認してください
2. 標準Pythonの構文に従っているか確認してください
3. Pythonのバージョンが要件を満たしているか確認してください

## 貢献

このプロジェクトは非公式の改造版であり、公式のPythonプロジェクトとは関係ありません。

## ライセンス

このプロジェクトは、元のCPythonと同じPSF License Agreementに従います。詳細は `LICENSE` ファイルを参照してください。

## リンク

- 公式Pythonウェブサイト: https://www.python.org
- 公式Pythonソースコード: https://github.com/python/cpython
- 公式Pythonドキュメント: https://docs.python.org

---

**再度の注意**: これは非公式のプロジェクトです。公式のPythonではないことを理解した上で使用してください。
