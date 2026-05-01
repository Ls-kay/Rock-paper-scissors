export default function ChoiceButton({ choice, onClick }) {
  return (
    <button className="choice-btn" onClick={() => onClick(choice)}>
      {choice.toUpperCase()}
    </button>
  );
}