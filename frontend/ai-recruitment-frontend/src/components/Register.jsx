import { useState } from "react";
import axios from "axios";
import { Link, useNavigate } from "react-router-dom";

function Register() {

  const navigate = useNavigate();

  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = async () => {

    try {

      const response = await axios.post(
        axios.post(`${import.meta.env.VITE_API_URL}/register`, data),
        {
          username: username,
          email: email,
          password: password,
        }
      );

      alert(response.data.message);

      navigate("/");

    } catch (error) {

      console.log(error);
      alert("Registration Failed");
    }
  };

  return (

    <div className="container">

      <div className="card">

        <h1>Register</h1>

        <input
          type="text"
          placeholder="Enter Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="input-field"
        />

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

        <button onClick={handleRegister}>
          Register
        </button>

        <p className="bottom-text">

          Already have account?

          <Link to="/" className="link">
            Login
          </Link>

        </p>

      </div>

    </div>

  );
}

export default Register;