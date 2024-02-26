#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>


// Drawing the world
void draw(void *u, int w, int h)
{
	char (*world)[w] = u;
	// Clearing the screen.
	printf("\033[H");
	for (int i=0; i<w; i++){
		for (int j=0; j<h; j++)
			printf(world[i][j] ? "X" : " "); //showing the living cells with X.
		printf("\n");
	}
}

// Applying the basic rules of the `Game Of Life`.
// 1- Any live cell with fewer then two live neighbors dies, as if by underpopulation.
// 2- Any live cell with two or three live neighbors lives on to the next generation.
// 3- Any live cell with more than 3 live neighbors dies, as if by overpopulation.
// 4- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproductoin.
void evolution(void *u, int w, int h)
{
	char (*world)[w] = u;
	char new[w][h];

	for (int i=0; i<w; i++){
		for (int j=0; j<h; j++){
			int lives = 0;
			for (int x=i-1; x<=i+1; x++)
				for (int y=j-1; y<=j+1; y++)
					if (world[(y + h) % h][(x + w) % w])
						lives++;
			if (world[j][i]) lives--;
			// The cell in [i][j] lives if it has 3 living neighbors.
			// Any cell lives if at least has 2 living neighbors.
			new[j][i] = (lives==3 || (lives==2 && world[j][i]));
		}
	}
	// Updating the world
	for (int i=0; i<w; i++)
		for (int j=0; j<h; j++)
			world[i][j] = new[i][j];
}


int main()
{
	// Initializing the world
	int w=30;
	int h=30;
	char world[w][h];
	// for a better random number.
	srand(time(0));

	// Initializing the world with some random live cell.
	for (int i=0; i<w; i++)
		for (int j=0; j<h; j++)
			world[i][j] = rand() < RAND_MAX/10 ? 1 : 0;
	// The main loop of the game	
	while (1){
		draw(world, w, h);
		evolution(world, w, h);
		sleep(1);	
	}

	return 0;	
}
