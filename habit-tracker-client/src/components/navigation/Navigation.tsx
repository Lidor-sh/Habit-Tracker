import { navItems } from "../../constants/navigationConstants";
import "./Navigation.css";

export default function Navigation() {
  return (
    <>
      <div className="ToolBarContainer">
        <div className="NavContainer">
          {navItems.map((item, index) => {
            return (
              <a className="NavItem" href={item.url} key={index}>
                {item.name}
              </a>
            );
          })}
        </div>
      </div>
    </>
  );
}
