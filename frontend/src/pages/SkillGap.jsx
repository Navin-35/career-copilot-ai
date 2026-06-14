import { useState } from "react";
import api from "../services/api";

export default function SkillGap() {

  const [resumeId, setResumeId] =
    useState("");

  const [role, setRole] =
    useState("");

  const [result, setResult] =
    useState(null);

  const analyzeSkillGap = async () => {

    try {

      const response =
        await api.post(
          "/career/skill-gap",
          {
            resume_id:
              Number(resumeId),

            target_role:
              role
          }
        );

      setResult(
        response.data
      );

    } catch (error) {

      console.error(error);

      alert(
        "Failed"
      );
    }
  };

  return (

    <div className="p-8">

      <h1 className="text-3xl font-bold">

        Skill Gap Analysis

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
        className="bg-blue-600 text-white px-4 py-2 ml-2"
        onClick={analyzeSkillGap}
      >
        Analyze
      </button>

      {result && (

        <pre className="mt-6">

          {JSON.stringify(
            result,
            null,
            2
          )}

        </pre>

      )}

    </div>
  );
}