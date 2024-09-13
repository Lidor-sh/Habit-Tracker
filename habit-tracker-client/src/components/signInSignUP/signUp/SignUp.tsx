import { useContext, useState } from "react";
import "./SignUp.css";
import { UserContext } from "../../../context/UserContext";

export default function SignUp() {
  const [email, setEamil] = useState("");
  const [password, setPassword] = useState("");
  const [username, setUsername] = useState("");
  const { setToken } = useContext(UserContext)!;
  const [error, setError] = useState("");

  const onClickSignUp = async () => {
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        email: email,
        username: username,
        password: password,
        image: "1",
      }),
    };
    const response = await fetch("http://127.0.0.1:8000/api/users", requestOptions);
    const data = await response.json();
    if (!response.ok) {
      setError(data.detail);
    } else {
      setToken(data.access_token);
    }
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    // TODO: add validation
    onClickSignUp();
  };
  return (
    <>
      <form className="SignUpFormContainer" onSubmit={handleSubmit}>
        <div className="SignUpForm">
          <div className="Title">Sign Up</div>
          <div>{error}</div>
          <input
            type="email"
            id="email"
            placeholder="Email"
            value={email}
            onChange={(e) => {
              setEamil(e.target.value);
            }}
          />
          <input
            type="text"
            id="username"
            placeholder="Username"
            value={username}
            onChange={(e) => {
              setUsername(e.target.value);
            }}
          />
          <input
            type="password"
            id="password"
            placeholder="Password"
            value={password}
            onChange={(e) => {
              setPassword(e.target.value);
            }}
          />
          <button type="submit">Sign Up</button>
        </div>
      </form>
    </>
  );
}
