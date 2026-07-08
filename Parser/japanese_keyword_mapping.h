/*
 * Japanese Keyword Mapping for Python
 * 
 * This file provides Japanese keyword to English keyword mapping
 * to enable Japanese-based Python programming.
 * 
 * WARNING: This is an unofficial modification to CPython.
 * Use at your own risk. The developers are not responsible for any issues.
 */

#ifndef JAPANESE_KEYWORD_MAPPING_H
#define JAPANESE_KEYWORD_MAPPING_H

typedef struct {
    const char *japanese;
    const char *english;
} JapaneseKeywordMapping;

static const JapaneseKeywordMapping japanese_keyword_map[] = {
    // Control flow
    {"もし", "if"},
    {"それ以外", "else"},
    {"あるいは", "elif"},
    {"繰り返し", "for"},
    {"その間", "while"},
    {"抜ける", "break"},
    {"続ける", "continue"},
    
    // Functions and classes
    {"関数", "def"},
    {"クラス", "class"},
    {"戻る", "return"},
    {"生成する", "yield"},
    {"無名関数", "lambda"},
    
    // Import and modules
    {"読み込み", "import"},
    {"から", "from"},
    {"として", "as"},
    
    // Exception handling
    {"試す", "try"},
    {"例外", "except"},
    {"最後に", "finally"},
    {"発生させる", "raise"},
    
    // Boolean and logical
    {"かつ", "and"},
    {"または", "or"},
    {"ではない", "not"},
    {"中に", "in"},
    {"である", "is"},
    
    // Other keywords
    {"何もしない", "pass"},
    {"表明する", "assert"},
    {"グローバル", "global"},
    {"非ローカル", "nonlocal"},
    {"削除", "del"},
    {"共有して", "with"},
    {"非同期", "async"},
    {"待機する", "await"},
    
    // Constants
    {"偽", "False"},
    {"真", "True"},
    {"無", "None"},
    
    // Soft keywords
    {"一致", "match"},
    {"場合", "case"},
    {"型", "type"},
    {"遅延", "lazy"},
    
    {NULL, NULL}  // Terminator
};

#endif /* JAPANESE_KEYWORD_MAPPING_H */
