#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 1000
#define MEMORY_ALLOCATION_ERROR  -1

// list node
typedef struct Node {
	int *data;
	int array_size;
	struct Node* next;
	struct Node* prev;
} Node;

// doubly linked list
typedef struct List {
	Node *head;
	Node *tail;
	int size;
} List;

// iterator
typedef struct iterator {
	int position;
	struct Node* node_ptr;
} iterator;

// forward initialization
iterator begin(Node* head) {
	iterator it = {0, head};
	return it;
}

// backward initialization
iterator end(Node* tail) {
	iterator it = {tail->array_size - 1, tail};
	return it;
}

// initialize list
void init(List *list) {
	list->head = NULL;
	list->tail = NULL;
	list->size = 0;
}

// ---------------------------------------------- to implement ...

// append element to the list
void push_back(List *list, int *data, int array_size) {
	Node *new_node = malloc(sizeof(Node));
	new_node->data = data;
	new_node->array_size = array_size;

	if (list->head == NULL || list->tail == NULL || list->size == 0) { // if list is empty
		list->head = new_node;
		list->tail = new_node;
	} else { // list is not empty
		new_node->prev = list->tail;
		list->tail->next = new_node;
		list->tail = new_node;
	}
	list->size += 1;
	return;
}

// set iterator to move n elements forward from its current position
void skip_forward(iterator* itr, int n) {
	n -= 1;
	while (n > itr->node_ptr->array_size-1) {
		n -= itr->node_ptr->array_size - itr->position;
		itr->node_ptr = itr->node_ptr->next;
	}
	itr->position = n;
	return;
}

// forward iteration - get n-th element in the list
int get_forward(List *list, int n) {
	iterator it = begin(list->head);
	skip_forward(&it, n);
	return it.node_ptr->data[it.position];
}

// set iterator to move n elements backward from its current position
void skip_backward(iterator* itr, int n) {
	n -= 1;
	while (n > itr->position) {
		n -= itr->position+1;
		itr->node_ptr = itr->node_ptr->prev;
		itr->position = itr->node_ptr->array_size-1;
	}
	itr->position -= n;
	return;
}

// backward iteration - get n-th element from the end of the list
int get_backward(List *list, int n) {
	iterator it = end(list->tail);
	skip_backward(&it, n);
	return it.node_ptr->data[it.position];
}

// remove n-th element; if array empty remove node
void remove_at(List *list, int n) {
	iterator it = begin(list->head);
	skip_forward(&it, n);
	if (it.node_ptr->array_size == 1) {
		free(it.node_ptr->data);

		if (!it.node_ptr->prev && !it.node_ptr->next) {
			list->head = NULL;
			list->tail = NULL;
			list->size = 0;
		} else if (!it.node_ptr->prev) {
			list->head = it.node_ptr->next;
			list->head->prev = NULL;
			list->size -= 1;

		} else if (!it.node_ptr->next) {
			list->tail = it.node_ptr->prev;
			list->tail->next = NULL;
			list->size -= 1;
		} else {
			it.node_ptr->prev->next = it.node_ptr->next;
			it.node_ptr->next->prev = it.node_ptr->prev;
			list->size -= 1;
		}

		free(it.node_ptr);
	} else {
		int* new_data = malloc((it.node_ptr->array_size-1)*sizeof(int));
		memcpy(new_data, it.node_ptr->data, it.position*sizeof(int));
		memcpy(&(new_data[it.position]), &(it.node_ptr->data[it.position+1]), (it.node_ptr->array_size-1-it.position)*sizeof(int));
		free(it.node_ptr->data);
		it.node_ptr->data = new_data;
		it.node_ptr->array_size -= 1;
	}
	return;
}

// -------------------- helper functions

// print list
void dumpList(const List *list) {
	for(Node *node = list->head; node != NULL; node = node->next) {
		printf("-> ");
		for (int k = 0; k < node->array_size; k++) {
			printf("%d ", node->data[k]);
		}
		printf("\n");
	}
}

// remove the first element
void delete_front(List *list) {
	Node *to_delete;
	if(list->head == NULL) return;
	to_delete = list->head;
	list->head = list->head->next;
	if(list->head == NULL) list->tail = NULL;
	free(to_delete->data);
	free(to_delete);
	list->size--;
}

// free list
void freeList(List *list) {
	while(list->head) {
		delete_front(list);
	}
}

// read int vector
void read_vector(int tab[], int n) {
	for (int i = 0; i < n; ++i) {
		scanf("%d", tab + i);
	}
}

// initialize the list and push data
void read_list(List *list) {
	int size, n;
	init(list);
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &size);
		int *tab = (int*) malloc((size_t)size * sizeof(int));
		read_vector(tab, size);
		push_back(list, tab, size);
	}
}

int main() {
	int to_do, size, m;
	List list;

	scanf("%d", &to_do);
	read_list(&list);
	switch (to_do) {
	case 1:
		dumpList(&list);
		break;
	case 2:
		scanf("%d", &size);
		for (int i = 0; i < size; i++) {
			scanf("%d", &m);
			printf("%d ", get_forward(&list, m));
		}
		printf("\n");
		break;
	case 3:
		scanf("%d", &size);
		for (int i = 0; i < size; i++) {
			scanf("%d", &m);
			printf("%d ", get_backward(&list, m));
		}
		printf("\n");
		break;
	case 4:
		scanf("%d", &size);
		for (int i=0; i < size; i++) {
			scanf("%d", &m);
			remove_at(&list, m);
		}
		dumpList(&list);
		break;
	default:
		printf("NOTHING TO DO FOR %d\n", to_do);
		break;
	}
	freeList(&list);

	return 0;
}
