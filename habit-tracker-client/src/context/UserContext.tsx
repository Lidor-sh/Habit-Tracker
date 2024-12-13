import React, { createContext, ReactNode, useEffect, useState } from "react";

interface UserContextType {
  token: string | null;
  setToken: React.Dispatch<React.SetStateAction<string | null>>;
  currentUser: any;
}

interface UserProviderProps {
  children: ReactNode;
}

export const UserContext = createContext<UserContextType | null>(null);

export const UserProvider = ({ children }: UserProviderProps) => {
  const [token, setToken] = useState<string | null>(
    localStorage.getItem("UserToken")
  );
  const [currentUser, setCurrentUser] = useState<any>(null);

  useEffect(() => {
    const fetchUser = async () => {
      if (!token) {
        return;
      }
      const requestOptions = {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + token,
        },
      };
      const response = await fetch(
        "http://127.0.0.1:8000/api/user/me",
        requestOptions
      );

      if (!response.ok) {
        setToken(null);
        localStorage.setItem("UserToken", null!);
      } else {
        const userDate = await response.json();
        setCurrentUser(userDate);
        localStorage.setItem("UserToken", token!);
      }
    };
    fetchUser();
  }, [token]);

  return (
    <UserContext.Provider value={{ token, setToken, currentUser }}>
      {children}
    </UserContext.Provider>
  );
};
