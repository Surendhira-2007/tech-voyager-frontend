import { useNavigate } from "react-router-dom";

function Login() {
  const navigate = useNavigate();

  const handleLogin = () => {
    navigate("/dashboard");
  };

  return (
    <div className="login-container">
      <div className="login-box">
        <h1>Tech Voyager</h1>
        <p>Login to your account</p>

        <input
          type="email"
          placeholder="Enter your email"
        />

        <input
          type="password"
          placeholder="Enter your password"
        />

        <button onClick={handleLogin}>
          Login
        </button>
      </div>
    </div>
  );
}

export default Login;