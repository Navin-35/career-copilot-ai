import { useState } from "react";
import api from "../services/api";

export default function Roadmap() {

  const [resumeId, setResumeId] =
    useState("");

  const [role, setRole] =
    useState("");

  const [roadmap, setRoadmap] =
    useState(null);

  const generateRoadmap =
    async () => {

      try {

        const response =
          await api.post(
            "/roadmap/generate",
            {
              resume_id:
                Number(resumeId),

              target_role:
                role
            }
          );

        setRoadmap(
          response.data
        );

      } catch (error) {

        console.error(error);

        alert(
          "Roadmap failed"
        );
      }
    };

  return (

    <div className="p-8">

      <h1 className="text-3xl font-bold">

        Learning Roadmap

      </h1>

      <input
        className="border p-2 mt-4"
        placeholder="Resume ID"
        value={resumeId}
        onChange={(e)=>
          setResumeId(
            e.target.value
          )
        }
      />

      <input
        className="border p-2 mt-4 ml-2"
        placeholder="Target Role"
        value={role}
        onChange={(e)=>
          setRole(
            e.target.value
          )
        }
      />

      <button
        onClick={
          generateRoadmap
        }
        className="bg-green-600 text-white px-4 py-2 ml-2"
      >
        Generate
      </button>

      {roadmap && (

        <pre className="mt-6">

          {JSON.stringify(
            roadmap,
            null,
            2
          )}

        </pre>

      )}

    </div>
  );
}