import React, { createContext, ReactNode, useEffect, useState } from "react";

interface UserContextType {
  token: string | null;
  setToken: React.Dispatch<React.SetStateAction<string | null>>;
}

interface UserProviderProps {
  children: ReactNode;
}

export const UserContext = createContext<UserContextType | null>(null);

export const UserProvider = ({ children }: UserProviderProps) => {
    const [token, setToken] = useState<string|null>(localStorage.getItem("UserToken"));

    useEffect(() => {
        const fetchUser = async () => {
            const requestOptions = {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: "Bearer " + token
                },
            };
            const response = await fetch("http://127.0.0.1:8000/api/user/me", requestOptions);

            if (!response.ok){
                setToken(null);
            }
            localStorage.setItem("UserToken", token!);
        };
        fetchUser();
    },[token])
    
    return (
        <UserContext.Provider value={{token, setToken}}>
            {children}
        </UserContext.Provider>
    )
};