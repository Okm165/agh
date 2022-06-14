#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define IN_LINE_COMMENT 1
#define IN_BLOCK_COMMENT 2
#define IN_STRING 4
#define IN_ID 8
#define IN_QUOTE 16
#define IN_BACKSLASH 32

#define MAX_ID_LEN 64
#define MAX_IDS 1024

// mod
#define MAX_LINE 128

int index_cmp(const void *, const void *);
int cmp(const void *, const void *);

char tab[MAX_IDS][MAX_ID_LEN];

char *keywords[] = {
	"auto", "break", "case", "char",
	"const", "continue", "default", "do",
	"double", "else", "enum", "extern",
	"float", "for", "goto", "if",
	"int", "long", "register", "return",
	"short", "signed", "sizeof", "static",
	"struct", "switch", "typedef", "union",
	"unsigned", "void", "volatile", "while"};

char* ext_keywords[] = {
"auto",
"break",
"case",
"char",
"const",
"continue",
"default",
"do",
"double",
"else",
"enum",
"extern",
"float",
"for",
"goto",
"if",
"inline",
"int",
"long",
"register",
"restrict",
"return",
"short",
"signed",
"sizeof",
"static",
"struct",
"switch",
"typedef",
"union",
"unsigned",
"void",
"volatile",
"while",
"_Alignas",
"_Alignof",
"_Atomic",
"_Bool",
"_Complex",
"_Decimal128",
"_Decimal32",
"_Decimal64",
"_Generic",
"_Imaginary",
"_Noreturn",
"_Static_assert",
"_Thread_local",
"if",
"elif",
"else",
"endif",
"ifdef",
"ifndef",
"define",
"undef",
"include",
"line",
"error",
"pragma",
"defined",
"__has_c_attribute",
"__int8",
"__int16",
"__int32",
"__int64",
};

struct FLAG {
	int com;
	int str;
	int ide;
	int bck;
};

// is letter
int isl(char c)
{
	return (c > 64 && c < 91) || (c > 96 && c < 123) || (c == 95);
}
// is number
int isn(char c)
{
	return (c > 47 && c < 58);
}
// is letter or number
int islon(char c)
{
	return isl(c) || isn(c);
}
int iskeyword(char *c)
{
	for (int i = 0; i < 65; i++)
	{
		if (!cmp(&c, &ext_keywords[i]))
		{
			return 1;
		}
	}
	return 0;
}
void approve_candidate(int* ptr_tab)
{
	int approved = 1;
	for (int i = 0; i < *ptr_tab; i++){
		if (!index_cmp(&i, ptr_tab))
		{
			approved = 0;
			break;
		}
	}
	if (approved)
	{
		*ptr_tab += 1;
	}
}
int line_comment_starts(char* line, int* i, struct FLAG* flag)
{
	if (line[*i] == '/' && line[*i + 1] == '/' && flag->com == 0 && flag->str == 0)
	{
		// flag->com = IN_LINE_COMMENT;
		(*i)++;
		return 1;
	}
	return 0;
}
int block_comment_starts(char* line, int* i, struct FLAG* flag)
{
	if (line[*i] == '/' && line[*i + 1] == '*' && flag->com == 0 && flag->str == 0)
	{
		flag->com = IN_BLOCK_COMMENT;
		(*i)++;
		return 1;
	}
	return 0;
}
int block_comment_ends(char* line, int* i, struct FLAG* flag)
{
	if (line[*i] == '*' && line[*i + 1] == '/' && flag->com == IN_BLOCK_COMMENT && flag->str == 0)
	{
		flag->com = 0;
		(*i)++;
		return 1;
	}
	return 0;
}
int string_starts(char* line, int* i, struct FLAG* flag)
{
	if (line[*i] == '"' && flag->com == 0 && flag->str == 0 && flag->bck == 0)
	{
		flag->str = IN_STRING;
		return 1;
	}
	return 0;
}
int string_ends(char* line, int* i, struct FLAG* flag)
{
	if (line[*i] == '"' && flag->com == 0 && flag->str == IN_STRING && flag->bck == 0)
	{
		flag->str = 0;
		return 1;
	}
	return 0;
}
int quote_starts(char* line, int* i, struct FLAG* flag)
{
	if (line[*i] == '\'' && flag->com == 0 && flag->str == 0 && flag->bck == 0)
	{
		flag->str = IN_QUOTE;
		return 1;
	}
	return 0;
}
int quote_ends(char* line, int* i, struct FLAG* flag)
{
	if (line[*i] == '\'' && flag->com == 0 && flag->str == IN_QUOTE && flag->bck == 0)
	{
		flag->str = 0;
		return 1;
	}
	return 0;
}
int id_starts(char* line, int* i, struct FLAG* flag)
{
	if (isl(line[*i]) && flag->com == 0 && flag->str == 0 && flag->ide == 0)
	{
		flag->ide = IN_ID;
		return 1;
	}
	return 0;
}
int id_continues(char* line, int* i, struct FLAG* flag)
{
	if (islon(line[*i]) && flag->com == 0 && flag->str == 0 && flag->ide == IN_ID)
	{
		flag->ide = IN_ID;
		return 1;
	}
	return 0;
}
int id_ends(char* line, int* i, struct FLAG* flag)
{
	if (!islon(line[*i]) && flag->com == 0 && flag->str == 0 && flag->ide == IN_ID)
	{
		flag->ide = 0;
		return 1;
	}
	return 0;
}

