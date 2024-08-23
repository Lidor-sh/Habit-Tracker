import { navItems } from "../../constants/navigationConstants";
import "./Navigation.css";
import logo from "../../assets/logo.png";
import { Link } from "react-router-dom";

export default function Navigation() {
  return (
    <>
      <div className="ToolBarContainer">
        <div className="LogoContainer">
          <img src={logo} className="Logo" />
          <h3>Habit Tracker</h3>
        </div>
        <div className="NavContainer">
          {navItems.map((item, index) => {
            return (
              <a className="NavItem" href={item.url} key={index}>
                {item.name}
              </a>
            );
          })}
        </div>
        <Link to={"/signup"} className="Signin-container">
          <div className="SignIn">Let's Start</div>
        </Link>
      </div>
    </>
  );
}
