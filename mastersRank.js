var user = [
  {id: 1, name: 'Rick', totalScore: 0},
  {id: 2, name: 'Morty', totalScore: 0}
];

var playerList = [
  {playerName: 'Jon', rank: 1, score: 286, overUnder: -2},
  {playerName: 'Bob', rank: 2, score: 286, overUnder: -2},
  {playerName: 'Jill', rank: 3, score: 286, overUnder: -2},
  {playerName: 'Hank', rank: 4, score: 286, overUnder: -2},
  {playerName: 'Roger', rank: 5, score: 286, overUnder: -2},
  {playerName: 'Chris', rank: 6, score: 286, overUnder: -2}
];

var maxWeight = 10;

function removePlayer(player) {
  playerList.splice(player, 1);
  console.log("Removed Player: " + playerList[player].playerName);
  repopulate();
  console.log(playerList);

};

function repopulate() {
  for (i = 0; i < playerList.length; i++) {
    playerList[i].rank = i+1;
  }
}

function calculateWeight(player) {
  return (maxWeight - (playerList[player].rank-1));
}

function calculateScore(player) {
  return totalScore = calculateWeight(player) * playerList[player].score;
}

function calculateAllScores(id) {
  for (var i = 0; i < Object.keys(playerList).length; i++) {
    user[id].totalScore += calculateScore(i);
  }
}

console.log(playerList);
removePlayer(4);
