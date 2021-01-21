#include <stdio.h>
#define MAX_FILE_SIZE (1024*1024)
int main(int argc[],char *argv[]){

	FILE *fpntr;
	int i;
	int pass=argv[1];
	char data[MAX_FILE_SIZE];
	fpntr=fopen(argv[2],"rb");
	while (!feof(fpntr))
		data[i++] = getc(fpntr);
	fclose(fpntr);
	fpntr=fopen(argv[2],"wb");
	for (int j=0; j<i-1; j++)
		putc((data[j] ^ pass),fpntr);
	fclose(fpntr);	
	return 0;
}

