#include <stdio.h>
#define MAX_FILE_SIZE (1024*1024)
int main(int argc[],char *argv[]){

	FILE *fptr;
	int i;
	int pass=argv[1];
	char data[MAX_FILE_SIZE];
	fptr=fopen(argv[2],"rb");
	while (!feof(fptr))
		data[i++] = fgetc(fptr);
	fclose(fptr);
	fptr=fopen(argv[2],"wb");
	for (int j=0; j<i-1; j++)
		fputc((data[j] ^ pass),fptr);
	fclose(fptr);	
	return 0;
}

