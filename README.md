A small and simple code to plot a periodic but randomized central tendency of
a data source. 
Started out as an independent project to measure 'deterministic chaos' with a randomized variable.
But now looks like a specific version of Random Walks, not sure.
Original Inspiration - Starting point to computing a large number of particles, being affected by each other, such as gas particles in a box.
Early codes use randomint() to randomize the data source.
Used simple quantum mechanical principles (qiskit module - Aer simulator) to replace random().
Second possible study emerging: Measuring any difference between the data source plotted using Quantum Computing (Qiskit) and the pseudo-RNG of python (random),
Graph not yet plotted. Will be done soon.
Only the Data Source initialized.

Update: I was looking at a resource compilation by Gerard 't Hooft, linked below. I proceeded to check out some of his work and stumbled upon
something called the 'Cellular Automaton' Intepretation of Quantum Mechanics. I googled what a 'Cellular Automaton' is.
Apparantly, A cellular automaton is "a collection of "colored" cells on a grid of specified shape that evolves
through a number of discrete time steps according to a set of rules based on the states of neighboring cells. 
The rules are then applied iteratively for as many time steps as desired."
Now, at least the definition, is very similar (at least conceptually) to the system I designed in my program. Further Exploration required.

Links:
https://www.goodtheorist.science/classmech.html
https://mathworld.wolfram.com/CellularAutomaton.html#:~:text=A%20cellular%20automaton%20is%20a,many%20time%20steps%20as%20desired.

Update 2: I plotted my first graphs (NOT Qcomp) and the results were as expected, I had predicted they will be like 1-D Random Walks
but with a periodic feature (visible when graphs are compiled for fewer iterations).

Figure 1 is compiled for 100,000 iterations with 1,000 elements in the list in each iteration.
Figure 2 is compiled for 100,000 iterations as well but with only 10 elements in the list in each iteration.

This difference can be seen in the value of Cental Tendency (on y-axis), for figure 1, it's very low but in Figure 2 it's compounded easily
(Implying a direct proportionality, which is to be expected).

This is by design, however I am now interested making a mathematical model for this simulation of Random Walk, derive the RMS etc., to have
a clear picture of how and why these two systems are similar and how they are different.
I would also like to see how this technique, which gives a direct proportionality, can be used in computationally studying physical systems, 
for example, a large number of particles, where individual properties may be correlated.

I will plot the graphs for the model written using Qiskit soon.

