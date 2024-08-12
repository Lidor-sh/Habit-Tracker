import { navItems } from "../../constants/navigationConstants";
import "./Navigation.css";
import logo from "../../assets/logo.png";

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
        <div className="SignIn">Lets Start</div>
      </div>
    </>
  );
}
