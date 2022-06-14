#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_STR_LEN 64
#define MAX_PERSONS 1024

typedef struct Person {
	int age;
	char first_name[MAX_STR_LEN];
	char last_name[MAX_STR_LEN];
} Person;

// Sort according to age (decreasing)
// When ages equal compare first name and then last name
int cmp_person(const void *p1, const void *p2){
    if (((Person*)p1)->age != ((Person*)p2)->age){
        return (((Person*)p2)->age - ((Person*)p1)->age);
    }
    else if (strcmp(((Person*)p1)->first_name, ((Person*)p2)->first_name)){
        return strcoll(((Person*)p1)->first_name, ((Person*)p2)->first_name);
    }
    return strcoll(((Person*)p1)->last_name, ((Person*)p2)->last_name);
}

// Read data to Person array (till EOF)
int read_person_array(Person *persons){
    char str[MAX_STR_LEN];
    int cnt = 0;
    while(fgets(str, MAX_STR_LEN, stdin) != NULL){
        if (strlen(str) <= 1){continue;}
        sscanf(str,"%d %s %s", &persons[cnt].age, persons[cnt].first_name, persons[cnt].last_name);
        cnt += 1;
    }
    return cnt;
}

// Print Person array
void print_person_array(Person *persons, int n){
    for(int i = 0; i < n; i++){
        printf("%d %s %s\n", persons[i].age, persons[i].first_name, persons[i].last_name);
    }
}

int is_woman(char name [MAX_STR_LEN]){
    return name[strlen(name)-1] == 'a';
}

// Sort women first (woman's first name ends with 'a');
// Then sort women by age and men by last name
// Line consists of: age, first_name, last_name
// (int that order)
int cmp_lines(const void *l1, const void *l2){
    int l1_age;
    char l1_first_name[MAX_STR_LEN];
    char l1_last_name[MAX_STR_LEN];
    int l2_age;
    char l2_first_name[MAX_STR_LEN];
    char l2_last_name[MAX_STR_LEN];
    sscanf(l1,"%d %s %s", &l1_age, l1_first_name, l1_last_name);
    sscanf(l2,"%d %s %s", &l2_age, l2_first_name, l2_last_name);

    if(is_woman(l1_first_name) && !is_woman(l2_first_name)){
        return -1;
    }
    else if(!is_woman(l1_first_name) && is_woman(l2_first_name)){
        return 1;
    }
    else if(is_woman(l1_first_name) && is_woman(l2_first_name)){
        return l1_age - l2_age;
    }
    else if(!is_woman(l1_first_name) && !is_woman(l2_first_name)){
        return strcoll(l1_last_name, l2_last_name);
    }
}

// Read lines with students' data (as text)
int read_lines(char lines[][MAX_STR_LEN]){
    int cnt = 0;
    while(fgets(lines[cnt], MAX_STR_LEN, stdin) != NULL){
        if (strlen(lines[cnt]) <= 1){continue;}
        cnt += 1;
    }
    return cnt;
}

// Print sorted lines
void print_lines(char lines[][MAX_STR_LEN], int n){
    for(int i = 0; i < n; i++){
        printf("%s", lines[i]);
    }
}

// -------------------------------------------------

int read_int() {
	char buf[MAX_STR_LEN];
	int n;
	fgets(buf, MAX_STR_LEN, stdin);
	sscanf(buf, "%d", &n);
	return n;
}

int main(void) {
	int to_do = read_int();
	int n;
	Person persons[MAX_PERSONS];
	char lines[MAX_PERSONS][MAX_STR_LEN];
	switch (to_do) {
		case 1:
			n = read_person_array(persons);
			qsort(persons, (size_t)n, sizeof(Person), cmp_person);
			print_person_array(persons, n);
			break;
		case 2:
			n = read_lines(lines);
			qsort(lines, (size_t) n, MAX_STR_LEN, cmp_lines);
			print_lines(lines, n);
			break;
		default:
			printf("Nothing to do for %d\n", to_do);
			break;
	}
}

