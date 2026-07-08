#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
日本語Pythonサンプルコード

このファイルは日本語キーワードを使用したPythonコードの例です。
japanese_preprocessor.pyを使用して標準Pythonコードに変換してください。
"""

# 基本的な出力
print("こんにちは、世界！")

# 変数の定義と計算
数1 = int(input("最初の数を入力してください: "))
数2 = int(input("二番目の数を入力してください: "))

sum = 数1 + 数2
print(f"合計: {合計}")

# 条件分岐
if sum > 100:
    print("100より大きいです")
elif sum > 50:
    print("50より大きいです")
else:
    print("50以下です")

# 繰り返し処理
print("\n1から10までの数:")
for i in range(1, 11):
    print(i)

# リストの操作
果物リスト = ["りんご", "ばなな", "オレンジ", "ぶどう"]

print("\n果物リスト:")
for 果物 in 果物リスト:
    print(f"- {果物}")

# 関数定義
def 階乗計算(n):
    if n <= 1:
        return 1
    else:
        return n * 階乗計算(n - 1)

数 = 5
結果 = 階乗計算(数)
print(f"\n{数}の階乗は{結果}です")

# クラス定義
class 学生:
    def __init__(自己, 名前, 年齢):
        自己.名前 = 名前
        自己.年齢 = 年齢
    
    def 紹介(自己):
        print(f"私は{自己.名前}です。{自己.年齢}歳です。")
    
    def 年齢を増やす(自己, 年数=1):
        自己.年齢 += 年数

田中 = 学生("田中太郎", 20)
田中.紹介()
田中.年齢を増やす(1)
print("1年経過しました")
田中.紹介()

# 辞書の操作
成績 = dict()
成績["数学"] = 85
成績["英語"] = 92
成績["理科"] = 78

print("\n成績一覧:")
for 科目, 点数 in 成績.items():
    print(f"{科目}: {点数}点")

平均 = sum(成績.values()) / len(成績)
print(f"平均点: {平均:.1f}点")

# 例外処理
def 安全な除算(a, b):
    try:
        結果 = a / b
        return 結果
    except ZeroDivisionError:
        print("エラー: 0で割ることはできません")
        return None

print("\n除算テスト:")
print(f"10 / 2 = {安全な除算(10, 2)}")
print(f"10 / 0 = {安全な除算(10, 0)}")

# リスト内包表記（日本語キーワードは使用しませんが、日本語変数名は使用可能）
二乗リスト = [x**2 for x in range(1, 6)]
print(f"\n1から5の二乗: {二乗リスト}")

# ファイル操作
def ファイルに書き込む(ファイル名, 内容):
    try:
        with open(ファイル名, 'w', encoding='utf-8') as f:
            f.write(内容)
        print(f"ファイル '{ファイル名}' に書き込みました")
    except IOError as e:
        print(f"ファイル書き込みエラー: {e}")

def ファイルから読み込む(ファイル名):
    try:
        with open(ファイル名, 'r', encoding='utf-8') as f:
            内容 = f.read()
        print(f"ファイル '{ファイル名}' から読み込みました")
        return 内容
    except IOError as e:
        print(f"ファイル読み込みエラー: {e}")
        return None

テストファイル = "test_japanese.txt"
ファイルに書き込む(テストファイル, "これは日本語Pythonのテストです。\n日本語でプログラミングできます！")
読み込んだ内容 = ファイルから読み込む(テストファイル)
if 読み込んだ内容:
    print(f"内容: {読み込んだ内容}")

# 終了メッセージ
print("\nプログラムを終了します。")
