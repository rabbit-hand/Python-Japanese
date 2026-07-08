"""
Japanese Keyword Module for Python

This module provides Japanese keyword support for Python programming.
It enables Japanese-based Python programming by converting Japanese keywords
to English keywords before execution.

WARNING: This is an unofficial modification to Python.
Use at your own risk. The developers are not responsible for any issues.
"""

import re
import sys

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

# Reverse mapping for display purposes
ENGLISH_TO_JAPANESE_MAP = {v: k for k, v in JAPANESE_KEYWORD_MAP.items()}
ENGLISH_TO_JAPANESE_BUILTIN_MAP = {v: k for k, v in JAPANESE_BUILTIN_MAP.items()}

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

def is_japanese_keyword(word):
    """
    Check if a word is a Japanese keyword.
    
    Args:
        word: String to check
        
    Returns:
        Boolean indicating if the word is a Japanese keyword
    """
    return word in JAPANESE_KEYWORD_MAP

def get_english_keyword(japanese_keyword):
    """
    Get the English equivalent of a Japanese keyword.
    
    Args:
        japanese_keyword: Japanese keyword string
        
    Returns:
        English keyword string or None if not found
    """
    return JAPANESE_KEYWORD_MAP.get(japanese_keyword)

def get_japanese_keyword(english_keyword):
    """
    Get the Japanese equivalent of an English keyword.
    
    Args:
        english_keyword: English keyword string
        
    Returns:
        Japanese keyword string or None if not found
    """
    return ENGLISH_TO_JAPANESE_MAP.get(english_keyword)

def exec_japanese(code, globals_dict=None, locals_dict=None):
    """
    Execute Python code with Japanese keywords and builtin functions.
    
    Args:
        code: String containing Python code with Japanese keywords and builtins
        globals_dict: Global namespace dictionary (optional)
        locals_dict: Local namespace dictionary (optional)
    """
    if globals_dict is None:
        globals_dict = globals()
    if locals_dict is None:
        locals_dict = globals_dict
    
    converted_code = convert_japanese_code(code)
    exec(converted_code, globals_dict, locals_dict)

def compile_japanese(source, filename, mode, flags=0, dont_inherit=False):
    """
    Compile Python code with Japanese keywords and builtin functions.
    
    Args:
        source: String containing Python code with Japanese keywords and builtins
        filename: Filename for error messages
        mode: Compilation mode ('exec', 'eval', or 'single')
        flags: Compiler flags (optional)
        dont_inherit: If True, don't inherit __future__ imports (optional)
        
    Returns:
        Code object
    """
    converted_source = convert_japanese_code(source)
    return compile(converted_source, filename, mode, flags, dont_inherit)

# List of all Japanese keywords
japanese_kwlist = list(JAPANESE_KEYWORD_MAP.keys())

# Check if a word is a Japanese keyword
isjapanesekeyword = frozenset(japanese_kwlist).__contains__

__all__ = [
    'JAPANESE_KEYWORD_MAP',
    'JAPANESE_BUILTIN_MAP',
    'ENGLISH_TO_JAPANESE_MAP',
    'ENGLISH_TO_JAPANESE_BUILTIN_MAP',
    'convert_japanese_keywords',
    'convert_japanese_builtins',
    'convert_japanese_code',
    'is_japanese_keyword',
    'get_english_keyword',
    'get_japanese_keyword',
    'exec_japanese',
    'compile_japanese',
    'japanese_kwlist',
    'isjapanesekeyword',
]
