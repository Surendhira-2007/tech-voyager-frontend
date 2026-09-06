import { Routes, Route } from "react-router-dom";

import AIPredictions from "./AIPredictions";
import Login from "./login";

function Dashboard() {
  return (
    <div className="app">
      <div className="sidebar">
        <h2>Tech Voyager</h2>
        <p>AI Project Management</p>

        <nav>
          <a href="#/dashboard">📊 Dashboard</a>
          <a href="#/projects">📁 Projects</a>
          <a href="#/risk">⚠️ Risk Analysis</a>
          <a href="#/predictions">🤖 AI Predictions</a>
          <a href="#/alerts">🔔 Alerts</a>
          <a href="#/reports">📄 Reports</a>
        </nav>
      </div>

      <div className="content">
        <h1>Dashboard</h1>
        <h2>Welcome to Tech Voyager AI Project Management System.</h2>

        <div className="cards">
          <div className="card">
            <h3>Total Projects</h3>
            <h2>12</h2>
          </div>

          <div className="card">
            <h3>High Risk Projects</h3>
            <h2>3</h2>
          </div>

          <div className="card">
            <h3>AI Predictions</h3>
            <h2>8</h2>
          </div>
        </div>
      </div>
    </div>
  );
}

function RiskAnalysis() {
  return <h1>Risk Analysis Page</h1>;
}

function Alerts() {
  return <h1>Alerts Page</h1>;
}

function Reports() {
  return <h1>Reports Page</h1>;
}

function App() {
  return (
    <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/login" element={<Login />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/risk" element={<RiskAnalysis />} />
      <Route path="/predictions" element={<AIPredictions />} />
      <Route path="/alerts" element={<Alerts />} />
      <Route path="/reports" element={<Reports />} />
    </Routes>
  );
}

export default App;