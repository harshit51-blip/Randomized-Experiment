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
A sample data source can be seen in the sample_data PNG file. You can clearly see the periodic nature of the system by looking at subsequent iterations and
matching the elemental data in previous iterations.

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

You can see the Periodic Nature of the system in the Periodic_Nature PNG file. It was run for only a 1,000 iterations, thus, as I said, bringing
the inherent periodic nature to life. 
Hence, due to the random and periodic behaviour of this system, and similarities to Random Walks, I have decided to call this
'Randomized Periodic Walks'.

Figure 1 is compiled for 100,000 iterations with 1,000 elements in the list in each iteration.
Figure 2 is compiled for 100,000 iterations as well but with only 10 elements in the list in each iteration.

This difference can be seen in the value of Cental Tendency (on y-axis), for figure 1, it's very low but in Figure 2 it's compounded easily
(Implying a direct proportionality, which is to be expected).

This is by design, however I am now interested making a mathematical model for this simulation of Random Walk, derive the RMS etc., to have
a clear picture of how and why these two systems are similar and how they are different.
I would also like to see how this technique, which gives a direct proportionality, can be used in computationally studying physical systems, 
for example, a large number of particles, where individual properties may be correlated.


Update 3: Plotted the version using Qiskit.
The code was very slow, 100,000 iterations took almost 3 hours to reach the halfway mark, had to shutdown.
This slowness was predicted (the intermediate data to be computed here is massive as compared to the classical version), although Code Optimization still required.
I have some Ideas, will update accordingly.
Instead, compiled 10,000 iterations with 10 elements in the list, Figure 1_quantum is the result. The similarity (identical) to the classical version is evident.
To show the periodic nature of the code, compiled 250 iterations, Figure 2_quantum is the result.



