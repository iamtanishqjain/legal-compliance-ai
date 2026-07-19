import { useState } from "react";
import { useAuth } from "../context/AuthContext";
import Logo from "./Logo";

function LoginScreen() {
  const { login } = useAuth();
  const [username, setUsername] = useState("admin");
  const [password, setPassword] = useState("admin123");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e) {
    e.preventDefault();
    setError("");
    setLoading(true);
    try {
      await login(username, password);
    } catch (err) {
      setError(err.message || "Could not reach the API");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center px-4">
      <div className="w-full max-w-md">
        <div className="flex flex-col items-center mb-8">
          <div className="mb-3">
            <Logo className="w-12 h-12" />
          </div>
          <h1 className="text-2xl font-semibold text-white tracking-tight">Legal Compliance AI</h1>
          <p className="text-sm text-muted mt-1">Sign in to analyze employment contracts</p>
        </div>

        <form
          onSubmit={handleSubmit}
          className="bg-panel border border-border rounded-2xl p-7 shadow-2xl shadow-black/40 space-y-4"
        >
          <div>
            <label className="block text-xs font-medium text-muted mb-1.5" htmlFor="username">
              Username
            </label>
            <input
              id="username"
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
              className="w-full bg-bg border border-border rounded-lg px-3.5 py-2.5 text-sm text-white outline-none focus:border-accent focus:ring-2 focus:ring-accent/20 transition"
            />
          </div>

          <div>
            <label className="block text-xs font-medium text-muted mb-1.5" htmlFor="password">
              Password
            </label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              className="w-full bg-bg border border-border rounded-lg px-3.5 py-2.5 text-sm text-white outline-none focus:border-accent focus:ring-2 focus:ring-accent/20 transition"
            />
          </div>

          {error && (
            <div className="text-sm text-high bg-high/10 border border-high/20 rounded-lg px-3 py-2">
              {error}
            </div>
          )}

          <button
            type="submit"
            disabled={loading}
            className="w-full bg-gradient-to-r from-accent to-accent-2 text-white text-sm font-semibold rounded-lg py-2.5 hover:opacity-90 active:scale-[0.99] transition disabled:opacity-60 disabled:cursor-not-allowed"
          >
            {loading ? "Signing in…" : "Sign in"}
          </button>

          <p className="text-xs text-muted text-center pt-1">
            Demo credentials: <code className="text-white/80">admin</code> /{" "}
            <code className="text-white/80">admin123</code>
          </p>
        </form>
      </div>
    </div>
  );
}

export default LoginScreen;
