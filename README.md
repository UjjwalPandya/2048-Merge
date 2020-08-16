# 2048-Merge
A minimalistic code to define a function to merge a single row or column in Python.



Problem Statement/Objective:

In the first assignment, we have to focus on only one aspect of the 2048 game: merging tiles.




Summary:

The necessary and sufficient task to be performed through the programming perspective in this assignment is to define a function capable enough to merge a single row or column in 2048 game. I feel that before decomposing the major problem in different mini problems, it was very confusing for me to understand how to tackle the problem and due to that thought, I was not even able to start my work. But once I successfully decomposed the main problem into mini problems, everything was seemed to be clear to me. The most interesting part of this assignment is that the solution is structured in a very basic and minimalistic manner which can be easily understood even by the person without any knowledge of any sort of programming language.
 
 
 
Decomposition of the Problem:

The main objective of this assignment is to merge a single row or column in 2048 game. But in the process of solving this problem, there are different problems involved which are:

I.	Removing zeroes from the list: The main task performed in the 2048 game is  to merging two numbers by skipping the voids (which is the value ‘0’ in our case) present in between the two numbers with the same value or arranging the two numbers consecutively with the different values. As I am using ‘0’ in place of empty tiles (voids), it is necessary to remove all the zeroes from the list as zero is also an integer which will confuse the system resulting into irrelevant outputs.
To solve this problem, I have defined a function remove_zero.

II.	Merging the same values from the list: This is the most important part of our main problem. This part is responsible for merging two same values and forming a single value that is twice the original value and arranging two different values consecutively without merging them.
To solve this problem, I have defined a function merging.

III.	Adding back the zeroes to the list: Once we are done with the merging part, it is necessary to add the zeroes at the voids. This part is responsible for replacing the empty spaces with zeroes to maintain the dimensions of the game.
To solve this problem, I have defined a function add_zero.

IV.	Merge the list: It is very necessary that all the above-mentioned actions should be performed at one go. This part is responsible for simultaneous actions taken at one single input.
To solve this problem, I have defined a function merge.
 
 
 
Architecture:

A very simple architecture is formed for the inter-relationship of the user defined functions which can be easily understood. The solution depicts that first ‘remove_zero’ function will remove all the zeroes from the list and arrange the values consecutively. Then ‘merging’ function will take the result of the ‘remove_zero’ function and merge the same values by adding a zero at the void forming because of the merge and updates the result. Then ‘remove_zero’ function will remove all the zeroes from the list and arrange the values consecutively and updates the list again. Then ‘add_zero’ function will add the value ‘0’ at the voids to maintain the dimensions of the list. And all these functions are going to be performed in a single function, ‘merge’.
 
 
 
Code Design:

The code is designed in a very minimalistic way and executed in such a simple manner that a person without any sort of knowledge of any programming language can also understand it by just reading it once. The problem is decomposed in a very sophisticated and basic manner and all the sub problems and inter-related to each other which can also be understood by looking at the code. It’s an organized logical sequence of the approach towards the problem. There are four user-defined functions whose name is enough to explain their role in solving the problem.



Programming:

The code is implemented in a logical manner. As Python acts for each line of code simultaneously while executing it, it is necessary that all the user defined functions are arranged in a systematic manner. Before starting with the programming part, I had to take a quick revision on ‘EN2001: Introduction to Programming’ course. The implementation sequence is already been discussed in the previous sections and those are as follows:

I.	Removing zeroes from the list
To solve this problem, I have defined a function remove_zero.

II.	Merging the same values from the list
To solve this problem, I have defined a function merging.

III.	Adding back the zeroes to the list
To solve this problem, I have defined a function add_zero.

IV.	Merge the list
To solve this problem, I have defined a function merge.
