import { useState } from "react";
import axios from "axios";
import { Link, useNavigate } from "react-router-dom";

function Login() {

  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/login",
        {
          email: email,
          password: password,
        }
      );

    localStorage.setItem(
        "token",
        response.data.access_token
        );
    localStorage.setItem(
        "username",
        response.data.user.username
        );

    alert("Login Success");

    navigate("/dashboard");

    } catch (error) {

      console.log(error);
      alert("Login Failed");
    }
  };

  return (

    <div className="container">

      <div className="card">

        <h1>Login</h1>

        <input
          type="email"
          placeholder="Enter Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="input-field"
        />

        <input
          type="password"
          placeholder="Enter Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="input-field"
        />

        <button onClick={handleLogin}>
          Login
        </button>

        <p className="bottom-text">

          Don't have account?

          <Link to="/register" className="link">
            Register
          </Link>

        </p>

      </div>

    </div>

  );
}

export default Login;