int find_idents()
{
	struct FLAG flag;
	flag.com = 0;
	flag.str = 0;
	flag.ide = 0;
	flag.bck = 0;

	int ptr_tab = 0;
	int ptr_cnd = 0;
	int len = 0;
	char line[MAX_LINE];

	while (fgets(line, MAX_LINE, stdin) != NULL)
	{
		len = strlen(line);
		char candidate[MAX_ID_LEN];
		
		for (int i = 0; i < len; i++){
			if (line[i] == '\\'){
				i++;
				continue;
			}
			else if (line_comment_starts(line, &i, &flag)){
				candidate[ptr_cnd] = 0;
				if (!iskeyword(candidate)){
					memcpy(&tab[ptr_tab], candidate, ptr_cnd+1);
					approve_candidate(&ptr_tab);
				}
				break;
			}
			else if (block_comment_starts(line, &i, &flag)){
				continue;
			}
			else if (block_comment_ends(line, &i, &flag)){
				continue;
			}
			else if (string_starts(line, &i, &flag)){
				continue;
			}
			else if (string_ends(line, &i, &flag)){
				continue;
			}
			else if (quote_starts(line, &i, &flag)){
				continue;
			}
			else if (quote_ends(line, &i, &flag)){
				continue;
			}
			else if(isn(line[i]) && flag.com == 0 && flag.str == 0 && flag.ide == 0){
				// skip word
				while (i < len && line[i] != ' '){
					i++;
				}
			}
			else if (id_starts(line, &i, &flag)){
				ptr_cnd = 0;
				candidate[ptr_cnd] = line[i];
				ptr_cnd += 1;
				continue;
			}
			else if (id_continues(line, &i, &flag)){
				candidate[ptr_cnd] = line[i];
				ptr_cnd += 1;
				continue;
			}
			else if (id_ends(line, &i, &flag)){
				candidate[ptr_cnd] = 0;
				if (!iskeyword(candidate)){
					memcpy(&tab[ptr_tab], candidate, ptr_cnd+1);
					approve_candidate(&ptr_tab);
				}
			}
		}
	}
	
	// for (int i = 0; i < ptr_tab; i++)
	// {
	// 	printf("%s ", tab[i]);
	// }
	return ptr_tab;
}

int cmp(const void *first_arg, const void *second_arg)
{
	char *a = *(char **)first_arg;
	char *b = *(char **)second_arg;
	return strcmp(a, b);
}

int index_cmp(const void *first_arg, const void *second_arg)
{
	int a = *(int *)first_arg;
	int b = *(int *)second_arg;
	return strcmp(tab[a], tab[b]);
}

int main(void)
{
	printf("%d\n", find_idents());
	return 0;
}
