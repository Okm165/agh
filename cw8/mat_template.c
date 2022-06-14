#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>

#define TAB_SIZE  1000
#define BUF_SIZE  1000

double get(int cols, int row, int col, const double *A){
	return A[cols * row + col];
}

void set(int cols, int row, int col, double *A, double value){
	A[cols * row + col] = value;
}

void prod_mat(int rowsA, int colsA, int colsB, double *A, double *B, double *AB){
	for(int i = 0; i < rowsA; i++){
		for(int j = 0; j < colsB; j++){
			double sum = 0;
			for(int k = 0; k < colsA; k++){
				sum += get(colsA, i, k, A) * get(colsB, k, j, B);
			}
			set(colsB, i, j, AB, sum);
		}
	}
}

void read_mat(int rows, int cols, double *t){
	for(int i = 0; i < rows*cols; i++){
		scanf("%lf",&t[i]);
	}
}

void print_mat(int rows, int cols, double *t){
	for(int i = 0; i < rows; i++){
		for(int j = 0; j < cols; j++){
			printf("%.2f ", get(cols, i, j, t));
		}
		printf("\n");
	}
}

int read_char_lines(char *tab[]){
	int lines_counter = 0;
	char str[BUF_SIZE];
	while(fgets(str, BUF_SIZE, stdin) != NULL){
		int len = strlen(str)+1;
		tab[lines_counter] = malloc(sizeof(char)*len);
		memcpy(tab[lines_counter], str, len);
		lines_counter += 1;
	}
	return lines_counter;
}

void write_char_line(char *tab[], int n){
	printf("%s", tab[n]);
}

void delete_lines(char *tab[], int line_count){
	for(int i = 0; i < line_count; i++){
		free(tab[i]);
	}
}

int read_dbl_lines_v1(double *ptr_tab[]){
	char str[BUF_SIZE];
	double val;
	int read;
	int len;
	int cnt;
	int o;
	int lines_counter = 0;
	fgets(str, BUF_SIZE, stdin);
	while(fgets(str, BUF_SIZE, stdin) != NULL){
		len = strlen(str);
		cnt = 0;
		o = 0;
		while(cnt < len){
			sscanf(&str[cnt],"%lf %n",&val,&read);
			cnt += read;
			ptr_tab[lines_counter][o] = val;
			o += 1;
		}
		ptr_tab[lines_counter+1] = &ptr_tab[lines_counter][o];
		lines_counter += 1;
	}
	return lines_counter;
}

void write_dbl_line_v1(double *ptr_tab[], int n){
	int diff = ptr_tab[n] - ptr_tab[n-1];
	for(int i = 0; i < diff; i++){
		printf("%.2f ", ptr_tab[n-1][i]);
	}
}

int main(void) {
	int to_do;

	scanf ("%d", &to_do);

	double A[TAB_SIZE], B[TAB_SIZE], C[TAB_SIZE];
	int n, lines_counter, rowsA,colsA,rowsB,colsB;
	char *char_lines_table[TAB_SIZE];
	double series_table[TAB_SIZE];
	double *ptr_table[TAB_SIZE];

	switch (to_do) {
		case 1:
			scanf("%d %d",&rowsA,&colsA);
			read_mat(rowsA, colsA, A);
			// print_mat(rowsA,colsA,A);//
			scanf("%d %d",&rowsB,&colsB);
			read_mat(rowsB, colsB, B);
			// print_mat(rowsB,colsB,B);//
			prod_mat(rowsA,colsA,colsB,A,B,C);
			print_mat(rowsA,colsB,C);
			break;
		case 2:
			scanf("%d",&n);
			ptr_table[0] = series_table;
			lines_counter = read_dbl_lines_v1(ptr_table);
			write_dbl_line_v1(ptr_table,n);
			break;
		case 3:
			scanf("%d", &n);
			lines_counter = read_char_lines(char_lines_table);
			write_char_line(char_lines_table,n);
			delete_lines(char_lines_table,lines_counter);
			break;
		default:
			printf("NOTHING TO DO FOR %d\n", to_do);
	}
	return 0;
}
