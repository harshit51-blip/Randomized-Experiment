A small and simple code to plot a periodic but randomized central tendency of
a data source. 
Started out as an independent project to measure 'deterministic choas' with a randomized variable.
But now looks like a specific version of Random Walks, not sure
Original Inspiration - Starting point to computing a large number of particles, being affected by each other, such as gas particles in a box.
Early codes use randomint() to randomize the data source.
Used simple quantum mechanical principles (qiskit module - Aer simulator) to replace random().
Second possible study emerging: Measuring any difference between the data source plotted using Quantum Computing (Qiskit) and the pseudo-RNG of python (random)
Graph not yet plotted. Will be done soon.
Only the Data Source initialized

Update: I was looking at a resource compilation by Gerard 't Hooft, linked below. I proceeded to check out some of his work and stumbled upon
something called the 'Cellular Automaton' Intepretation of Quantum Mechanics. I googled what a 'Cellular Automaton' is.
Apparantly, A cellular automaton is a collection of "colored" cells on a grid of specified shape that evolves
through a number of discrete time steps according to a set of rules based on the states of neighboring cells. 
The rules are then applied iteratively for as many time steps as desired.
Now, at least the definition, is very similar (at least conceptually) to the system I designed in my program. Further Exploration required.
It's quite amazing how I stumbled upon something like this.

Links:
https://www.goodtheorist.science/classmech.html
https://mathworld.wolfram.com/CellularAutomaton.html#:~:text=A%20cellular%20automaton%20is%20a,many%20time%20steps%20as%20desired.
