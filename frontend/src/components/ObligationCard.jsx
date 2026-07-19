const BORDER_CLASSES = {
  LOW: "border-l-low",
  MEDIUM: "border-l-medium",
  HIGH: "border-l-high",
};

const BADGE_CLASSES = {
  LOW: "bg-low/10 text-low",
  MEDIUM: "bg-medium/10 text-medium",
  HIGH: "bg-high/10 text-high",
};

function ObligationCard({ result }) {
  const { obligation, risk, matched_sentence, explanation, manual_review, similarity_score } = result;

  return (
    <div
      className={`bg-panel border border-border border-l-4 rounded-xl p-5 ${
        BORDER_CLASSES[risk] || "border-l-border"
      }`}
    >
      <div className="flex items-start justify-between gap-3 mb-2">
        <h3 className="font-semibold text-white">{obligation}</h3>
        <span
          className={`shrink-0 text-[11px] font-bold uppercase tracking-wide px-2.5 py-1 rounded-full ${
            BADGE_CLASSES[risk] || "bg-white/10 text-white"
          }`}
        >
          {risk}
        </span>
      </div>

      {matched_sentence ? (
        <blockquote className="text-sm italic text-muted border-l-2 border-border pl-3 mb-2">
          "{matched_sentence}"
        </blockquote>
      ) : (
        <p className="text-sm italic text-muted mb-2">No matching clause found in the contract.</p>
      )}

      <p className="text-sm text-white/90">{explanation}</p>

      <div className="flex items-center gap-3 mt-3 text-xs text-muted">
        <span>Similarity: {(similarity_score * 100).toFixed(0)}%</span>
        {manual_review && (
          <span className="text-medium font-medium flex items-center gap-1">
            <svg className="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M12 9v3.75m9-.75a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9 3.75h.008v.008H12v-.008Z"
              />
            </svg>
            Manual review recommended
          </span>
        )}
      </div>
    </div>
  );
}

export default ObligationCard;
