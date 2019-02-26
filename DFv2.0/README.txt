TODO: Find some shit!

CHANGES: 
      2/10/19 Matt
                 -- added a fixMatrix() function, maps of all shapes and sizes now work
                 -- changed the printing a little bit, made steps count when we walk into a wall (this can be changed when we 
                 make the AI 'smarter', when they know not to walk into a wall). Also changed the printMap function so it is 
                 called on every iteration, personally I like it more that way for the same reason as the step counter, but we 
                 can change that if you guys object, "Democracy is King" is my favorite saying after all. 
        2/11/19 Matt
                 --added functionality to manually (and optionally) place player or portal in the map where we wish
                 --added -initOverride command line parameter that overrides previous change and initializes player/portal anyway
                 --added -noGraphics command line parameter that turns off the graphics for the AI/Map

OVERRIDE INITIALIZATION/NO GRAPHICS/NO SLEEP HOWTO:
By using a map with a 'p' and/or 'g' tile in them, we can override their positions and randomly place them by using the command:
      `python framework.py mapXX.txt -initOverride` or `-r`
      
We can also turn off graphics with the -noGraphics parameter
      `python framework.py mapXX.txt -noGraphics` or `-ng`
      
Lastly, we can make the program not sleep inbetween steps by the command
      `python framework.py mapXX.txt -fast` or `-f`
      
NOTE: The mapXX.txt is optional in all of these. The command line parameters can also appear in any order, so long 
      as the mapXX.txt comes first


READING MAPS BY INPUT
HOW TO DO:
python framework.py <map_file_name>
(test map will be used if no map file is passed)

FORMAT:
<height>
<width>
<matrix (NOT case-sensitive)>

ex:
WWWWW
WFFFW
WFFFW
WFFFW
WWWWW

NOTE:
changed the following (I know there is a bit of lost of meaning with these variable names but it is the most efficient method that I could come up with):
GRND 	->	F	#floor
WALL 	->	W 	#wall
PLAYER	->	P 	#player
PORTAL	->	G 	#goal
NONE 	-> 	N 	#none
