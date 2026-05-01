export default function ScoreBoard({ score }) {
  return (
    <div className="scoreboard">
      <p>You: {score.user}</p>
      <p>Computer: {score.computer}</p>
    </div>
  );
}