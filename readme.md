# CSE 571 - AI Project 
## Topic: Bi-Directional(mm) Search Algorithm implementation


### Introduction
Following the paper given under this [link](http://www.aaai.org/ocs/index.php/AAAI/AAAI16/paper/download/12320/12109), the Bi-Directional algorithm has been understood and implemented using the Python language on the PACMAN domain. This project is based on the earlier class projects on the same domain, where other algorithms i.e., DFS, BFS, UCS, A* where implemented. The domain used in the project uses a set of pre-defined layouts along with custom created.

### Packages required for execution

- numpy ***v-1.19.5***
- pandas ***v-1.1.5***
- matplotlib ***v-3.3.4***
- seaborn ***v-0.11.2***
- scipy ***v-1.5.4***

### File structure
The main directory consists of the set of files along with another sub-directory named as ***1.Search***, with following details:
- In ***search.py*** file, all the algorithm implementation can be found.
- In ***layouts*** folder, all the layouts(pre-defined & custom) can be found.
- In ***layouts/Combination*** folder, all the combination of layouts(pre-defined & custom) with different Pacman-Food pairs can be found.
- The rest of the files are similar to the class project.

NOTE: The script file for running the code automatically to generate a resultant CSV file & other statistical results can be found directly under the root directory with file name as ***autorun.py***.


### Instructions for execution
- For generating a CSV file with results on different  layouts with different algorithm:
    - Go to the root directory of the project
    - Run the following command on the terminal to generate  the result on existing layouts 
        
        > `python3 autorun.py <args>` 
    
    - For generating different combination of layouts along with the result use the argument <code>-y</code> after the main command. Otherwise to run only for layouts in ***layouts*** folder use the argument <code>-n</code>(Note: Here the combinations are created having different Pacman-Food location pairs) .
    - For example
  
        > `python3 autorun.py -y` 
    
    - To run for all the combinations of the layouts  ***(Beware!!! It does take about 40 min to run for all combinations)***
    - Finally, A new csv file can be found generated with required Nodes expansion data. ( ***results_given_layouts.csv***  is generated for the layouts in ***/layouts*** folder and ***results_Combination_layouts.csv*** is generated for layouts in ***/layouts/Combination*** folder)
    - To execute statTest.py for generating the t-test results
        
        > `python3 statTest.py <arg1> <arg2>`

    - The two arguments are the names of the algorithms used for comparison.
    - The arguments can contain any values from the list ['dfs','bfs','ucs','astar','mm','mm0'] 
    - To execute the graphical_results.py for generating graph
        
        > `python3 graphical_results.py <args>`
  
    - The arguments can take in any layout names as input and generate the respective graphs for them

- For manual running of the code on the different layouts and algorithms, use the command below
    - Go to the sub-directory of the project ***1.Search***
    - Run the following command on the terminal to generate  the result 
        
        > `python3 pacman.py -l <layoutName> -p SearchAgent -a fn=<algorithm name>,prob=PositionSearchProblem,heuristic=manhattanHeuristic -q` 
    
    - For example:
        
        > `python3 pacman.py -l mediumMaze -p SearchAgent -a fn=mm,prob=PositionSearchProblem,heuristic=manhattanHeuristic -q`

    - Here the algorithm values that can be used in the command are 'dfs','bfs','ucs','aStar', 'mm'
    - To run for the MM0, Kindly remove the heuristic, For example:
        
        > `python3 pacman.py -l mediumMaze -p SearchAgent -a fn=mm,prob=PositionSearchProblem -q`
    - Omit -q in all the above commands to see the visual Pacman game running.

**NOTE:** 
- **All the commands executed are the under the anaconda CSE571 environment used for all the class projects**
- **The project has been implemented for PositionSearchProblem only**
