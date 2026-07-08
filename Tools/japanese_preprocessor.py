#!/usr/bin/env python3
"""
Japanese Python Preprocessor

This script converts Japanese keywords to English keywords before execution.
This enables Japanese-based Python programming while maintaining compatibility
with standard Python.

WARNING: This is an unofficial modification to Python.
Use at your own risk. The developers are not responsible for any issues.
"""

import re
import sys
import os

# Japanese to English keyword mapping
JAPANESE_KEYWORD_MAP = {
    # Control flow
    'もし': 'if',
    'それ以外': 'else',
    'あるいは': 'elif',
    '繰り返し': 'for',
    'その間': 'while',
    '抜ける': 'break',
    '続ける': 'continue',
    
    # Functions and classes
    '関数': 'def',
    'クラス': 'class',
    '戻る': 'return',
    '生成する': 'yield',
    '無名関数': 'lambda',
    
    # Import and modules
    '読み込み': 'import',
    'から': 'from',
    'として': 'as',
    
    # Exception handling
    '試す': 'try',
    '例外': 'except',
    '最後に': 'finally',
    '発生させる': 'raise',
    
    # Boolean and logical
    'かつ': 'and',
    'または': 'or',
    'ではない': 'not',
    '中に': 'in',
    'である': 'is',
    
    # Other keywords
    '何もしない': 'pass',
    '表明する': 'assert',
    'グローバル': 'global',
    '非ローカル': 'nonlocal',
    '削除': 'del',
    '共有して': 'with',
    '非同期': 'async',
    '待機する': 'await',
    
    # Constants
    '偽': 'False',
    '真': 'True',
    '無': 'None',
    
    # Soft keywords
    '一致': 'match',
    '場合': 'case',
    '型': 'type',
    '遅延': 'lazy',
}

# Japanese to English builtin function mapping
JAPANESE_BUILTIN_MAP = {
    # I/O functions
    '表示': 'print',
    '入力': 'input',
    
    # Type conversion
    '整数': 'int',
    '浮動小数': 'float',
    '文字列': 'str',
    '論理値': 'bool',
    'リスト': 'list',
    '辞書': 'dict',
    '集合': 'set',
    'タプル': 'tuple',
    'バイト列': 'bytes',
    
    # Sequence operations
    '長さ': 'len',
    '範囲': 'range',
    '列挙': 'enumerate',
    '圧縮': 'zip',
    '反転': 'reversed',
    'ソート済み': 'sorted',
    
    # Math operations
    '絶対値': 'abs',
    '最小': 'min',
    '最大': 'max',
    '合計': 'sum',
    '累乗': 'pow',
    '四捨五入': 'round',
    
    # Functional operations
    '写像': 'map',
    'フィルター': 'filter',
    '任意': 'any',
    '全て': 'all',
    
    # Object operations
    '種類': 'type',
    'ID': 'id',
    'ハッシュ': 'hash',
    '属性取得': 'getattr',
    '属性設定': 'setattr',
    '属性削除': 'delattr',
    '属性有無': 'hasattr',
    
    # File operations
    '開く': 'open',
    
    # Other
    '助言': 'help',
    '実行': 'exec',
    '評価': 'eval',
    'コンパイル': 'compile',
    '辞書化': 'dict',
    '集合化': 'set',
    'リスト化': 'list',
    'タプル化': 'tuple',
}

def convert_japanese_keywords(code):
    """
    Convert Japanese keywords to English keywords in the given code.
    
    Args:
        code: String containing Python code with Japanese keywords
        
    Returns:
        String with Japanese keywords replaced by English keywords
    """
    # Sort keywords by length (longest first) to avoid partial matches
    sorted_keywords = sorted(JAPANESE_KEYWORD_MAP.keys(), key=len, reverse=True)
    
    # Create a pattern that matches Japanese keywords as whole words
    pattern = r'\b(' + '|'.join(re.escape(kw) for kw in sorted_keywords) + r')\b'
    
    def replace_keyword(match):
        japanese = match.group(0)
        return JAPANESE_KEYWORD_MAP[japanese]
    
    # Replace keywords
    converted_code = re.sub(pattern, replace_keyword, code)
    
    return converted_code

def convert_japanese_builtins(code):
    """
    Convert Japanese builtin functions to English builtin functions in the given code.
    
    Args:
        code: String containing Python code with Japanese builtin functions
        
    Returns:
        String with Japanese builtin functions replaced by English builtin functions
    """
    # Sort builtins by length (longest first) to avoid partial matches
    sorted_builtins = sorted(JAPANESE_BUILTIN_MAP.keys(), key=len, reverse=True)
    
    # Create a pattern that matches Japanese builtin functions as whole words
    pattern = r'\b(' + '|'.join(re.escape(bi) for bi in sorted_builtins) + r')\b'
    
    def replace_builtin(match):
        japanese = match.group(0)
        return JAPANESE_BUILTIN_MAP[japanese]
    
    # Replace builtins
    converted_code = re.sub(pattern, replace_builtin, code)
    
    return converted_code

def convert_japanese_code(code):
    """
    Convert both Japanese keywords and builtin functions to English.
    
    Args:
        code: String containing Python code with Japanese keywords and builtins
        
    Returns:
        String with all Japanese keywords and builtins replaced by English equivalents
    """
    # First convert keywords, then builtins
    converted_code = convert_japanese_keywords(code)
    converted_code = convert_japanese_builtins(converted_code)
    
    return converted_code

def process_file(input_file, output_file=None):
    """
    Process a Python file and convert Japanese keywords and builtin functions.
    
    Args:
        input_file: Path to the input Python file
        output_file: Path to the output file (optional, defaults to input_file)
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        code = f.read()
    
    converted_code = convert_japanese_code(code)
    
    if output_file is None:
        output_file = input_file
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(converted_code)
    
    print(f"Converted {input_file} -> {output_file}")

def execute_japanese_python(file_path):
    """
    Execute a Python file with Japanese keywords and builtin functions by converting it first.
    
    Args:
        file_path: Path to the Python file with Japanese keywords and builtins
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()
    
    converted_code = convert_japanese_code(code)
    
    # Execute the converted code
    exec(converted_code, globals())

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Japanese preprocessor: python japanese_preprocessor.py <input_file> [output_file]")
        print("  Execute Japanese Python: python japanese_preprocessor.py --exec <file>")
        sys.exit(1)
    
    if sys.argv[1] == '--exec':
        if len(sys.argv) < 3:
            print("Error: --exec requires a file argument")
            sys.exit(1)
        execute_japanese_python(sys.argv[2])
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        process_file(input_file, output_file)

if __name__ == '__main__':
    main()
