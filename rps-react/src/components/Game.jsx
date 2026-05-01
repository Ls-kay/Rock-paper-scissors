import { useState } from "react";
import ChoiceButton from "./ChoiceButton";
import ScoreBoard from "./ScoreBoard";

const choices = ["rock", "paper", "scissors"];

export default function Game() {
  const [userChoice, setUserChoice] = useState(null);
  const [computerChoice, setComputerChoice] = useState(null);
  const [result, setResult] = useState("");
  const [score, setScore] = useState({ user: 0, computer: 0 });

  const getComputerChoice = () => {
    return choices[Math.floor(Math.random() * choices.length)];
  };

  const determineWinner = (user, comp) => {
    if (user === comp) return "Draw";

    if (
      (user === "rock" && comp === "scissors") ||
      (user === "paper" && comp === "rock") ||
      (user === "scissors" && comp === "paper")
    ) {
      setScore((prev) => ({ ...prev, user: prev.user + 1 }));
      return "You Win";
    } else {
      setScore((prev) => ({ ...prev, computer: prev.computer + 1 }));
      return "You Lose";
    }
  };

  const handleChoice = (choice) => {
    const comp = getComputerChoice();
    setUserChoice(choice);
    setComputerChoice(comp);
    setResult(determineWinner(choice, comp));
  };

  return (
    <div className="game">
      <div className="choices">
        {choices.map((choice) => (
          <ChoiceButton key={choice} choice={choice} onClick={handleChoice} />
        ))}
      </div>

      <div className="results">
        <p>You: {userChoice}</p>
        <p>Computer: {computerChoice}</p>
        <h2>{result}</h2>
      </div>

      <ScoreBoard score={score} />
    </div>
  );
}