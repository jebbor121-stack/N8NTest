'''
// A very simple game in JavaScript

function startGame() {
  alert("Welcome to the Simple Game!");
  let playerName = prompt("What's your name?");
  if (playerName) {
    alert("Hello, " + playerName + "! Let's play.");
    // More game logic can be added here
    alert("Game over for now, " + playerName + "!");
  } else {
    alert("No name entered. Exiting game.");
  }
}

startGame();
'''