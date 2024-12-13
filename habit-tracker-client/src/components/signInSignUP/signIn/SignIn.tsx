import { useContext, useState } from "react";
import "./SignIn.css";
import { UserContext } from "../../../context/UserContext";

export default function SignIn() {
  const [email, setEamil] = useState("eyal@gmail.com");
  const [password, setPassword] = useState("1");
  const { setToken } = useContext(UserContext)!;
  const [error, setError] = useState("");

  const onClickSignIn = async () => {
    const formData = new URLSearchParams();
    formData.append("username", email);
    formData.append("password", password);
    ``;
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: formData,
    };
    const response = await fetch(
      "http://127.0.0.1:8000/api/login",
      requestOptions
    );
    const data = await response.json();
    if (!response.ok) {
      setError(data.detail);
    } else {
      setToken(data.access_token);
      setError("Success");
    }
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    // TODO: add validation
    onClickSignIn();
  };

  return (
    <>
      <h2>Sign In</h2>
      <form onSubmit={handleSubmit}>
        {error}
        <input
          type="email"
          id="email"
          value={email}
          onChange={(e) => {
            setEamil(e.target.value);
          }}
        />
        <input
          type="password"
          id="password"
          value={password}
          onChange={(e) => {
            setPassword(e.target.value);
          }}
        />
        <button type="submit">Sign In</button>
      </form>
    </>
  );
}
