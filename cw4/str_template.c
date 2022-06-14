#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

// consider chars from [FIRST_CHAR, LAST_CHAR)
#define FIRST_CHAR 33
#define LAST_CHAR 127
#define MAX_CHARS (LAST_CHAR - FIRST_CHAR)
#define MAX_DIGRAMS (LAST_CHAR - FIRST_CHAR) * (LAST_CHAR - FIRST_CHAR)

#define NEWLINE '\n'
#define IN_WORD 1

#define IN_LINE_COMMENT 1
#define IN_BLOCK_COMMENT 2

#define MAX_LINE 128

int count_chars[MAX_CHARS] = { 0 };
int count_digrams[MAX_DIGRAMS] = { 0 };

// function to be used as comparator to qsort (compares counters and thes sorts
// alphabetically when equal)
int cmp (const void *a, const void *b) {
	int va = *(int*)a;
	int vb = *(int*)b;
	if (count_chars[va] == count_chars[vb]) return count_chars[va] - count_chars[vb]; // sort alphabetically if counts equal
	return count_chars[vb] - count_chars[va];
}

// function to be used as comparator to qsort for digrams (compares counters and
// thes sorts alphabetically when equal)
int cmp_di (const void *a, const void *b) {
	int va = *(int*)a;
	int vb = *(int*)b;
	// sort according to second char if counts and the first char equal
	if (count_digrams[va] == count_digrams[vb] && va / MAX_CHARS == vb / MAX_CHARS) return va % MAX_CHARS - vb % MAX_CHARS;
	// sort according to first char if counts equal
	if (count_digrams[va] == count_digrams[vb]) return va / MAX_CHARS - vb / MAX_CHARS;
	return count_digrams[vb] - count_digrams[va];
}

// count number of lines (nl), number of words (nw) and number of characters
// (nc) in the text read from stdin
// DONE
void wc(int *nl, int *nw, int *nc) {
	int char_count = 0;
	int total = 0;
	int total_chars = 0;
	int lines = 0;
	int words = 0;
	char line[MAX_LINE];
	char word[MAX_LINE];
	while (fgets(line, MAX_LINE, stdin) != NULL) {
		lines += 1;
		total_chars += strlen(line);
		total = 0;
		char_count = 0;
		while (sscanf(&line[total], "%s%n", word, &char_count) != EOF) {
			words += 1;
			total += char_count+1;
		}
	}
	*nl = lines;
	*nw = words;
	*nc = total_chars;
}

// count how many times each character from [FIRST_CHAR, LAST_CHAR) occurs
// in the text read from stdin. Sort chars according to their respective
// cardinalities (decreasing order). Set n_char and cnt to the char_no - th char
// in the sorted list and its cardinality respectively
void char_count(int char_no, int *n_char, int *cnt){
	int len;
	char line[MAX_LINE];
	while (fgets(line, MAX_LINE, stdin) != NULL){
		len = strlen(line);
		for (int i = 0; i < len; i++){
			if ((int)line[i] >= FIRST_CHAR && (int)line[i] <= LAST_CHAR){
				count_chars[(int)line[i] - FIRST_CHAR] += 1;
			}
		}
	}
	int indexes[MAX_CHARS];
	for (int i = 0; i < MAX_CHARS; i++){
		indexes[i] = i;
	}

	qsort(indexes, MAX_CHARS, sizeof(int), cmp);

	*n_char = indexes[char_no-1] + FIRST_CHAR;
	*cnt = count_chars[indexes[char_no-1]];
}

// count how many times each digram (a pair of characters, from [FIRST_CHAR,
// LAST_CHAR) each) occurs in the text read from stdin. Sort digrams according
// to their respective cardinalities (decreasing order). Set digram[0] and
// digram[1] to the first and the second char in the digram_no - th digram_char
// in the sorted list. Set digram[2] to its cardinality.
void digram_count(int digram_no, int digram[]){
	int len;
	char line[MAX_LINE];
	while (fgets(line, MAX_LINE, stdin) != NULL){
		len = strlen(line);
		for (int i = 0; i < len; i++){
			if ((int)line[i] >= FIRST_CHAR && (int)line[i] <= LAST_CHAR && (int)line[i+1] >= FIRST_CHAR && (int)line[i+1] <= LAST_CHAR){
				count_digrams[((int)line[i] - FIRST_CHAR)*MAX_CHARS + (int)line[i+1] - FIRST_CHAR] += 1;
			}
		}
	}
	int indexes[MAX_DIGRAMS];
	for (int i = 0; i < MAX_DIGRAMS; i++){
		indexes[i] = i;
	}

	qsort(indexes, MAX_DIGRAMS, sizeof(int), cmp_di);

	digram[0] = (indexes[digram_no-1] / MAX_CHARS) + FIRST_CHAR;
	digram[1] = (indexes[digram_no-1] % MAX_CHARS) + FIRST_CHAR;
	digram[2] = count_digrams[indexes[digram_no-1]];
	
}

// Count block and line comments in the text read from stdin. Set
// line_comment_counter and block_comment_counter accordingly
void find_comments(int *line_comment_counter, int *block_comment_counter){
	char line[MAX_LINE];
	int lcc = 0;
	int bcc = 0;
	int flag = 0;
	int len;
	while (fgets(line, MAX_LINE, stdin) != NULL){
		len = strlen(line);
		for (int i = 0; i < len; i++) {
			if (line[i] == '/' && line[i+1] == '/' && flag == 0){
				lcc += 1;
				i++;
				break;
			}
			else if (line[i] == '/' && line[i+1] == '*' && flag == 0)
			{
				bcc += 1;
				i++;
				flag = IN_BLOCK_COMMENT;
			}
			else if (line[i] == '*' && line[i+1] == '/' && flag == IN_BLOCK_COMMENT)
			{
				flag = 0;
				i++;
			}
		}
	}

	*line_comment_counter = lcc;
	*block_comment_counter = bcc;
}

int read_line() {
	char line[MAX_LINE];
	int n;

	fgets (line, MAX_LINE, stdin); // to get the whole line
	sscanf (line, "%d", &n);
	return n;
}

int main(void) {
	int to_do;
	int nl, nw, nc, char_no, n_char, cnt;
	int line_comment_counter, block_comment_counter;
	int digram[3];

	to_do = read_line();
	switch (to_do) {
		case 1: // wc()
			wc (&nl, &nw, &nc);
			printf("%d %d %d\n", nl, nw, nc);
			break;
		case 2: // char_count()
			char_no = read_line();
			char_count(char_no, &n_char, &cnt);
			printf("%c %d\n", n_char, cnt);
			break;
		case 3: // digram_count()
			char_no = read_line();
			digram_count(char_no, digram);
			printf("%c%c %d\n", digram[0], digram[1], digram[2]);
			break;
		case 4:
			find_comments(&line_comment_counter, &block_comment_counter);
			printf("%d %d\n", block_comment_counter, line_comment_counter);
			break;
		default:
			printf("NOTHING TO DO FOR %d\n", to_do);
			break;
	}
	return 0;
}

