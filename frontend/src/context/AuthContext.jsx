import { createContext, useContext, useState, useCallback } from "react";
import { login as apiLogin } from "../api/client";

const AuthContext = createContext(null);

function AuthProvider({ children }) {
  const [token, setToken] = useState(() => sessionStorage.getItem("lc_token"));
  const [username, setUsername] = useState(() => sessionStorage.getItem("lc_user"));

  const login = useCallback(async (user, pass) => {
    const data = await apiLogin(user, pass);
    sessionStorage.setItem("lc_token", data.access_token);
    sessionStorage.setItem("lc_user", user);
    setToken(data.access_token);
    setUsername(user);
  }, []);

  const logout = useCallback(() => {
    sessionStorage.removeItem("lc_token");
    sessionStorage.removeItem("lc_user");
    setToken(null);
    setUsername(null);
  }, []);

  return (
    <AuthContext.Provider value={{ token, username, isAuthed: Boolean(token), login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used within AuthProvider");
  return ctx;
}

export { AuthProvider, useAuth };
