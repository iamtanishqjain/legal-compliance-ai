import { useAuth } from "../context/AuthContext";
import Logo from "./Logo";

function Header() {
  const { username, logout } = useAuth();

  return (
    <header className="border-b border-border">
      <div className="max-w-3xl mx-auto px-4 py-4 flex items-center justify-between">
        <div className="flex items-center gap-2.5">
          <Logo className="w-7 h-7" />
          <span className="font-semibold text-white tracking-tight">Legal Compliance AI</span>
        </div>
        <div className="flex items-center gap-3">
          <span className="text-sm text-muted hidden sm:inline">Signed in as {username}</span>
          <button
            onClick={logout}
            className="text-sm font-medium text-white/80 border border-border rounded-lg px-3 py-1.5 hover:bg-white/5 transition"
          >
            Sign out
          </button>
        </div>
      </div>
    </header>
  );
}

export default Header;
