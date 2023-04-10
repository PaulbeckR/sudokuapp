const boardElement = document.getElementById("board");
const newGameButton = document.getElementById("newGame");
const solveButton = document.getElementById("solve");
const validateButton = document.getElementById("validate");

// Add this function to fetch a Sudoku board from the backend
async function fetchSudokuBoard(difficulty) { 
   
    
    // Add the difficulty parameter
    try {
    
    
      const response = await fetch(`https://paulbeck.pythonanywhere.com/api/sudoku?difficulty=${difficulty}`); // Use backticks for the string
      const board = await response.json();
      console.log("API response:", board); 
      return board;
    } catch (error) {
      console.error("Error fetching the Sudoku board:", error);
      console.error("Error fetching the Sudoku board:", error);

      return null;
    }
}

// Modify the newGame function to use the fetched board
async function newGame() {
    const difficultyForm = document.getElementById("difficulty-form");
    const selectedDifficulty  = difficultyForm.difficulty.value;

    const board = await fetchSudokuBoard(selectedDifficulty);
    if (board) {
      renderBoard(board);
    } else {
      alert("Error fetching new Sudoku board. Please try again.");
    }
}

function renderBoard(boardData) {
    // Clear any existing board content
    boardElement.innerHTML = '';
  
    // Iterate through the rows and columns of the boardData
    for (let row = 0; row < 9; row++) {
      const rowElement = document.createElement("div");
      rowElement.classList.add("row");
  
      for (let col = 0; col < 9; col++) {
        const cellElement = document.createElement("input");
        cellElement.classList.add("cell");
        cellElement.type = "text";
        cellElement.maxLength = "1";
        cellElement.value = boardData[row][col] === 0 ? "" : boardData[row][col];
  
        rowElement.appendChild(cellElement);
      }
  
      boardElement.appendChild(rowElement);
    }
  }
  




// Add an event listener to the "New Game" button
newGameButton.addEventListener("click", newGame);

// Fetch and render an initial board when the page loads
newGame();
