#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define BUFFER_SIZE 1024
#define MEMORY_ALLOCATION_ERROR -1
#define LIST_ERROR -2
#define PROGRAM_ERROR -3

struct tagList;
typedef void (*ConstDataFp)(const void *);
typedef void (*DataFp)(void *);
typedef int (*CompareDataFp)(const void *, const void *);
typedef void (*InsertInOrder)(struct tagList *, void *);

typedef struct tagListElement
{
	struct tagListElement *next;
	void *data;
} ListElement;

typedef struct tagList
{
	ListElement *head;
	ListElement *tail;
	ConstDataFp dump_data;
	DataFp free_data;
	CompareDataFp compare_data;
	InsertInOrder insert_sorted;
} List;

// -----------------------------------------------------------------
// generic functions - they are common for all instances of the list
// (independent of the data type)
// -----------------------------------------------------------------

void init_list(List *p_list, ConstDataFp dump_data, DataFp free_data,
			   CompareDataFp compare_data, InsertInOrder insert_sorted)
{
	p_list->head = NULL;
	p_list->tail = NULL;
	p_list->dump_data = dump_data;
	p_list->free_data = free_data;
	p_list->compare_data = compare_data;
	p_list->insert_sorted = insert_sorted;
}

// Print all elements of the list
void dump_list(const List *p_list)
{
	ListElement *curr = p_list->head;
	while (curr != NULL)
	{
		p_list->dump_data(curr->data);
		curr = curr->next;
	}
	printf("\n");
	return;
}

// Print elements of the list if comparable to data
void dump_list_if(List *p_list, void *data)
{
	ListElement *curr = p_list->head;
	while (curr != NULL)
	{
		if (p_list->compare_data(curr->data, data) == 0)
			p_list->dump_data(curr->data);
		curr = curr->next;
	}
	return;
}

// Free all elements of the list
void free_list(List *p_list)
{
	ListElement *curr = p_list->head;
	while (curr != NULL)
	{
		ListElement *togo = curr->next;
		p_list->free_data(curr);
		curr = togo;
	}
	p_list->head = NULL;
	p_list->tail = NULL;
	return;
}

// Push element at the beginning of the list
void push_front(List *p_list, void *data)
{
	ListElement *element = malloc(sizeof(ListElement));
	if (element == NULL)
		exit(MEMORY_ALLOCATION_ERROR);
	element->data = data;
	if (p_list->head)
	{
		element->next = p_list->head;
		p_list->head = element;
	}
	else
	{
		p_list->head = element;
		element->next = NULL;
		p_list->tail = p_list->head;
	}
	return;
}

// Push element at the end of the list
void push_back(List *p_list, void *data)
{
	ListElement *element = malloc(sizeof(ListElement));
	if (element == NULL)
		exit(MEMORY_ALLOCATION_ERROR);
	element->data = data;
	element->next = NULL;
	if (p_list->tail)
		p_list->tail->next = element;
	p_list->tail = element;
	if (!p_list->head)
		p_list->head = p_list->tail;
	return;
}

// Remove the first element
void pop_front(List *p_list)
{
	ListElement *element = p_list->head;
	p_list->head = p_list->head->next;
	p_list->free_data(element->data);
	if (p_list->head == NULL)
		p_list->tail = NULL;
	return;
}

// Reverse the list
void reverse(List *p_list)
{
	ListElement *prev = p_list->head;
	ListElement *curr = prev->next;
	if (curr == NULL || prev == NULL)
		return;
	prev->next = NULL;
	while (curr != NULL)
	{
		ListElement *togo = curr->next;
		curr->next = prev;
		prev = curr;
		curr = togo;
	}
	ListElement *togo = p_list->head;
	p_list->head = p_list->tail;
	p_list->tail = togo;
	return;
}

// insert element preserving the ordering (defined by insert_sorted function)
void insert_in_order(List *p_list, void *data)
{
	p_list->insert_sorted(p_list, data);
}

// find element in sorted list after which to insert given element
ListElement *find_insertion_point(const List *p_list, ListElement *p_element)
{
	ListElement *curr = p_list->head;
	if (curr == NULL)
		return NULL;
	if (p_list->compare_data(curr->data, p_element->data) > 0)
	{
		return NULL;
	}
	if (curr->next == NULL && p_list->compare_data(curr->data, p_element->data) <= 0)
	{
		return curr;
	}
	while (curr->next != NULL)
	{
		if (p_list->compare_data(curr->next->data, p_element->data) >= 0)
		{
			return curr;
		}
		curr = curr->next;
	}
	return curr;
}

// Insert element after 'previous'
void push_after(List *p_list, void *data, ListElement *previous)
{
	ListElement *element = malloc(sizeof(ListElement));
	if (element == NULL)
		exit(MEMORY_ALLOCATION_ERROR);
	element->data = data;
	if (p_list->head == NULL)
	{
		element->next = p_list->head;
		p_list->head = element;
		p_list->tail = p_list->head;
	}
	else
	{
		if (previous == NULL)
		{
			element->next = p_list->head;
			p_list->head = element;
		}
		else
		{
			if (previous == p_list->tail)
			{
				element->next = previous->next;
				previous->next = element;
				p_list->tail = element;
			}
			else
			{
				element->next = previous->next;
				previous->next = element;
			}
		}
	}
	return;
}

// Insert element preserving order (no counter)
void insert_elem(List *p_list, void *p_data)
{
	ListElement *element = malloc(sizeof(ListElement));
	if (element == NULL)
		exit(MEMORY_ALLOCATION_ERROR);
	element->data = p_data;
	element->next = NULL;
	ListElement *insert_after = find_insertion_point(p_list, element);
	push_after(p_list, p_data, insert_after);
	return;
}

