#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

#define BUFFER_SIZE 1024
#define MAX_RATE 4
#define MEMORY_ALLOCATION_ERROR  -1
#define LIST_ERROR               -2
#define PROGRAM_ERROR            -3

typedef union data_union {
	int int_data;
	char char_data;
	void *ptr_data;
} data_union;

typedef void (*DataFp)(data_union);
typedef void (*DataPFp)(data_union*);
typedef  int (*CompareDataFp)(data_union, data_union);
typedef  int (*HashFp)(data_union, int);

typedef struct ht_element {
	struct ht_element *next;
	data_union data;
} ht_element;

typedef struct hash_table {
	int size;
	int no_elements;
	ht_element **ht;
	DataFp dump_data;
	DataFp free_data;
	CompareDataFp compare_data;
	HashFp hash_function;
	DataPFp modify_data;
} hash_table;

void insert_element(hash_table *p_table, data_union data);

void *safe_malloc(size_t size) {
	void *ptr = malloc(size);
	if(ptr) return ptr;
	exit(MEMORY_ALLOCATION_ERROR);
}

// ---------------------- functions to implement

// initialize table fields
void init_ht(hash_table *p_table, int size, DataFp dump_data, DataFp free_data,
		 CompareDataFp compare_data, HashFp hash_function, DataPFp modify_data) {
			 p_table->size = size;
			 p_table->no_elements = 0;
			 p_table->ht = (ht_element **)safe_malloc(sizeof(ht_element)*size);
			 memset(p_table->ht, 0, sizeof(ht_element)*size);

			 p_table->dump_data = dump_data;
			 p_table->free_data = free_data;
			 p_table->compare_data = compare_data;
			 p_table->hash_function = hash_function;
			 p_table->modify_data = modify_data;
			 return;

}

// print elements of the list with hash n
void dump_list(const hash_table* p_table, int n) {
	ht_element* element = p_table->ht[n];
	while (element != NULL) {
		p_table->dump_data(element->data);
		element = element->next;
	}
	return;
}

// Free element pointed by data_union using free_data() function
void free_element(DataFp free_data, ht_element *to_delete) {
	if (free_data != NULL){
		free_data(to_delete->data);
	}
	free(to_delete);
	return;
}

// free all elements from the table (and the table itself)
void free_table(hash_table* p_table) {
	ht_element* element;
	ht_element* next;
	for (int i = 0; i < p_table->size; i++) {	// for every cell in ht
		element = p_table->ht[i];
		while (element != NULL) {				// for every element in list that hash to same hash
			next = element->next;
			free_element(p_table->free_data, element);
			element = next;
		}
	}
	// after this every cell in ht is deeply freed, lets free table now
	free(p_table->ht);
	return;
}

// calculate hash function for integer k
int hash_base(int k, int size) {
	static const double c = 0.618033988; // (sqrt(5.) – 1) / 2.;
	double tmp = k * c;
	return (int)floor(size * (tmp - floor(tmp)));
}

// find element; return pointer to previous
ht_element *find_previous(hash_table *p_table, data_union data, int *first) {
	*first = 0;
	int hash = p_table->hash_function(data, p_table->size);
	ht_element* element = p_table->ht[hash];
	if (element == NULL) return NULL;
	if (p_table->compare_data(element->data, data) == 0) {
		*first = 1;
		return NULL;
	}
	ht_element *prev, *curr;
	prev = element;
	curr = prev->next;
	while (curr != NULL) {
		if (p_table->compare_data(curr->data, data) == 0) {
			return prev;
		}
		prev = curr;
		curr = curr->next;
	}
	return NULL;
}


// return pointer to element with given value
ht_element *get_element(hash_table *p_table, data_union data) {
	int hash = p_table->hash_function(data, p_table->size);
	ht_element* element = p_table->ht[hash];
	while (element != NULL) {
		if (p_table->compare_data(element->data, data) == 0){
			return element;
		}
		element = element->next;
	}
	return NULL;
}

void rehash(hash_table *p_table) {
	// create a temporary linked list of all elements
	ht_element guard, *prev = &guard, *p, *q;
	guard.next = NULL;
	for(int i=0; i<p_table->size; ++i) {
		p = p_table->ht[i];
		while(p) {
			prev->next = p;
			prev = p;
			p = p->next;
		}
	}
	// resize the table of pointers and set them to NULL
	p_table->size *= 2;
	p_table->ht = realloc(p_table->ht, p_table->size * sizeof(ht_element*));
	// for(ht_element **p=p_table->ht; p; ++p) *p = NULL;
	memset(p_table->ht, 0, p_table->size * sizeof(ht_element*));
	// calculate new hashes and insert elements in appropriate spots
	p = guard.next;
	while(p) {
		int i = p_table->hash_function(p->data, p_table->size);
		q = p->next;
		p->next = p_table->ht[i];
		p_table->ht[i] = p;
		p = q;
	}
	return;
}

// insert element
void insert_element(hash_table *p_table, data_union data) {
	if (get_element(p_table, data)) return;

	ht_element *new_element = (ht_element *)safe_malloc(sizeof(ht_element));
	new_element->data = data;
	new_element->next = NULL;

	int hash = p_table->hash_function(data, p_table->size);
	new_element->next = p_table->ht[hash];
	p_table->ht[hash] = new_element;
	p_table->no_elements += 1;

	if (p_table->no_elements/p_table->size > MAX_RATE) {
		rehash(p_table);
	}

	return;
}

