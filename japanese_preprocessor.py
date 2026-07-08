#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
日本語Pythonプリプロセッサー
日本語で書かれたPythonコードを標準のPythonコードに変換します

⚠️ 重要：これは非公式のツールです
このツールはPython Software Foundationによって公式にサポートされていません。
使用により生じたいかなる問題についても、開発者は責任を負いません。
"""

import json
import re
import sys
import os
from pathlib import Path


class JapanesePreprocessor:
    """日本語キーワードを英語に変換するプリプロセッサー"""
    
    def __init__(self, keywords_file="japanese_keywords.json"):
        """キーワードマッピングファイルを読み込む"""
        self.keywords_file = keywords_file
        self.keywords = {}
        self.builtins = {}
        self.operators = {}
        self.methods = {}
        self.syntax = {}
        self._load_keywords()
    
    def _load_keywords(self):
        """JSONファイルからキーワードマッピングを読み込む"""
        try:
            with open(self.keywords_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.keywords = data.get('keywords', {})
                self.builtins = data.get('builtins', {})
                self.operators = data.get('operators', {})
                self.methods = data.get('methods', {})
                self.syntax = data.get('syntax', {})
        except FileNotFoundError:
            print(f"警告: キーワードファイル '{self.keywords_file}' が見つかりません")
        except json.JSONDecodeError:
            print(f"警告: キーワードファイル '{self.keywords_file}' の解析に失敗しました")
    
    def _create_pattern(self, mapping):
        """キーワードマッピングから正規表現パターンを作成"""
        # キーワードを長さの降順でソート（部分一致を避けるため）
        sorted_keywords = sorted(mapping.keys(), key=len, reverse=True)
        # 単語境界を使用して、変数名の一部を置換しないようにする
        pattern = '|'.join(r'(?<!\w)' + re.escape(k) + r'(?!\w)' for k in sorted_keywords)
        return re.compile(pattern)
    
    def _protect_strings_and_comments(self, source_code):
        """文字列リテラルとコメントを一時的に保護する"""
        protected = []
        placeholders = []
        
        # 文字列リテラルのパターン（シングルクォート、ダブルクォート、トリプルクォート）
        string_patterns = [
            r'"""[^"\\]*(?:\\.[^"\\]*)*"""',
            r"'''[^'\\]*(?:\\.[^'\\]*)*'''",
            r'"[^"\\]*(?:\\.[^"\\]*)*"',
            r"'[^'\\]*(?:\\.[^'\\]*)*'"
        ]
        
        # コメントのパターン
        comment_pattern = r'#.*$'
        
        # すべてのパターンを結合
        combined_pattern = '|'.join(string_patterns + [comment_pattern])
        combined_regex = re.compile(combined_pattern, re.MULTILINE)
        
        # 文字列とコメントをプレースホルダーに置換
        def replace_with_placeholder(match):
            protected.append(match.group(0))
            placeholder = f"__PROTECTED_{len(protected)-1}__"
            placeholders.append(placeholder)
            return placeholder
        
        source_code = combined_regex.sub(replace_with_placeholder, source_code)
        
        return source_code, protected, placeholders
    
    def _restore_strings_and_comments(self, source_code, protected, placeholders):
        """保護した文字列とコメントを元に戻す"""
        for placeholder, original in zip(placeholders, protected):
            source_code = source_code.replace(placeholder, original)
        return source_code
    
    def replace_keywords(self, source_code):
        """キーワードを置換する"""
        # 文字列とコメントを保護
        source_code, protected, placeholders = self._protect_strings_and_comments(source_code)
        
        # キーワードの置換
        keyword_pattern = self._create_pattern(self.keywords)
        
        def keyword_replacer(match):
            return self.keywords[match.group(0)]
        
        source_code = keyword_pattern.sub(keyword_replacer, source_code)
        
        # 組み込み関数の置換
        builtin_pattern = self._create_pattern(self.builtins)
        
        def builtin_replacer(match):
            return self.builtins[match.group(0)]
        
        source_code = builtin_pattern.sub(builtin_replacer, source_code)
        
        # メソッドの置換
        method_pattern = self._create_pattern(self.methods)
        
        def method_replacer(match):
            return self.methods[match.group(0)]
        
        source_code = method_pattern.sub(method_replacer, source_code)
        
        # 構文の置換
        syntax_pattern = self._create_pattern(self.syntax)
        
        def syntax_replacer(match):
            return self.syntax[match.group(0)]
        
        source_code = syntax_pattern.sub(syntax_replacer, source_code)
        
        # 演算子の置換
        operator_pattern = self._create_pattern(self.operators)
        
        def operator_replacer(match):
            return self.operators[match.group(0)]
        
        source_code = operator_pattern.sub(operator_replacer, source_code)
        
        # 文字列とコメントを復元
        source_code = self._restore_strings_and_comments(source_code, protected, placeholders)
        
        return source_code
    
    def process_file(self, input_file, output_file=None):
        """ファイルを処理する"""
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                source_code = f.read()
        except FileNotFoundError:
            print(f"エラー: 入力ファイル '{input_file}' が見つかりません")
            return False
        except UnicodeDecodeError:
            print(f"エラー: ファイル '{input_file}' のエンコーディングがUTF-8ではありません")
            return False
        
        # キーワード置換
        processed_code = self.replace_keywords(source_code)
        
        # 出力ファイルの決定
        if output_file is None:
            input_path = Path(input_file)
            output_file = input_path.stem + '_converted' + input_path.suffix
        
        # 処理済みコードを書き込み
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(processed_code)
            print(f"変換完了: {input_file} -> {output_file}")
            return True
        except IOError as e:
            print(f"エラー: 出力ファイル '{output_file}' の書き込みに失敗しました: {e}")
            return False
    
    def process_string(self, source_code):
        """文字列を直接処理する"""
        return self.replace_keywords(source_code)


def main():
    """コマンドラインインターフェース"""
    if len(sys.argv) < 2:
        print("使用方法: python japanese_preprocessor.py <入力ファイル> [出力ファイル]")
        print("例: python japanese_preprocessor.py script.py")
        print("例: python japanese_preprocessor.py script.py script_converted.py")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    preprocessor = JapanesePreprocessor()
    success = preprocessor.process_file(input_file, output_file)
    
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
