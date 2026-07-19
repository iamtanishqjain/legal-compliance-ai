import { useState } from "react";
import { AuthProvider, useAuth } from "./context/AuthContext";
import { analyzeContract } from "./api/client";
import LoginScreen from "./components/LoginScreen";
import Header from "./components/Header";
import UploadCard from "./components/UploadCard";
import SummaryStats from "./components/SummaryStats";
import ObligationCard from "./components/ObligationCard";

function Dashboard() {
  const { token } = useAuth();
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleAnalyze(file) {
    setLoading(true);
    setError("");
    setResult(null);
    try {
      const data = await analyzeContract(file, token);
      setResult(data);
    } catch (err) {
      setError(err.message || "Something went wrong");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen">
      <Header />

      <main className="max-w-3xl mx-auto px-4 py-8 space-y-6">
        <UploadCard onAnalyze={handleAnalyze} loading={loading} />

        {error && (
          <div className="text-sm text-high bg-high/10 border border-high/20 rounded-xl px-4 py-3">
            {error}
          </div>
        )}

        {result && (
          <>
            <SummaryStats data={result} />
            <div className="space-y-3">
              {result.results.map((r) => (
                <ObligationCard key={r.obligation} result={r} />
              ))}
            </div>
          </>
        )}

        <p className="text-center text-xs text-muted pt-4 pb-8">
          Human-in-the-loop compliance pre-screening. Not a substitute for legal advice.
        </p>
      </main>
    </div>
  );
}

function AppContent() {
  const { isAuthed } = useAuth();
  return isAuthed ? <Dashboard /> : <LoginScreen />;
}

function App() {
  return (
    <AuthProvider>
      <AppContent />
    </AuthProvider>
  );
}

export default App;
