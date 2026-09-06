import { useState } from "react";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import "./App.css";

function Dashboard() {
  return (
    <div>
      <h1>📊 Dashboard</h1>
      <h2>Project Monitoring Dashboard</h2>

      <div className="cards">
        <div className="card">
          <h3>Total Projects</h3>
          <h2>1,981</h2>
          <p>📁 Active Projects</p>
        </div>

        <div className="card">
          <h3>High Risk Projects</h3>
          <h2>142</h2>
          <p>🔴 Requires Attention</p>
        </div>

        <div className="card">
          <h3>Delayed Projects</h3>
          <h2>325</h2>
          <p>⚠️ Schedule Delay</p>
        </div>
      </div>
    </div>
  );
}

function Projects() {
  const [projects, setProjects] = useState([
    {
      name: "Chennai Metro Project",
      status: "Delayed",
      risk: "High",
      progress: "65"
    },
    {
      name: "National Highway Project",
      status: "In Progress",
      risk: "Medium",
      progress: "78"
    },
    {
      name: "Smart City Project",
      status: "On Track",
      risk: "Low",
      progress: "90"
    }
  ]);

  const [showForm, setShowForm] = useState(false);

  const [newProject, setNewProject] = useState({
    name: "",
    status: "New",
    risk: "Low",
    progress: ""
  });

  const handleChange = (e) => {
    setNewProject({
      ...newProject,
      [e.target.name]: e.target.value
    });
  };

  const addProject = (e) => {
    e.preventDefault();

    if (newProject.name.trim() === "") {
      alert("Please enter a project name");
      return;
    }

    setProjects([...projects, newProject]);

    setNewProject({
      name: "",
      status: "New",
      risk: "Low",
      progress: ""
    });

    setShowForm(false);
  };

  return (
    <div>
      <div className="page-header">
        <div>
          <h1>📁 Projects</h1>
          <p>Manage and monitor all your projects</p>
        </div>

        <button
          className="add-btn"
          onClick={() => setShowForm(!showForm)}
        >
          + Add Project
        </button>
      </div>

      {showForm && (
        <form className="project-form" onSubmit={addProject}>

          <input
            type="text"
            name="name"
            placeholder="Project Name"
            value={newProject.name}
            onChange={handleChange}
          />

          <select
            name="status"
            value={newProject.status}
            onChange={handleChange}
          >
            <option>New</option>
            <option>In Progress</option>
            <option>Delayed</option>
            <option>On Track</option>
          </select>

          <select
            name="risk"
            value={newProject.risk}
            onChange={handleChange}
          >
            <option>Low</option>
            <option>Medium</option>
            <option>High</option>
          </select>

          <input
            type="number"
            name="progress"
            placeholder="Progress (%)"
            min="0"
            max="100"
            value={newProject.progress}
            onChange={handleChange}
          />

          <button type="submit" className="save-btn">
            Save Project
          </button>

        </form>
      )}

      <div className="project-grid">
        {projects.map((project, index) => (
          <div className="project-card" key={index}>
            <h2>{project.name}</h2>

            <p>
              <b>Status:</b> {project.status}
            </p>

            <p>
              <b>Risk Level:</b> {project.risk}
            </p>

            <p>
              <b>Progress:</b> {project.progress}%
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}

function RiskAnalysis() {
  const riskProjects = [
    {
      name: "Chennai Metro Project",
      score: 85,
      level: "High",
      factors: "Schedule delay, Cost overrun"
    },
    {
      name: "National Highway Project",
      score: 60,
      level: "Medium",
      factors: "Resource shortage"
    },
    {
      name: "Smart City Project",
      score: 25,
      level: "Low",
      factors: "No major issues"
    }
  ];

  return (
    <div>
      <div className="page-header">
        <div>
          <h1>⚠️ Risk Analysis</h1>
          <p>AI-powered project risk assessment</p>
        </div>
      </div>

      <div className="risk-grid">

        {riskProjects.map((project, index) => (
          <div className="risk-card" key={index}>

            <h2>{project.name}</h2>

            <div className="risk-score">
              Risk Score: <b>{project.score}/100</b>
            </div>

            <div className="risk-progress">
              <div
                className={`risk-progress-bar ${project.level.toLowerCase()}`}
                style={{ width: `${project.score}%` }}
              ></div>
            </div>

            <p>
              <b>Risk Level:</b> {project.level}
            </p>

            <p>
              <b>Risk Factors:</b> {project.factors}
            </p>

          </div>
        ))}

      </div>
    </div>
  );
}

function AIPredictions() {
  const predictions = [
    {
      project: "Chennai Metro Project",
      delay: "6 Months",
      cost: "12%",
      probability: "68%",
      recommendation: "Increase workforce and review the project schedule."
    },
    {
      project: "National Highway Project",
      delay: "2 Months",
      cost: "5%",
      probability: "82%",
      recommendation: "Monitor resource availability and material costs."
    },
    {
      project: "Smart City Project",
      delay: "No Major Delay",
      cost: "2%",
      probability: "95%",
      recommendation: "Project is progressing normally. Continue monitoring."
    }
  ];

  return (
    <div>
      <div className="page-header">
        <div>
          <h1>🤖 AI Predictions</h1>
          <p>AI-powered project outcome predictions</p>
        </div>
      </div>

      <div className="prediction-grid">

        {predictions.map((item, index) => (
          <div className="prediction-card" key={index}>

            <h2>{item.project}</h2>

            <div className="prediction-item">
              <span>⏳ Predicted Delay</span>
              <b>{item.delay}</b>
            </div>

            <div className="prediction-item">
              <span>💰 Cost Overrun</span>
              <b>{item.cost}</b>
            </div>

            <div className="prediction-item">
              <span>🎯 Completion Probability</span>
              <b>{item.probability}</b>
            </div>

            <div className="recommendation">
              <b>🤖 AI Recommendation</b>
              <p>{item.recommendation}</p>
            </div>

          </div>
        ))}

      </div>
    </div>
  );
}

function Alerts() {
  const alerts = [
    {
      project: "Chennai Metro Project",
      type: "High Risk",
      message: "AI predicts a possible project delay of 6 months.",
      level: "high"
    },
    {
      project: "National Highway Project",
      type: "Medium Risk",
      message: "Possible cost overrun due to increasing material costs.",
      level: "medium"
    },
    {
      project: "Smart City Project",
      type: "Low Risk",
      message: "Project is progressing normally with no major issues.",
      level: "low"
    }
  ];

  return (
    <div>
      <div className="page-header">
        <div>
          <h1>🔔 Early Warning Alerts</h1>
          <p>AI-generated alerts for project monitoring</p>
        </div>
      </div>

      <div className="alerts-container">
        {alerts.map((alert, index) => (
          <div className={`alert-card ${alert.level}`} key={index}>

            <div className="alert-header">
              <h2>{alert.project}</h2>

              <span className={`alert-badge ${alert.level}`}>
                {alert.type}
              </span>
            </div>

            <p className="alert-message">
              {alert.message}
            </p>

            <p className="alert-status">
              🔔 Status: Active
            </p>

          </div>
        ))}
      </div>
    </div>
  );
}

function Reports() {
  const reports = [
    {
      title: "Project Status Report",
      description: "Overall progress and current status of all projects.",
      date: "September 2026",
      icon: "📊"
    },
    {
      title: "Risk Assessment Report",
      description: "AI-based risk analysis and identified risk factors.",
      date: "September 2026",
      icon: "⚠️"
    },
    {
      title: "AI Prediction Report",
      description: "Predicted delays, cost overruns and completion probability.",
      date: "September 2026",
      icon: "🤖"
    }
  ];

  return (
    <div>
      <div className="page-header">
        <div>
          <h1>📄 Reports</h1>
          <p>Project monitoring and AI analysis reports</p>
        </div>
      </div>

      <div className="report-grid">
        {reports.map((report, index) => (
          <div className="report-card" key={index}>
            
            <div className="report-icon">
              {report.icon}
            </div>

            <h2>{report.title}</h2>

            <p>{report.description}</p>

            <div className="report-date">
              📅 {report.date}
            </div>

            <button className="view-report-btn">
              View Report
            </button>

          </div>
        ))}
      </div>
    </div>
  );
}

function App() {
  return (
    <BrowserRouter>
      <div className="app">
        
        <aside className="sidebar">
          <h2>🏛 TECH VOYAGER</h2>
          <p>Project Monitoring</p>

          <nav>
            <Link to="/">📊 Dashboard</Link>
            <Link to="/projects">📁 Projects</Link>
            <Link to="/risk">⚠️ Risk Analysis</Link>
            <Link to="/ai">🤖 AI Predictions</Link>
            <Link to="/alerts">🔔 Alerts</Link>
            <Link to="/reports">📄 Reports</Link>
          </nav>
        </aside>

        <main className="content">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/projects" element={<Projects />} />
            <Route path="/risk" element={<RiskAnalysis />} />
            <Route path="/ai" element={<AIPredictions />} />
            <Route path="/alerts" element={<Alerts />} />
            <Route path="/reports" element={<Reports />} />
          </Routes>
        </main>

      </div>
    </BrowserRouter>
  );
}

export default App;