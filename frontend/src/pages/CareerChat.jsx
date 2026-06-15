import { useState } from "react";
import api from "../services/api";

export default function CareerChat() {

  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const askQuestion = async () => {

    if (!question.trim()) {
      alert("Please enter a question");
      return;
    }

    try {

      setLoading(true);

      const response = await api.post(
        "/career/ask",
        {
          question: question
        }
      );

      setAnswer(
        response.data.answer
      );

    } catch (error) {

      console.error(error);

      alert(
        "Failed to get answer from AI"
      );

    } finally {

      setLoading(false);
    }
  };

  return (

    <div className="p-8 max-w-4xl mx-auto">

      <h1 className="text-4xl font-bold mb-6">
        AI Career Coach
      </h1>

      <textarea
        rows="5"
        className="w-full border rounded-lg p-4 shadow-sm"
        placeholder="Ask your career question..."
        value={question}
        onChange={(e) =>
          setQuestion(
            e.target.value
          )
        }
      />

      <button
        onClick={askQuestion}
        className="bg-blue-600 text-white px-6 py-3 mt-4 rounded-lg hover:bg-blue-700 transition"
      >
        {loading
          ? "Thinking..."
          : "Ask AI"}
      </button>

      {answer && (

        <div className="bg-gray-100 rounded-lg p-6 mt-6 shadow">

          <h2 className="text-xl font-bold text-blue-600">
            AI Coach
          </h2>

          <p className="mt-4 whitespace-pre-wrap text-gray-800">
            {answer}
          </p>

        </div>

      )}

    </div>

  );
}