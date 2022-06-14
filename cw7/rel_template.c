#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_REL_SIZE 1000
#define MAX_RANGE 1000

typedef struct {
	int first;
	int second;
} pair;

int cmp (pair p1, pair p2);
void print_rel(pair *pair_ptr, int size);
void print_map(int map_ptr[MAX_RANGE][MAX_RANGE], int x, int y);

// Add pair to existing relation if not already there
int add_relation (pair* pair_ptr, int size, pair p) {
	for (int i = 0; i < size; i++) {
		if (cmp(pair_ptr[i], p) == 0) {
			return size;
		}
	}
	pair_ptr[size] = p;
	return size+1;
}

// Case 1:
// The relation R is reflexive if xRx for every x in X
int is_reflexive(pair* pair_ptr, int size) {
	int map[MAX_RANGE][MAX_RANGE];
	for (int i = 0; i < MAX_RANGE; i++) {
		for (int j = 0; j < MAX_RANGE; j++) {
			map[i][j] = 0;
		}
	}

	for (int i = 0; i < size; i++) {
		map[pair_ptr[i].first][pair_ptr[i].second] = 1;
	}

	for (int i = 0; i < size; i++) {
		if (map[pair_ptr[i].first][pair_ptr[i].first] != 1 ||
		map[pair_ptr[i].second][pair_ptr[i].second] != 1){
			return 0;
		}
	}
	return 1;
}
// The relation R on the set X is called irreflexive
// if xRx is false for every x in X
int is_irreflexive(pair* pair_ptr, int size) {
	int map[MAX_RANGE][MAX_RANGE];
	for (int i = 0; i < MAX_RANGE; i++) {
		for (int j = 0; j < MAX_RANGE; j++) {
			map[i][j] = 0;
		}
	}

	for (int i = 0; i < size; i++) {
		map[pair_ptr[i].first][pair_ptr[i].second] = 1;
	}
	for (int i = 0; i < size; i++) {
		if (map[pair_ptr[i].first][pair_ptr[i].first] == 1 ||
		map[pair_ptr[i].second][pair_ptr[i].second] == 1) {
			return 0;
		}
	}
	
	return 1;
}
// A binary relation R over a set X is symmetric if:
// for all x, y in X xRy <=> yRx
int is_symmetric(pair* pair_ptr, int size) {
	int map[MAX_RANGE][MAX_RANGE];
	for (int i = 0; i < MAX_RANGE; i++) {
		for (int j = 0; j < MAX_RANGE; j++) {
			map[i][j] = 0;
		}
	}

	int x[MAX_RANGE];
	for (int i = 0; i < MAX_RANGE; i++) {
		x[i] = 0;
	}

	for (int i = 0; i < size; i++) {
		map[pair_ptr[i].first][pair_ptr[i].second] = 1;
		x[pair_ptr[i].first] = 1;
		x[pair_ptr[i].second] = 1;
	}

	int red_x[MAX_RANGE];
	int cnt = 0;
	for (int i = 0; i < MAX_RANGE; i++) {
		if (x[i] != 0) {
			red_x[cnt] = i;
			cnt += 1;
		}
	}

	for (int i = 0; i < cnt; i++) {
		for (int j = 0; j < cnt; j++) {
			if ((map[red_x[i]][red_x[j]] == 1 && map[red_x[j]][red_x[i]] == 0) || (map[red_x[j]][red_x[i]] == 1 && map[red_x[i]][red_x[j]] == 0)) {
				return 0;
			}
		}
	}
	return 1;
}
// A binary relation R over a set X is antisymmetric if:
// for all x,y in X if xRy and yRx then x=y
int is_antisymmetric(pair* pair_ptr, int size) {
	int map[MAX_RANGE][MAX_RANGE];
	for (int i = 0; i < MAX_RANGE; i++) {
		for (int j = 0; j < MAX_RANGE; j++) {
			map[i][j] = 0;
		}
	}

	for (int i = 0; i < size; i++) {
		map[pair_ptr[i].first][pair_ptr[i].second] = 1;
	}

	for (int i = 0; i < size; i++) {
		if (map[pair_ptr[i].second][pair_ptr[i].first] == 1 &&
		pair_ptr[i].second != pair_ptr[i].first) {
			return 0;
		}
	}
	return 1;
}
// A binary relation R over a set X is asymmetric if:
// for all x,y in X if at least one of xRy and yRx is false
int is_asymmetric(pair* pair_ptr, int size) {
	int map[MAX_RANGE][MAX_RANGE];
	for (int i = 0; i < MAX_RANGE; i++) {
		for (int j = 0; j < MAX_RANGE; j++) {
			map[i][j] = 0;
		}
	}

	int x[MAX_RANGE];
	for (int i = 0; i < MAX_RANGE; i++) {
		x[i] = 0;
	}

	for (int i = 0; i < size; i++) {
		map[pair_ptr[i].first][pair_ptr[i].second] = 1;
		x[pair_ptr[i].first] = 1;
		x[pair_ptr[i].second] = 1;
	}

	int red_x[MAX_RANGE];
	int cnt = 0;
	for (int i = 0; i < MAX_RANGE; i++) {
		if (x[i] != 0) {
			red_x[cnt] = i;
			cnt += 1;
		}
	}

	for (int i = 0; i < cnt; i++) {
		for (int j = 0; j < cnt; j++) {
			if (map[red_x[i]][red_x[j]] == 1 && map[red_x[j]][red_x[i]] == 1) {
				return 0;
			}
		}
	}
	return 1;
}
// A homogeneous relation R on the set X is a transitive relation if:
// for all x, y, z in X, if xRy and yRz, then xRz
int is_transitive(pair* pair_ptr, int size) {
	int map[MAX_RANGE][MAX_RANGE];
	for (int i = 0; i < MAX_RANGE; i++) {
		for (int j = 0; j < MAX_RANGE; j++) {
			map[i][j] = 0;
		}
	}

	int x[MAX_RANGE];
	for (int i = 0; i < MAX_RANGE; i++) {
		x[i] = 0;
	}

	for (int i = 0; i < size; i++) {
		map[pair_ptr[i].first][pair_ptr[i].second] = 1;
		x[pair_ptr[i].first] = 1;
		x[pair_ptr[i].second] = 1;
	}

	int red_x[MAX_RANGE];
	int cnt = 0;
	for (int i = 0; i < MAX_RANGE; i++) {
		if (x[i] != 0) {
			red_x[cnt] = i;
			cnt += 1;
		}
	}

	for (int i = 0; i < cnt; i++) {
		for (int j = 0; j < cnt; j++) {
			for (int k = 0; k < cnt; k++) {
				if (map[red_x[i]][red_x[j]] == 1 && map[red_x[j]][red_x[k]] == 1 && map[red_x[i]][red_x[k]] == 0) {
					return 0;
				}
			}
		}
	}
	return 1;
}