// ---------------------------------------------------------------
// type-specific definitions
// ---------------------------------------------------------------

// int element

typedef struct DataInt
{
	int id;
} DataInt;

void dump_int(const void *d)
{
	printf("%d ", ((DataInt *)d)->id);
	return;
}

void free_int(void *d)
{
	free((DataInt *)d);
	return;
}

int cmp_int(const void *a, const void *b)
{
	return ((DataInt *)a)->id - ((DataInt *)b)->id;
}

DataInt *create_data_int(int v)
{
	DataInt *element = malloc(sizeof(DataInt));
	if (element == NULL)
		exit(MEMORY_ALLOCATION_ERROR);
	element->id = v;
	return element;
}

// Word element

typedef struct DataWord
{
	char *word;
	int counter;
} DataWord;

void dump_word(const void *d)
{
	printf("%s\n", ((DataWord *)d)->word);
	return;
}

void dump_word_lowercase(const void *d)
{
	char *original = ((DataWord *)d)->word;
	int length = strlen(original);

	for (int i = 0; i < length; i++)
	{
		original[i] = tolower(original[i]);
	}
	printf("%s\n", original);
	return;
}

void free_word(void *d)
{
	free((DataWord *)d);
	return;
}

// conpare words case insensitive
int cmp_word_alphabet(const void *a, const void *b)
{
	return strcmp(((DataWord *)a)->word, ((DataWord *)b)->word);
}

int cmp_word_counter(const void *a, const void *b)
{
	return ((DataWord *)a)->counter - ((DataWord *)b)->counter;
}

// insert element; if present increase counter
void insert_elem_counter(List *p_list, void *data)
{
	ListElement *curr = p_list->head;
	if (curr == NULL)
	{
		push_after(p_list, data, NULL);
		return;
	}
	if (p_list->compare_data(curr->data, data) > 0)
	{
		push_after(p_list, data, NULL);
		return;
	}
	if (curr->next == NULL)
	{
		if (p_list->compare_data(curr->data, data) < 0)
		{
			push_after(p_list, data, curr);
			return;
		}
		else
		{
			((DataWord *)(curr->data))->counter += 1;
			return;
		}
	}
	else
	{
		while (curr->next != NULL)
		{
			if (p_list->compare_data(curr->data, data) == 0)
			{
				((DataWord *)(curr->data))->counter += 1;
				return;
			}
			if (p_list->compare_data(curr->next->data, data) > 0)
			{
				push_after(p_list, data, curr);
				return;
			}

			curr = curr->next;
		}
		if (p_list->compare_data(curr->data, data) == 0)
		{
			((DataWord *)(curr->data))->counter += 1;
			return;
		}
		push_after(p_list, data, curr);
	}
	return;
}

// read text, parse it to words, and insert those words to the list
// in order given by the last parameter (0 - read order,
// 1 - alphabetical order)
void stream_to_list(List *p_list, FILE *stream, int order)
{
	char buffer[BUFFER_SIZE];
	const char s[11] = " .,?!:;-\n	";
	char *token;

	while (fgets(buffer, BUFFER_SIZE, stream) != NULL)
	{
		token = strtok(buffer, s);

		while (token != NULL)
		{
			if (strlen(token) == 0)
				continue;
			DataWord *element = malloc(sizeof(DataWord));
			if (element == NULL)
				exit(MEMORY_ALLOCATION_ERROR);

			char *str = strdup(token);

			element->word = str;
			element->counter = 1;

			if (!order)
			{
				push_back(p_list, element);
			}
			else
			{
				int length = strlen(element->word);
				for (int i = 0; i < length; i++)
				{
					element->word[i] = tolower(element->word[i]);
				}
				insert_in_order(p_list, element);
			}

			token = strtok(NULL, s);
		}
		memset(buffer, 0, BUFFER_SIZE);
	}
	return;
}

// test integer list
void list_test(List *p_list, int n)
{
	char op[2];
	int v;
	for (int i = 0; i < n; ++i)
	{
		scanf("%s", op);
		switch (op[0])
		{
		case 'f':
			scanf("%d", &v);
			push_front(p_list, create_data_int(v));
			break;
		case 'b':
			scanf("%d", &v);
			push_back(p_list, create_data_int(v));
			break;
		case 'd':
			pop_front(p_list);
			break;
		case 'r':
			reverse(p_list);
			break;
		case 'i':
			scanf("%d", &v);
			insert_in_order(p_list, create_data_int(v));
			break;
		default:
			printf("No such operation: %s\n", op);
			break;
		}
	}
}

int main(void)
{
	int to_do, n;
	List list;

	scanf("%d", &to_do);
	switch (to_do)
	{
	case 1: // test integer list
		scanf("%d", &n);
		init_list(&list, dump_int, free_int,
				  cmp_int, insert_elem);
		list_test(&list, n);
		dump_list(&list);
		free_list(&list);
		break;
	case 2: // read words from text, insert into list, and print
		init_list(&list, dump_word, free_word,
				  cmp_word_alphabet, insert_elem_counter);
		stream_to_list(&list, stdin, 0);
		dump_list(&list);
		free_list(&list);
		break;
	case 3: // read words, insert into list alphabetically, print words encountered n times
		scanf("%d", &n);
		init_list(&list, dump_word_lowercase, free_word,
				  cmp_word_alphabet, insert_elem_counter);
		stream_to_list(&list, stdin, 1);
		list.compare_data = cmp_word_counter;
		DataWord data = {NULL, n};
		// list.dump_data = dump_word_lowercase;
		dump_list_if(&list, &data);
		// dump_list(&list);
		printf("\n");
		free_list(&list);
		break;
	default:
		printf("NOTHING TO DO FOR %d\n", to_do);
		break;
	}
	return 0;
}
