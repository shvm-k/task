import React, { useState } from "react";
import axios from "axios";

const FileUploader = () => {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState("");

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post("http://127.0.0.1:8000/upload-pdf/", formData);
      if (response.data.success) {
        setResult(JSON.stringify(response.data.data, null, 2));
      } else {
        setResult(`Error: ${response.data.error}`);
      }
    } catch (error) {
      setResult(`Error: ${error.message}`);
    }
  };

  return (
    <div>
      <h1>Upload PDF</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
      <pre>{result}</pre>
    </div>
  );
};

export default FileUploader;