// Case 2:
// Relation R is connected if for each x, y in X:
// xRy or yRx (or both)
int is_connected(pair* pair_ptr, int size) {
	int map[MAX_RANGE][MAX_RANGE];
	for (int i = 0; i < MAX_RANGE; i++) {
		for (int j = 0; j < MAX_RANGE; j++) {
			map[i][j] = 0;
		}
	}

	int x[MAX_RANGE];
	for (int i = 0; i < MAX_RANGE; i++) {
		x[i] = 0;
	}

	for (int i = 0; i < size; i++) {
		map[pair_ptr[i].first][pair_ptr[i].second] = 1;
		x[pair_ptr[i].first] = 1;
		x[pair_ptr[i].second] = 1;
	}

	int red_x[MAX_RANGE];
	int cnt = 0;
	for (int i = 0; i < MAX_RANGE; i++) {
		if (x[i] != 0) {
			red_x[cnt] = i;
			cnt += 1;
		}
	}

	for (int i = 0; i < cnt; i++) {
		for (int j = 0; j < cnt; j++) {
			if (map[red_x[i]][red_x[j]] == 0 && map [red_x[j]][red_x[i]] == 0) {
				return 0;
			}
		}
	}
	return 1;
}
// A partial order relation is a homogeneous relation that is
// reflexive, transitive, and antisymmetric
int is_partial_order(pair* pair_ptr, int size) {
	if (is_reflexive(pair_ptr, size) && is_transitive(pair_ptr, size) && is_antisymmetric(pair_ptr, size)) {
		return 1;
	}
	return 0;
}
// A total order relation is a partial order relation that is connected
int is_total_order(pair* pair_ptr, int  size) {
	if (is_partial_order(pair_ptr, size) && is_connected(pair_ptr, size)) {
		return 1;
	}
	return 0;
}

