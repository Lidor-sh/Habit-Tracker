import "./SignIn.css";

export default function SignIn() {
  return (
    <>
      <h2>Sign In</h2>
      <form>
        <input type="email" id="email" />
        <input type="text" id="username" />
        <input type="password" id="password" />
      </form>
    </>
  );
}
