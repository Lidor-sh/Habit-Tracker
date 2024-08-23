import { Link } from "react-router-dom";
import "./LoginPage.css";
import SignIn from "../../components/signInSignUP/signIn/SignIn";
import SignUp from "../../components/signInSignUP/signUp/SignUp";
export default function LoginPage() {
  return (
    <>
      <div className="LoginOutline">
        <Link to={"/"}>Return Home</Link>
        <div className="LoginContainer">
          <SignIn />
          <SignUp />
        </div>
      </div>
    </>
  );
}
