const RISK_STYLES = {
  LOW: "text-low",
  MEDIUM: "text-medium",
  HIGH: "text-high",
  UNKNOWN: "text-muted",
};

function SummaryStats({ data }) {
  const { final_risk, compliance_score, summary } = data;

  return (
    <div className="bg-panel border border-border rounded-2xl p-6">
      <h2 className="text-lg font-semibold text-white mb-4">Compliance Summary</h2>
      <div className="grid grid-cols-3 gap-3">
        <Stat
          label="Overall Risk"
          value={final_risk}
          valueClass={RISK_STYLES[final_risk] || "text-white"}
        />
        <Stat label="Compliance Score" value={`${compliance_score}%`} valueClass="text-white" />
        <Stat label="Need Manual Review" value={summary.manual_review} valueClass="text-medium" />
      </div>

      <div className="mt-4 flex gap-2">
        <RiskPill label="Low" count={summary.LOW} tone="low" />
        <RiskPill label="Medium" count={summary.MEDIUM} tone="medium" />
        <RiskPill label="High" count={summary.HIGH} tone="high" />
      </div>
    </div>
  );
}

function Stat({ label, value, valueClass }) {
  return (
    <div className="bg-bg border border-border rounded-xl px-4 py-4 text-center">
      <div className={`text-2xl font-bold ${valueClass}`}>{value}</div>
      <div className="text-xs text-muted mt-1">{label}</div>
    </div>
  );
}

const TONE_CLASSES = {
  low: "bg-low/10 text-low border-low/20",
  medium: "bg-medium/10 text-medium border-medium/20",
  high: "bg-high/10 text-high border-high/20",
};

function RiskPill({ label, count, tone }) {
  return (
    <span className={`text-xs font-medium px-2.5 py-1 rounded-full border ${TONE_CLASSES[tone]}`}>
      {label}: {count}
    </span>
  );
}

export default SummaryStats;
