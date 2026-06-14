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

    <div className="p-8">

      <h1 className="text-3xl font-bold mb-4">
        AI Career Coach
      </h1>

      <textarea
        rows="5"
        className="w-full border rounded p-3"
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
        className="bg-blue-600 text-white px-4 py-2 mt-4 rounded"
      >
        {loading ? "Thinking..." : "Ask AI"}
      </button>

      {answer && (

        <div className="mt-6 border rounded p-4 bg-gray-100">

          <h2 className="font-bold text-lg mb-2">
            AI Response
          </h2>

          <p>{answer}</p>

        </div>

      )}

    </div>
  );
}