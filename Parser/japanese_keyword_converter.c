/*
 * Japanese Keyword Converter for Python
 * 
 * This file provides functionality to convert Japanese keywords to English
 * before the parser processes them.
 * 
 * WARNING: This is an unofficial modification to CPython.
 * Use at your own risk. The developers are not responsible for any issues.
 */

#include "japanese_keyword_mapping.h"
#include <string.h>
#include <ctype.h>

/*
 * Convert a Japanese keyword to its English equivalent.
 * Returns the English keyword if found, otherwise returns the original string.
 */
const char*
convert_japanese_keyword(const char *token)
{
    if (token == NULL) {
        return NULL;
    }
    
    for (int i = 0; japanese_keyword_map[i].japanese != NULL; i++) {
        if (strcmp(token, japanese_keyword_map[i].japanese) == 0) {
            return japanese_keyword_map[i].english;
        }
    }
    
    return token;  // Return original if not a Japanese keyword
}

/*
 * Check if a string is a Japanese keyword.
 * Returns 1 if it is, 0 otherwise.
 */
int
is_japanese_keyword(const char *token)
{
    if (token == NULL) {
        return 0;
    }
    
    for (int i = 0; japanese_keyword_map[i].japanese != NULL; i++) {
        if (strcmp(token, japanese_keyword_map[i].japanese) == 0) {
            return 1;
        }
    }
    
    return 0;
}

/*
 * Get the English equivalent of a Japanese keyword.
 * Returns NULL if the token is not a Japanese keyword.
 */
const char*
get_english_keyword(const char *japanese_token)
{
    if (japanese_token == NULL) {
        return NULL;
    }
    
    for (int i = 0; japanese_keyword_map[i].japanese != NULL; i++) {
        if (strcmp(japanese_token, japanese_keyword_map[i].japanese) == 0) {
            return japanese_keyword_map[i].english;
        }
    }
    
    return NULL;
}
