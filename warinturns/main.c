/* 

warinturns -- A turn based strategy game

By Fernando Henrique

http://www.liquuid.net

*/
   
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "map1.h" 
#include "SDL.h"

/* Screen Resolution */

#define WIDTHSCREEN 800
#define HEIGTHSCREEN 600

int i,j;

int main(int argc, char *argv[])
{
	Uint32 initflags = SDL_INIT_VIDEO;  /* See documentation for details */

	/* SDL Surfaces */
	
	SDL_Surface *screen;
	SDL_Surface *ground;
	SDL_Surface *island;
	SDL_Surface *mnt;
	SDL_Surface *road;
	SDL_Surface *tree;
	SDL_Surface *water;
	SDL_Surface *city;
	SDL_Surface *capital;
	SDL_Surface *factory;
	SDL_Surface *select;
     

	SDL_Rect src , dest ;


	Uint8  video_bpp = 16;

	Uint32 videoflags = SDL_DOUBLEBUF;
	int    done;
	Uint32 colorkey;
	
    SDL_Event event;

	/* Initialize the SDL library */
	if ( SDL_Init(initflags) < 0 ) {
		printf("Couldn't initialize SDL: %s\n",
			SDL_GetError());
		return 1;
	}
	
	/* Make sure SDL_Quit gets called when the program exits! */
	atexit(SDL_Quit);


	/* Set WIDTHSCREENxHEIGTHSCREEN video mode */
	screen=SDL_SetVideoMode(WIDTHSCREEN,HEIGTHSCREEN, video_bpp, videoflags);
        if (screen == NULL) {
		printf("Couldn't set WIDTHSCREENxHEIGTHSCREENx%d video mode: %s\n",
                        video_bpp, SDL_GetError());
		SDL_Quit();
		return 2;
	}




	water = SDL_DisplayFormat (SDL_LoadBMP("water.bmp"));
	if (water == NULL) {
		printf("Unable to load bitmap.\n");
		return 1;
	}

	island = SDL_DisplayFormat (SDL_LoadBMP("island.bmp"));
	if (island == NULL) {
		printf("Unable to load bitmap.\n");
		return 1;
	}

	road = SDL_DisplayFormat (SDL_LoadBMP("road.bmp"));
	if (road == NULL) {
		printf("Unable to load bitmap.\n");
	return 1;
	}
	tree = SDL_DisplayFormat (SDL_LoadBMP("tree.bmp"));
	if (tree == NULL) {
		printf("Unable to load bitmap.\n");
		return 1;
	}
	mnt = SDL_DisplayFormat (SDL_LoadBMP("mnt.bmp"));
	if (mnt == NULL) {
		printf("Unable to load bitmap.\n");
		return 1;
	}

	ground = SDL_DisplayFormat (SDL_LoadBMP("ground.bmp"));
	if (ground == NULL) {
		printf("Unable to load bitmap.\n");
		return 1;
	}

	city = SDL_DisplayFormat (SDL_LoadBMP("city.bmp"));
	if (city == NULL) {
		printf("Unable to load bitmap.\n");
		return 1;
	}

	capital = SDL_DisplayFormat (SDL_LoadBMP("capital.bmp"));
	if (capital == NULL) {
		printf("Unable to load bitmap.\n");
		return 1;
	}

			factory = SDL_DisplayFormat ( SDL_LoadBMP("factory.bmp"));
			if (factory == NULL) {
			printf("Unable to load bitmap.\n");
			return 1;
	}

	select = SDL_DisplayFormat (SDL_LoadBMP("select.bmp"));
	if (select == NULL) {
		printf("Unable to load bitmap.\n");
		return 1;
	}


	
	for (i=0;i<12;i++){
		for (j=0;j<16;j++){
			src.x=0;
			dest.x=j*50;
			src.y=0;
			dest.y=i*50;
			printf("%d",map[i][j]);
			switch(map[i][j]){
			
				case 0  : SDL_BlitSurface(water, &src, screen, &dest);
						break;	
				case 1  : SDL_BlitSurface(ground, &src, screen, &dest);
						break;
				case 2  : SDL_BlitSurface(tree, &src, screen, &dest);
						break;
				case 3  : SDL_BlitSurface(road, &src, screen, &dest);
					break;
				case 4  : SDL_BlitSurface(mnt, &src, screen, &dest);
						break;
				case 5  : SDL_BlitSurface(island, &src, screen, &dest);
						break;
				case 6  : SDL_BlitSurface(city, &src, screen, &dest);
						break;
				case 7  : SDL_BlitSurface(capital, &src, screen, &dest);
						break;
				case 8  : SDL_BlitSurface(factory, &src, screen, &dest);
						break;
				default: SDL_BlitSurface(water, &src, screen, &dest);
				
			}
	
		}
		printf("\n");
	}
	colorkey = SDL_MapRGB(select->format, 255, 0, 255);
	SDL_SetColorKey(select, SDL_SRCCOLORKEY, colorkey);
	src.x=0;
	src.y=0;
	dest.x=100;
	dest.y=100;
	SDL_BlitSurface(select, &src, screen, &dest);
	
		
		SDL_Flip(screen);

	done = 0;
	while ( !done ) {
		/* Check for events */
		while ( SDL_PollEvent(&event) ) {
			switch (event.type) {

				case SDL_MOUSEMOTION:
					break;
				case SDL_MOUSEBUTTONDOWN:
					break;
				case SDL_KEYDOWN:
					/* Any keypress quits the app... */
				case SDL_QUIT:
					done = 1;
					break;
				default:
					break;
			}
		}

	}
	
	/* Clean up the SDL library */

	SDL_FreeSurface(ground);
	SDL_FreeSurface(tree);
	SDL_FreeSurface(city);
	SDL_FreeSurface(mnt);
	SDL_FreeSurface(road);
	SDL_FreeSurface(island);
	SDL_FreeSurface(capital);
	SDL_FreeSurface(factory);
	SDL_FreeSurface(select);
	SDL_FreeSurface(screen);
	



	SDL_Quit();
	return 0;
}
