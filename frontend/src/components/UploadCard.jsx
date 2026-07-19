import { useCallback, useRef, useState } from "react";

function UploadCard({ onAnalyze, loading }) {
  const [file, setFile] = useState(null);
  const [dragOver, setDragOver] = useState(false);
  const inputRef = useRef(null);

  const pickFile = useCallback((f) => {
    if (f && f.type === "application/pdf") {
      setFile(f);
    }
  }, []);

  function handleDrop(e) {
    e.preventDefault();
    setDragOver(false);
    pickFile(e.dataTransfer.files?.[0]);
  }

  function handleSubmit(e) {
    e.preventDefault();
    if (file) onAnalyze(file);
  }

  return (
    <form onSubmit={handleSubmit} className="bg-panel border border-border rounded-2xl p-6">
      <h2 className="text-lg font-semibold text-white mb-1">Analyze a contract</h2>
      <p className="text-sm text-muted mb-4">
        Upload an employment contract (PDF) to check it against labour-law obligations.
      </p>

      <div
        onDragOver={(e) => {
          e.preventDefault();
          setDragOver(true);
        }}
        onDragLeave={() => setDragOver(false)}
        onDrop={handleDrop}
        onClick={() => inputRef.current?.click()}
        className={`cursor-pointer rounded-xl border-2 border-dashed px-6 py-10 text-center transition ${
          dragOver ? "border-accent bg-accent/5" : "border-border hover:border-white/20"
        }`}
      >
        <input
          ref={inputRef}
          type="file"
          accept="application/pdf"
          className="hidden"
          onChange={(e) => pickFile(e.target.files?.[0])}
        />
        <svg
          className="w-9 h-9 mx-auto mb-3 text-muted"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={1.5}
            d="M12 16.5V9m0 0-3 3m3-3 3 3M4.5 19.5h15A1.5 1.5 0 0 0 21 18V6a1.5 1.5 0 0 0-1.5-1.5h-15A1.5 1.5 0 0 0 3 6v12a1.5 1.5 0 0 0 1.5 1.5Z"
          />
        </svg>
        {file ? (
          <p className="text-sm text-white font-medium">{file.name}</p>
        ) : (
          <>
            <p className="text-sm text-white font-medium">Drop a PDF here or click to browse</p>
            <p className="text-xs text-muted mt-1">PDF only</p>
          </>
        )}
      </div>

      <button
        type="submit"
        disabled={!file || loading}
        className="mt-4 w-full bg-gradient-to-r from-accent to-accent-2 text-white text-sm font-semibold rounded-lg py-2.5 hover:opacity-90 active:scale-[0.99] transition disabled:opacity-40 disabled:cursor-not-allowed flex items-center justify-center gap-2"
      >
        {loading ? (
          <>
            <span className="w-4 h-4 border-2 border-white/40 border-t-white rounded-full animate-spin" />
            Analyzing…
          </>
        ) : (
          "Analyze contract"
        )}
      </button>
    </form>
  );
}

export default UploadCard;
