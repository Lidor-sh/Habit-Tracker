import { useContext, useEffect } from "react";
import { UserContext } from "../../context/UserContext";
import { useNavigate } from "react-router-dom";
import AuthorizedNavigation from "../../components/navigation/AuthorizedNavBar/AuthorizedNavigation";
import Habits from "../../components/Habit/Habits/Habits";

export default function AuthorizedHomePage() {
  const { token, setToken, currentUser } = useContext(UserContext)!;

  const navigate = useNavigate();
  useEffect(() => {

    if (!token) {
      navigate("/");
    } else {
    }
  }, [token]);
  return (
    <>
      <AuthorizedNavigation />
      <div>
        <Habits />
      </div>
    </>
  );
}