int find_max_elements(pair* pair_ptr, int size, int* arr) {
	int arr_ptr = 0;
	int tab[MAX_RANGE];
	int max_elements[MAX_RANGE];
	for (int i = 0; i < MAX_RANGE; i++) {
		tab[i] = -1;
		max_elements[i] = 0;
	}

	for (int i = 0; i < size; i++) {
		if (pair_ptr[i].second != pair_ptr[i].first) {
			tab[pair_ptr[i].first] = pair_ptr[i].second;
		}
	}

	for (int i = 0; i < size; i++) {
		if (tab[pair_ptr[i].second] == -1) {
			max_elements[pair_ptr[i].second] = 1;
		}
	}

	for (int i = 0; i < MAX_RANGE; i++) {
		if (max_elements[i] == 1) {
			arr[arr_ptr] = i;
			arr_ptr += 1;
		}
	}

	return arr_ptr;
}
int find_min_elements(pair* pair_ptr, int size, int* arr) {
	int arr_ptr = 0;
	int tab[MAX_RANGE];
	int min_elements[MAX_RANGE];
	for (int i = 0; i < MAX_RANGE; i++) {
		tab[i] = -1;
		min_elements[i] = 0;
	}

	for (int i = 0; i < size; i++) {
		if (pair_ptr[i].second != pair_ptr[i].first) {
			tab[pair_ptr[i].second] = pair_ptr[i].first;
		}
	}

	for (int i = 0; i < size; i++) {
		if (tab[pair_ptr[i].first] == -1) {
			min_elements[pair_ptr[i].first] = 1;
		}
	}

	for (int i = 0; i < MAX_RANGE; i++) {
		if (min_elements[i] == 1) {
			arr[arr_ptr] = i;
			arr_ptr += 1;
		}
	}

	return arr_ptr;
}
int get_domain(pair* pair_ptr, int size, int* arr) {
	int x[MAX_RANGE];
	for (int i = 0; i < MAX_RANGE; i++) {
		x[i] = 0;
	}

	for (int i = 0; i < size; i++) {
		x[pair_ptr[i].first] = 1;
		x[pair_ptr[i].second] = 1;
	}

	int cnt = 0;
	for (int i = 0; i < MAX_RANGE; i++) {
		if (x[i] != 0) {
			arr[cnt] = i;
			cnt += 1;
		}
	}
	return cnt;
}

