import "./SignUp.css";

export default function SignUp() {
  return (
    <>
      <form className="SignUpFormContainer">
        <div className="SignUpForm">
          <div className="Title">Sign Up</div>
          <input type="email" id="email" placeholder="Email" />
          <input type="text" id="username" placeholder="Username" />
          <input type="password" id="password" placeholder="Password" />
          <button>Sign Up</button>
        </div>
      </form>
    </>
  );
}
