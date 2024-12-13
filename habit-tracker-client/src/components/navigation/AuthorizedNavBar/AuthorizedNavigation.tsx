import { authNavItems } from "../../../constants/navigationConstants";
import "../Navigation.css";
import logo from "../../../assets/logo.png";
import { useContext } from "react";
import { UserContext } from "../../../context/UserContext";

export default function AuthorizedNavigation() {
  const { token, setToken, currentUser } = useContext(UserContext)!;

  console.log(currentUser);

  const logOut = () => {
    setToken(null);
    localStorage.setItem("UserToken", null!);
  };
  return (
    <>
      <div className="ToolBarContainer">
        <div className="LogoContainer">
          <img src={logo} className="Logo" />
          <h3>{currentUser ? currentUser.username : "null"}</h3>
        </div>
        <div className="NavContainer">
          {authNavItems.map((item, index) => {
            return (
              <a className="NavItem" href={item.url} key={index}>
                {item.name}
              </a>
            );
          })}
        </div>
        <div className="Signin-container" onClick={logOut}>
          <div className="SignIn">Logout</div>
        </div>
      </div>
    </>
  );
}