// remove element
void remove_element(hash_table *p_table, data_union data) {
	int first;
	ht_element *prev = find_previous(p_table, data, &first);
	ht_element *toremove = NULL;
	if(first == 1) {
		int i = p_table->hash_function(data, p_table->size);
		toremove = p_table->ht[i];
		p_table->ht[i] = toremove->next;
	}

	if(prev) {
		toremove = prev->next;
		prev->next = toremove->next;
	}

	if(toremove) {
		free_element(p_table->free_data, toremove);
		p_table->no_elements -= 1;
	}
	// printf("%d ", first);

	return;
}

// type-specific definitions

// int element

int hash_int(data_union data, int size) {
	return hash_base(data.int_data, size);
}

void dump_int(data_union data) {
	printf("%d ", data.int_data);
	return;
}

int cmp_int(data_union a, data_union b) {
	return a.int_data - b.int_data;
}

// read int value and insert to the union
data_union create_data_int() {
	data_union uni;
	scanf("%d", &uni.int_data);
	return uni;
}

// char element

int hash_char(data_union data, int size) {
	return hash_base((int)data.char_data, size);
}

void dump_char(data_union data) {
	printf("%c ", data.char_data);
	return;
}

int cmp_char(data_union a, data_union b) {
	return (int)a.char_data - (int)b.char_data;
}

// read char value and insert to the union
data_union create_data_char() {
	data_union uni;
	scanf(" %c", &uni.char_data);
	return uni;
}

// Word element

typedef struct DataWord {
	char *word;
	int counter;
} DataWord;

void dump_word(data_union data) {
	printf("%s %d ", ((DataWord*)data.ptr_data)->word, ((DataWord*)data.ptr_data)->counter);
	return;
}

void free_word(data_union data) {
	free(((DataWord*)data.ptr_data)->word);
	free(data.ptr_data);
	return;
}

int cmp_word(data_union a, data_union b) {
	return strcmp(((DataWord*)a.ptr_data)->word, ((DataWord*)b.ptr_data)->word);
}

int hash_word(data_union data, int size) {
	int s = 0;
	DataWord *dw = (DataWord*)data.ptr_data;
	char *p = dw->word;
	while (*p) {
		s += *p++;
	}
	return hash_base(s, size);
}

// increase the counter
void modify_word(data_union *data) {
	((DataWord*)data->ptr_data)->counter += 1;
	return;
}

// allocate DataWord structure and insert to the union
data_union create_data_word(char *value) {
	data_union uni;
	DataWord *dataword = safe_malloc(sizeof(DataWord));
	dataword->word = safe_malloc(strlen(value)+1);
	dataword->counter = 1;
	strcpy(dataword->word, value);
	uni.ptr_data = dataword;
	return uni;
}

// read text, parse it to words, and insert those words to the hashtable
void stream_to_ht(hash_table *p_table, FILE *stream) {
	char buffer[BUFFER_SIZE];
	const char tokens[] = " .,?!:;-\n\t\r";
	char *token;
	while (fgets(buffer, BUFFER_SIZE, stream) != NULL) {
		token = strtok(buffer, tokens);

		while (token != NULL)
		{
			if (strlen(token) == 0)
				continue;

			char *str = strdup(token);

			for (int i = 0; i < strlen(str); i++)
			{
				str[i] = tolower(str[i]);
			}

			data_union data = create_data_word(str);

			ht_element *el = get_element(p_table, data);
			if(el) {
				modify_word(&el->data);
				free_word(data);
			}
			else {
				insert_element(p_table, data);
			}

			token = strtok(NULL, tokens);
		}

		memset(buffer, 0, BUFFER_SIZE);
	}
}

// test primitive type list
void table_test(hash_table *p_table, int n, data_union (*create_data)()) {
	char op;
	data_union data;
	for (int i = 0; i < n; ++i) {
		scanf(" %c", &op);
		data = create_data();
		switch (op) {
			case 'r':
				remove_element(p_table, data);
				break;
			case 'i':
				insert_element(p_table, data);
				break;
			default:
				printf("No such operation: %c\n", op);
				break;
		}
	}
}

int main(void) {
	int to_do, n, index;
	hash_table table;
	char buffer[BUFFER_SIZE];
	data_union data;

	scanf ("%d", &to_do);
	switch (to_do) {
		case 1: // test integer table
			scanf("%d %d",&n, &index);
			init_ht(&table, 4, dump_int,NULL,
					cmp_int, hash_int, NULL);
			table_test(&table, n, create_data_int);
			printf ("%d\n", table.size);
			dump_list(&table, index);
			free_table(&table);
			break;
		case 2: // test char table
			scanf("%d %d",&n, &index);
			init_ht(&table, 4, dump_char,NULL,
			        cmp_char, hash_char, NULL);
			table_test(&table, n, create_data_char);
			printf ("%d\n", table.size);
			dump_list(&table, index);
			free_table(&table);
			break;
		case 3: // read words from text, insert into table, and print
			scanf("%s", buffer);
			init_ht(&table, 8, dump_word, free_word,
			        cmp_word, hash_word, modify_word);
			stream_to_ht(&table, stdin);
			printf ("%d\n", table.size);
			data = create_data_word(buffer);
			ht_element *e = get_element(&table, data);
			if (e) table.dump_data(e->data);
			if (table.free_data) table.free_data(data);
			free_table(&table);
			break;
		default:
			printf("NOTHING TO DO FOR %d\n", to_do);
			break;
	}
	return 0;
}
