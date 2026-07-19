const DEFAULT_API_BASE = import.meta.env.VITE_API_URL || "http://localhost:8000";

function getApiBase() {
  return localStorage.getItem("lc_api_base") || DEFAULT_API_BASE;
}

function setApiBase(url) {
  localStorage.setItem("lc_api_base", url.replace(/\/$/, ""));
}

async function login(username, password) {
  const body = new URLSearchParams();
  body.set("username", username);
  body.set("password", password);

  const res = await fetch(`${getApiBase()}/token`, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body,
  });

  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail || "Invalid username or password");
  }

  return res.json();
}

async function analyzeContract(file, token) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${getApiBase()}/analyze`, {
    method: "POST",
    headers: { Authorization: `Bearer ${token}` },
    body: formData,
  });

  if (res.status === 403) {
    throw new Error("Session expired. Please sign in again.");
  }
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail || "Analysis failed. Is the backend running?");
  }

  return res.json();
}

async function checkHealth() {
  try {
    const res = await fetch(`${getApiBase()}/`, { method: "GET" });
    return res.ok;
  } catch {
    return false;
  }
}

export { getApiBase, setApiBase, login, analyzeContract, checkHealth };
