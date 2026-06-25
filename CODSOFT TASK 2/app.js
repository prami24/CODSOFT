const boardElement = document.getElementById('board');
const statusElement = document.getElementById('status');
const restartButton = document.getElementById('restart');

let board = Array(9).fill('');
let gameOver = false;

const wins = [
  [0, 1, 2], [3, 4, 5], [6, 7, 8],
  [0, 3, 6], [1, 4, 7], [2, 5, 8],
  [0, 4, 8], [2, 4, 6],
];

function renderBoard() {
  boardElement.innerHTML = '';
  board.forEach((value, index) => {
    const button = document.createElement('button');
    button.className = 'cell';
    button.type = 'button';
    button.textContent = value;
    button.disabled = gameOver || value !== '';
    if (value === 'X') button.classList.add('x');
    if (value === 'O') button.classList.add('o');
    button.addEventListener('click', () => handleHumanMove(index));
    boardElement.appendChild(button);
  });
}

function checkWinner(state) {
  for (const [a, b, c] of wins) {
    if (state[a] && state[a] === state[b] && state[a] === state[c]) {
      return { winner: state[a], line: [a, b, c] };
    }
  }
  return null;
}

function isDraw(state) {
  return state.every(cell => cell !== '');
}

function setStatus(message) {
  statusElement.textContent = message;
}

function highlightWin(line) {
  line.forEach(index => {
    const cell = boardElement.children[index];
    if (cell) cell.classList.add('win');
  });
}

function minimax(state, isMaximizing) {
  const result = checkWinner(state);
  if (result?.winner === 'O') return 1;
  if (result?.winner === 'X') return -1;
  if (isDraw(state)) return 0;

  if (isMaximizing) {
    let bestScore = -Infinity;
    for (let i = 0; i < state.length; i++) {
      if (state[i] === '') {
        state[i] = 'O';
        const score = minimax(state, false);
        state[i] = '';
        bestScore = Math.max(bestScore, score);
      }
    }
    return bestScore;
  }

  let bestScore = Infinity;
  for (let i = 0; i < state.length; i++) {
    if (state[i] === '') {
      state[i] = 'X';
      const score = minimax(state, true);
      state[i] = '';
      bestScore = Math.min(bestScore, score);
    }
  }
  return bestScore;
}

function getBestMove() {
  let bestScore = -Infinity;
  let move = -1;

  for (let i = 0; i < board.length; i++) {
    if (board[i] === '') {
      board[i] = 'O';
      const score = minimax(board, false);
      board[i] = '';
      if (score > bestScore) {
        bestScore = score;
        move = i;
      }
    }
  }

  return move;
}

function finishGame(result) {
  gameOver = true;
  if (result?.line) highlightWin(result.line);
  if (result?.winner === 'X') {
    setStatus('You win.');
  } else if (result?.winner === 'O') {
    setStatus('AI wins.');
  } else {
    setStatus('It is a draw.');
  }
  renderBoard();
}

function handleHumanMove(index) {
  if (gameOver || board[index] !== '') return;

  board[index] = 'X';
  renderBoard();

  let result = checkWinner(board);
  if (result || isDraw(board)) {
    finishGame(result);
    return;
  }

  setStatus('AI is thinking...');
  window.setTimeout(() => {
    const aiIndex = getBestMove();
    if (aiIndex !== -1) {
      board[aiIndex] = 'O';
    }

    renderBoard();
    result = checkWinner(board);
    if (result || isDraw(board)) {
      finishGame(result);
      return;
    }

    setStatus('Your turn: choose a cell.');
  }, 180);
}

function restartGame() {
  board = Array(9).fill('');
  gameOver = false;
  setStatus('Your turn: choose a cell.');
  renderBoard();
}

restartButton.addEventListener('click', restartGame);

restartGame();