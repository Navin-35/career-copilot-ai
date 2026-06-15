import { useState } from "react";
import api from "../services/api";

export default function Roadmap() {

  const [resumeId, setResumeId] = useState("");
  const [role, setRole] = useState("");
  const [roadmap, setRoadmap] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateRoadmap = async () => {

    if (!resumeId || !role) {
      alert("Please enter Resume ID and Target Role");
      return;
    }

    try {

      setLoading(true);

      const response = await api.post(
        "/roadmap/generate",
        {
          resume_id: Number(resumeId),
          target_role: role
        }
      );

      setRoadmap(response.data);

    } catch (error) {

      console.error(error);

      alert("Roadmap generation failed");

    } finally {

      setLoading(false);
    }
  };

  return (

    <div className="p-8 max-w-5xl mx-auto">

      <h1 className="text-4xl font-bold mb-6">
        Learning Roadmap
      </h1>

      <div className="flex flex-col md:flex-row gap-4">

        <input
          className="border rounded-lg p-3 flex-1"
          placeholder="Resume ID"
          value={resumeId}
          onChange={(e) =>
            setResumeId(e.target.value)
          }
        />

        <input
          className="border rounded-lg p-3 flex-1"
          placeholder="Target Role"
          value={role}
          onChange={(e) =>
            setRole(e.target.value)
          }
        />

        <button
          onClick={generateRoadmap}
          className="bg-green-600 text-white px-6 py-3 rounded-lg hover:bg-green-700"
        >
          {loading ? "Generating..." : "Generate"}
        </button>

      </div>

      {roadmap && (

        <div className="mt-8">

          <div className="bg-white border rounded-xl shadow p-6">

            <h2 className="text-2xl font-bold mb-4">
              Generated Roadmap
            </h2>

            <pre className="whitespace-pre-wrap text-sm overflow-auto">
              {JSON.stringify(
                roadmap,
                null,
                2
              )}
            </pre>

          </div>

        </div>

      )}

    </div>

  );
}