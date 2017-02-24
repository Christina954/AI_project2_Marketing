# AI_project2_Marketing Assignment

Background: 
  You have a graph	(a	social	network;	nodes	on	this	graph	correspond	to	
people,	links	to	personal	friendships).	 You	wish	to	choose	a	set	of	K	nodes	in	this	
graph	so	that	the	total	number	of	graph	neighbors	of	these	nodes is	
maximized	over	all	possible	subsets	of	K	nodes	on	the	graph.
Note to self: the	total	number	of	neighbors	of	K	nodes	is	not	the	same	as	the	sum	of	the	numbers	
of	friends	each	node	has	(there	will	usually	be	overlap	in	friends	among	
individuals).

Goal: 
  Implement an	“agent”	who	computes	a	set	
of	K	nodes	(specified	as	“budget”)	that	they	wish	to	“seed”	(that	is,	to	target). In	task	
1,	I use	a	branch-and-bound	search	for	this and I use an alternative algorithm for task	2. 
Try to have runtime	<	0.06	seconds and utility	=	27.3. 

Files: 
Root	directory:
runSimulations.py:	the	driver	(to	run code,	just	type	python	
runSimulations.py)
runSimulationsTask2.py:	the	driver	(to	run	code,	just	type	python	
runSimulationsTask2.py) for	task	2 
util.py
network	directory	(package)
node.py:	implementation	of	a	node	in	the	network
network.py:	implementation	of	the	network class,	including	the	graph	generator.	
Nodes	in	this	network	are	going	to	be	referred	to	by	their	index,	which	
runs	from	0	to	numNodes	– 1.
cascade	directory	(package)
agents	directory	(package)
agent.py:	a	superclass	for	the	agent	
myagent.py:	agent	implementation.

