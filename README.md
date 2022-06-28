# drivetimes
a script for calling OSRM to get driving times between a set of sources and destinations

Use:  Coordinates go in coords in Lat,Long format.  (Note that OSRM uses Long,Lat instead; coordinates are switched during processing.)
The top line is for sources, and the other lines are all destinations.  In this way, the coordinates are laid out like labels in a table.

The script processes coordinates from coords, and puts results in results.txt.  The results are ordered such as to fill in the table implied by the positions of sources and destinations in coords.
