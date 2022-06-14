#include <stdio.h>
#include <math.h>

#define SIZE 40

void read_vector(double x[], int n) {
	for(int i = 0; i < n; ++i) {
		scanf("%lf", x++);
	}
}

void print_vector(double x[], int n) {
	for(int i = 0; i < n; ++i) {
		printf("%.4f ", x[i]);
	}
	printf("\n");
}

void read_mat(double A[][SIZE], int m, int n) {
	for(int i = 0; i < m; ++i) {
		for(int j = 0; j < n; ++j) {
			scanf("%lf", &A[i][j]);
		}
	}
}

void print_mat(double A[][SIZE], int m, int n) {
	for(int i = 0; i < m; ++i) {
		for(int j = 0; j < n; ++j) {
			printf("%.4f ", A[i][j]);
		}
		printf("\n");
	}
}

// void print_mat_ind(double A[][SIZE], int m, int n, const int indices[]);

// 5.1
// Calculate matrix product, AB = A X B
// A[m][p], B[p][n]
void mat_product(double A[][SIZE], double B[][SIZE], double AB[][SIZE], int m, int p, int n){
	double sum;
	for (int i = 0; i < m; i++) {
		for (int k = 0; k < n; k++) {
			sum = 0;
			for (int j = 0; j < p; j++) {
				sum += A[i][j] * B[j][k];
			}
			AB[i][k] = sum;
		}
	}
}

// Calculate matrix - vector product
// void mat_vec_product(double A[][SIZE], const double b[], double Ab[], int m, int n);

// void backward_substit(double A[][SIZE], double x[], int n);

// void backward_substitution_index(double A[][SIZE], const int indices[], double x[], int n);

// 5.2
// Matrix triangulation and determinant calculation - simplified version
// (no rows' swaps). If A[i][i] == 0, function returns NAN.
// Function may change A matrix elements.
double gauss_simplified(double A[][SIZE], int n){
	double x;
	double det = 1;
	for (int i = 0; i < n-1; i++) {
		if (A[i][i] == 0) {
			return NAN;
		}
		for (int j = i+1; j < n; j++) {
			x = A[j][i] / A[i][i];
			for (int k = i; k < n; k++) {
				A[j][k] = A[j][k]-A[i][k]*x;
			}
		}
	}
	for (int d = 0; d < n; d++) {
		det *= A[d][d];
	}
	return det;
}

// 5.3
// Matrix triangulation, determinant calculation, and Ax = b solving - extended version
// (Swap the rows so that the row with the largest, leftmost nonzero entry is on top. While
// swapping the rows use index vector - do not copy entire rows.)
// If max A[i][i] < eps, function returns 0.
// If det != 0 && b != NULL && x != NULL then vector x should contain solution of Ax = b.

void swap(int iv[], const int a, const int b) {
	int tmp = iv[a];
	iv[a] = iv[b];
	iv[b] = tmp;
}

double gauss(double A[][SIZE], const double b[], double x[], const int n, const double eps) {
	double max;
	int max_ind;
	double p;
	double det = 1;
	int idx = 1;
	int Aiv[n];
	int Biv[n];
	for (int i = 0; i < n; i++) {
		Aiv[i] = i;
		Biv[i] = i;
	}

	double Z[n];
	for (int i = 0; i < n; i++) {
		Z[i] = b[i];
	}
	
	for (int i = 0; i < n-1; i++) {
		max = fabs(A[Aiv[i]][i]);
		max_ind = i;
		for (int m = i; m < n; m++) {
			if (fabs(A[Aiv[m]][i]) > max) {
				max = fabs(A[Aiv[m]][i]);
				max_ind = m;
			}
		}

		if (i != max_ind) {
			idx *= -1;
		}
		swap(Aiv, i, max_ind);
		swap(Biv, i, max_ind);

		if (fabs(A[Aiv[i]][i]) < eps) {
			det = 0;
			break;
		}
		
		for (int j = i+1; j < n; j++) {
			p = A[Aiv[j]][i] / A[Aiv[i]][i];
			for (int k = i; k < n; k++) {
				A[Aiv[j]][k] = A[Aiv[j]][k]-A[Aiv[i]][k]*p;
			}
			Z[Biv[j]] = Z[Biv[j]]-Z[Biv[i]]*p;
		}
		det *= A[Aiv[i]][i];
	}
	det *= A[Aiv[n-1]][n-1]*idx;

	if( det != 0 && b != NULL && x != NULL ) {
		double rest;
		for (int u = n-1; u >= 0; u--) {
			rest = Z[Biv[u]];
			for( int y = u+1; y < n; y++) {
				rest -= x[y]*A[Aiv[u]][y];
			}
			x[u] = rest / A[Aiv[u]][u];
		}
	}
	return det;
}

