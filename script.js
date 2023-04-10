const boardElement = document.getElementById("board");
const newGameButton = document.getElementById("newGame");
const solveButton = document.getElementById("solve");
const validateButton = document.getElementById("validate");

// Add this function to fetch a Sudoku board from the backend
async function fetchSudokuBoard() {
    try {
      const response = await fetch("https://paulbeck.pythonanywhere.com/generate?difficulty=${difficulty}");
      const board = await response.json();
      return board;
    } catch (error) {
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
  
  // Add an event listener to the "New Game" button
  newGameButton.addEventListener("click", newGame);
  
  // Fetch and render an initial board when the page loads
  newGame();
  