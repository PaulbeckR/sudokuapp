# sudokuapp
SudokuApp



How to run program in Visual Studio: 

1. Environment: 
    Pip install pygame, version 2.1.3.dev8

2. Run main.py to run new sudoku game.





Sudoku is a puzzle game where each row, column and 3x3 box of a 9x9 grid must only contain once instance of each number 1-9. Players receive a partially completed board to fill in the remaining numbers. 


This program creates single-solution sudoku boards for players to complete in python. For a sudoku game to be "valid", there must only be one possible solution. The back-solving algorithm uses a constraint based search before checking all possible solutions for each board and is outlined in greater detail below.

The GUI was created with the pygame library and is hosted initially on trinket.io. See the "Future Developments" section below for what features/improvements are planned. 



Primary Python files: 

    main2.py 

        - This file contains the code needed to run the sudoku game and generate a playable game within the pygame library. Clone the app library and run this file to play a sudoku game. 

        Features:
            1. Difficulty Selection: Easy / Medium / Hard. 
            2. Loading screen (To support time needed for generating board)
            3. Game Play: 
                - Notes versus Solution entry: Users can edit possible candidates for a square, or enter a solution. Non-valid solutions are not accepted (for now)
                - Update Notes: A buton to auto-enter all possible candiates for each empy square. 


    BackSolver.py

        - This file contains the code for the full back-solving algorithm to generate unique solution sudoku boards. It follows the general steps: 

        0. Identify solution conditions (Difficulty level, maximum clues for game board)
        1. Generate Complete Sudoku Board: A 9x9 grid is created with numbers 1-9 stored only once for each row/col/box. This is created with a simple back-solving algorithm to ensure a valid board is created.
        2. Remove one number from the solution.
        3. Check all possible solutions for solving the grid. 
        4. If there is only one possible solution, return to step two and continue until solution conditions are met or clues have reached 17**
            - As of today, the minimum number of clues for a sudoku puzzle to have a single solution has been found to be 17. 
        5. If 17 clues have been reached without a solution, return current boards** This will be changed to starting the loop over and starting with a new solution board.


Analysis of back-solving algorithm: 

    Questions: 

        1. What is the best way to set difficulty levels? 
            - Number and/or type of strategies used? 
            - Time spent in creating the board? 
        
        2. Initial algorithm includes a "max_count" reset, where any search that loops X times is reset, starting with fresh board. Is this helpful to reduce time spent finding boards? Are certain counts better than others? 
            - Shouldn't my back-solver be able to go back one ore more steps if no unique solutions are found? Rather than just staying in place? But I would need to know how at each point how many clues are available before knowing I have checked each one. 
            - I am also checking at random... and so risk checking the same number. I should save the available positions (clues) in a list for each instance and try removing each one before back stepping to the previous solution? 

        3. How much memory is used for the algorithm? Are there ways to improve this?

        4. Is there a better way? 

            - Technically, each board will remove up to X clues at the beginning of a search if placed correctly, as removing them would always lead to a single solution. Could this mean that X clues could be removed from strategic places to spead up the search? 



Planned Improvements/Changes: 

    1. GUI: 
        - JavaScript/CSS/HTML using pythoneverywhere.com for more functional hosting and development of the user interface. 
        - Pygame: End Game screen, allowing New Game or Exit. 

    2. BackSolver.py: 

        - Analyze and identify optimal difficulty level settings. 
            - Add "Extremely Difficult" level with the addition of more advanced strategies?
        - Reduce computational requirements for backsolver - using predetermined and randomize positions to remove numbers. Remove board_reset unless clues under 17. 


    3. Additional Strategies: 

        - XYWing 
        - Swordfish


    4. Code Organization/Optimization 

        - Merge/Reduce files and organize by functionality. (Eg. reduce number of print_grid methods, counting clues)
        - Explore numpy arrays for increased optimization/speed? 
        - Refactor to use classes instead of copy.deepcopy
    



        https://projectgurukul.org/create-sudoku-game-python/



        The strategies used in the current algorithm include:           1. Only one option: A single number is the only possible option for a given square. A solution is found.          2. Naked Pairs/Triplets: A naked pair/triplet is any 2 or 3 squares that contain the same 2 or 3 numbers.                All other instances of that number in the same row/col or box can be removed.            3. Hidden Pairs/Triplets: A HIDDEN pair/triplet is any 2 or 3 squares that contain the same 2 or 3                 numbers where no other square of that same row/col/box includes them. Any other number listed                  in the 2 or 3 squares identified in the pair/triple can be removed.             4. Candidate Lines: Another exclusionary strategy in two parts:                         a. Rows and Cols versus Boxes: If a number is identified to be eligible in one row or col of a                             box. Then it can be removed as an eligible candidate for any other square of that same                              row/col.                         b.  