// 5.4
// Returns the determinant; B contains the inverse of A (if det(A) != 0)
// If max A[i][i] < eps, function returns 0.
double matrix_inv(double A[][SIZE], double B[][SIZE], int n, double eps) {
	int Aiv[n];
	int Biv[n];
	double max;
	int max_ind;
	int idx = 1;
	double p;
	double det = 1;

	for (int i = 0; i < n; i++) {
		Aiv[i] = i;
		Biv[i] = i;
	}

	// init B table
	double tB [SIZE][SIZE];
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (i == j) {
				tB[i][j] = 1;
			}
			else {
				tB[i][j] = 0;
			}
		}
	}
	
	for (int i = 0; i < n-1; i++) {
		max = fabs(A[Aiv[i]][i]);
		max_ind = i;
		for (int m = i; m < n; m++) {
			if (fabs(A[Aiv[m]][i]) > max) {
				max = fabs(A[Aiv[m]][i]);
				max_ind = m;
			}
		}

		if (i != max_ind) {
			idx *= -1;
		}
		swap(Aiv, i, max_ind);
		swap(Biv, i, max_ind);

		if (fabs(A[Aiv[i]][i]) < eps) {
			det = 0;
			break;
		}

		for (int j = i+1; j < n; j++) {
			p = A[Aiv[j]][i] / A[Aiv[i]][i];
			for (int k = i; k < n; k++) {
				A[Aiv[j]][k] = A[Aiv[j]][k]-A[Aiv[i]][k]*p;
			}
			for (int k = 0; k < n; k++) {
				tB[Biv[j]][k] = tB[Biv[j]][k]-tB[Biv[i]][k]*p;
			}
		}

		det *= A[Aiv[i]][i];
	}
	det *= A[Aiv[n-1]][n-1]*idx;

	if (fabs(det) < eps)
	{
		det = 0;
	}

	if (det != 0){
		// normalize
		double val;
		for (int i = 0; i < n; i++) {
			val = A[Aiv[i]][i];
			for (int k = i; k < n; k++) {
				A[Aiv[i]][k] = A[Aiv[i]][k] / val;
			}
			for (int k = 0; k < n; k++) {
				tB[Biv[i]][k] = tB[Biv[i]][k] / val;
			}
		}
		
		double rat;
		for (int i = 0; i < n; i++) {
			for (int o = i; o > 0; o--) {
				rat = A[Aiv[o-1]][i];
				for (int k = i; k < n; k++) {
					A[Aiv[o-1]][k] = A[Aiv[o-1]][k] - A[Aiv[i]][k]*rat;
				}
				for (int k = 0; k < n; k++) {
					tB[Biv[o-1]][k] = tB[Biv[o-1]][k] - tB[Biv[i]][k]*rat;
				}
			}
		}

		for (int a = 0; a < n; a++){
			int tr = Biv[a];
			for (int k = 0; k < n; k++) {
				if (fabs(tB[Biv[a]][k]) < eps) {
					tB[Biv[a]][k] = 0;
				}
				B[a][k] = tB[Biv[a]][k];
			}
			
		}
	}

	return det;

}

int main(void) {

	double A[SIZE][SIZE], B[SIZE][SIZE], C[SIZE][SIZE];
	double b[SIZE], x[SIZE], det, eps = 1.e-13;

	int to_do;
	int m, n, p;

	scanf ("%d", &to_do);

	switch (to_do) {
		case 1:
			scanf("%d %d %d", &m, &p, &n);
			read_mat(A, m, p);
			read_mat(B, p, n);
			mat_product(A, B, C, m, p, n);
			print_mat(C, m, n);
			break;
		case 2:
			scanf("%d", &n);
			read_mat(A, n, n);
			printf("%.4f\n", gauss_simplified(A, n));
			break;
		case 3:
			scanf("%d", &n);
			read_mat(A,n, n);
			read_vector(b, n);
			det = gauss(A, b, x, n, eps);
			printf("%.4f\n", det);
			if(det) print_vector(x, n);
			break;
		case 4:
			scanf("%d", &n);
			read_mat(A,n,n);
			printf("%.4f\n",matrix_inv(A, B, n, eps));
			print_mat(B, n, n);
			break;
		default:
			printf("NOTHING TO DO FOR %d\n", to_do);
			break;
	}
	return 0;
}

