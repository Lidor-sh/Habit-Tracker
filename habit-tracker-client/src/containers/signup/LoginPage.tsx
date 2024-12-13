import { Link, redirect, useNavigate } from "react-router-dom";
import "./LoginPage.css";
import SignIn from "../../components/signInSignUP/signIn/SignIn";
import SignUp from "../../components/signInSignUP/signUp/SignUp";
import { useContext, useEffect } from "react";
import { UserContext } from "../../context/UserContext";
export default function LoginPage() {
  const { token } = useContext(UserContext)!;
  const navigate = useNavigate();
  useEffect(() => {
    console.log("in the useEffect!!!");

    if (token) {
      console.log("blabla");
      navigate("/Habbit-Tracker");
    } else {
      console.log("Else");
    }
  }, [token]);
  return (
    <>
      <Link to={"/"}>Return Home</Link>
      <div className="LoginOutline">
        <div className="LoginContainer">
          <SignIn />
          <SignUp />
        </div>
      </div>
    </>
  );
}