// Case 3:
int composition (pair* pair1_ptr, int size1, pair* pair2_ptr, int size2, pair* res_ptr) {
	// int map1_ptr[MAX_RANGE];
	// int map1[MAX_RANGE][MAX_REL_SIZE];
	int map2_ptr[MAX_RANGE];
	int map2[MAX_RANGE][MAX_REL_SIZE];
	for (int i = 0; i < MAX_RANGE; i++) {
		for (int j = 0; j < MAX_RANGE; j++) {
			// map1[i][j] = 0;
			map2[i][j] = 0;
		}
		// map1_ptr[i] = 0;
		map2_ptr[i] = 0;
	}

	for (int i = 0; i < size2; i++) {
		map2[pair2_ptr[i].first][map2_ptr[pair2_ptr[i].first]] = pair2_ptr[i].second;
		map2_ptr[pair2_ptr[i].first] += 1;
	}
	// printf("\n");
	// for (int i = 0; i < size2; i++) {
	// 	// printf("%d ", map2_ptr[i]);
	// 	for (int j = 0; j <  map2_ptr[pair2_ptr[i].first]; j++) {
			
	// 		printf("%d ", map2[pair2_ptr[i].first][j]);
	// 	}
	// 	printf("\n");
	// }
	int res_cnt = 0;
	for (int i = 0; i < size1; i++) {
		for (int j = 0; j < map2_ptr[pair1_ptr[i].second]; j++) {
			pair newpair;
			newpair.first = pair1_ptr[i].first;
			newpair.second = map2[pair1_ptr[i].second][j];
			// res_ptr[res_cnt] = newpair;
			res_cnt = add_relation(res_ptr, res_cnt, newpair);
			// printf("%d %d \n", newpair.first, newpair.second);
		}
	}
	// print_rel(res_ptr, res_cnt);
	return res_cnt;
}

int cmp (pair p1, pair p2) {
	if (p1.first == p2.first) return p1.second - p2.second;
	return p1.first - p2.first;
}

// Read number of pairs, n, and then n pairs of ints
int read_relation(pair* pair_ptr){
	int size;
	scanf("%d", &size);
	for (int i = 0; i < size; i++){
		pair newpair;
		scanf("%d", &newpair.first);
		scanf("%d", &newpair.second);
		add_relation(pair_ptr, i, newpair);
	}
	return size;
}

void print_int_array(int *array, int n) {
	printf("%d\n", n);
	for (int i = 0; i < n; ++i) {
		printf("%d ", array[i]);
	}
	printf("\n");
}

void print_map(int map_ptr[MAX_RANGE][MAX_RANGE], int x, int y) {
	for (int i = 0; i < x; i++) {
		for (int j = 0; j < y; j++) {
			printf("%d ", map_ptr[i][j]);
		}
		printf("\n");
	}
}

void print_rel(pair *pair_ptr, int size) {
	printf("%d\n", size);
	for (int i = 0; i < size; i++) {
		printf("%d %d \n", pair_ptr[i].first, pair_ptr[i].second);
	}
	printf("\n");
}

int main(void) {
	int to_do;
	pair relation[MAX_REL_SIZE];
	pair relation_2[MAX_REL_SIZE];
	pair comp_relation[MAX_REL_SIZE];
	int domain[MAX_REL_SIZE];

	scanf("%d",&to_do);
	int size = read_relation(relation);
	int ordered, size_2, n_domain;

	switch (to_do) {
		case 1:
			printf("%d ", is_reflexive(relation, size));
			printf("%d ", is_irreflexive(relation, size));
			printf("%d ", is_symmetric(relation, size));
			printf("%d ", is_antisymmetric(relation, size));
			printf("%d ", is_asymmetric(relation, size));
			printf("%d\n", is_transitive(relation, size));
			break;
		case 2:
			ordered = is_partial_order(relation, size);
			n_domain = get_domain(relation, size, domain);
			printf("%d %d\n", ordered, is_total_order(relation, size));
			print_int_array(domain, n_domain);
			if (!ordered) break;
			int max_elements[MAX_REL_SIZE];
			int min_elements[MAX_REL_SIZE];
			int no_max_elements = find_max_elements(relation, size, max_elements);
			int no_min_elements = find_min_elements(relation, size, min_elements);
			print_int_array(max_elements, no_max_elements);
			print_int_array(min_elements, no_min_elements);
			break;
		case 3:
			size_2 = read_relation(relation_2);
			printf("%d\n", composition(relation, size,
			   relation_2, size_2, comp_relation));  
			break;
		default:
			printf("NOTHING TO DO FOR %d\n", to_do);
			break;
	}
	return 0;
}

