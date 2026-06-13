import { useState } from "react";
import api from "../services/api";

export default function UploadResume() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const uploadResume = async () => {
    if (!file) {
      alert("Please select a file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await api.post(
        "/resume/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      console.log("Success:", response.data);

      setMessage("Resume uploaded successfully!");

      alert("Resume uploaded successfully!");
    } catch (error) {
      console.error("Upload Error:", error);

      if (error.response) {
        console.log("Response Data:", error.response.data);
      }

      setMessage("Upload failed!");

      alert("Upload failed! Check browser console.");
    }
  };

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">
        Upload Resume
      </h1>

      <div className="border rounded-lg p-6 shadow-md max-w-lg">
        <input
          type="file"
          accept=".pdf"
          onChange={(e) => {
            setFile(e.target.files[0]);
          }}
        />

        <div className="mt-3">
          <strong>Selected File:</strong>{" "}
          {file ? file.name : "None"}
        </div>

        <button
          onClick={uploadResume}
          className="mt-4 bg-blue-600 text-white px-4 py-2 rounded"
        >
          Upload Resume
        </button>

        {message && (
          <p className="mt-4 font-semibold">
            {message}
          </p>
        )}
      </div>
    </div>
  );
}