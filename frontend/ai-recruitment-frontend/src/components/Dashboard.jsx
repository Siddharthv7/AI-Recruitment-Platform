import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Dashboard() {

  const navigate = useNavigate();

  const username = localStorage.getItem("username");

  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const [jobDescription, setJobDescription] = useState("");

  const [jobResult, setJobResult] = useState(null);
  const [aiFeedback, setAiFeedback] = useState([]);

  // Upload Resume
  const handleUpload = async () => {

    if (!file) {
      alert("Select Resume");
      return;
    }

    const formData = new FormData();

    formData.append("file", file);

    try {

      const response = await axios.post(
        "https://ai-recruitment-platform-ph30.onrender.com/extract-skills",
        formData
      );

    setResult(response.data);

    setAiFeedback(response.data.ai_feedback || []);
    
    await axios.post(
        "https://ai-recruitment-platform-ph30.onrender.com/save-resume",
        {
            filename: file.name,
            skills: response.data.skills,
            resume_score: response.data.resume_score
        }
      );

    } catch (error) {

      console.log(error);

      alert("Upload Failed");
    }
  };

  // Match Job
  const handleJobMatch = async () => {

    try {

      const response = await axios.post(
        "https://ai-recruitment-platform-ph30.onrender.com/match-job",
        {
          resume_skills: result.skills,
          job_description: jobDescription
        }
      );

      setJobResult(response.data);

    } catch (error) {

      console.log(error);

      alert("Job Match Failed");
    }
  };

  // Logout
  const handleLogout = () => {

    localStorage.clear();

    navigate("/");
  };

  return (

    <div className="container">

      <div className="card">

        <h1>Dashboard</h1>

        <h3>
          Welcome {username} 🚀
        </h3>

        <input
          type="file"
          onChange={(e) => setFile(e.target.files[0])}
        />

        <button onClick={handleUpload}>
          Upload Resume
        </button>

        <textarea
          placeholder="Paste Job Description..."
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
          className="job-textarea"
        ></textarea>

        <button onClick={handleJobMatch}>
          Match Job
        </button>

        {/* Resume Result */}
        {result && (

          <div className="result-section">

            <h2>Resume Score</h2>

            <div className="progress-bar">

              <div
                className="progress-fill"
                style={{
                  width: `${result.resume_score}%`
                }}
              >
                {result.resume_score}%
              </div>

            </div>

            <h2>Skills</h2>

            <div className="skills-container">

              {result.skills.map((skill, index) => (

                <div
                  className="skill-badge"
                  key={index}
                >
                  {skill}
                </div>

              ))}

            </div>
            <h2>AI Resume Feedback</h2>

            <div className="skills-container">

            {aiFeedback && aiFeedback.map((item, index) => (

                <div
                className="missing-badge"
                key={index}
                >
                ⚠️ {item}
                </div>

            ))}

            </div>

          </div>

        )}

        {/* Job Result */}
        {jobResult && (

          <div className="result-section">

            <h2>Job Match Score</h2>

            <div className="progress-bar">

              <div
                className="progress-fill blue"
                style={{
                  width: `${jobResult.match_score}%`
                }}
              >
                {jobResult.match_score}%
              </div>

            </div>

            <h2>Matched Skills</h2>

            <div className="skills-container">

              {jobResult.matched_skills.map((skill, index) => (

                <div
                  className="skill-badge"
                  key={index}
                >
                  {skill}
                </div>

              ))}

            </div>

            <h2>Missing Skills</h2>

            <div className="skills-container">

              {jobResult.missing_skills.map((skill, index) => (

                <div
                  className="missing-badge"
                  key={index}
                >
                  {skill}
                </div>

              ))}

            </div>

          </div>

        )}

        <button onClick={handleLogout}>
          Logout
        </button>

      </div>

    </div>

  );
}

export default Dashboard;