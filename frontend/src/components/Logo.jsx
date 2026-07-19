function Logo({ className = "w-7 h-7" }) {
  return (
    <svg viewBox="0 0 32 32" className={className} fill="none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="logoGrad" x1="0" y1="0" x2="32" y2="32" gradientUnits="userSpaceOnUse">
          <stop stopColor="#5b8def" />
          <stop offset="1" stopColor="#7c6ef2" />
        </linearGradient>
      </defs>
      <rect width="32" height="32" rx="8" fill="url(#logoGrad)" />
      <path
        d="M16 8v16M11 11l-3.5 6.5a3.5 3.5 0 0 0 7 0L11 11ZM21 11l-3.5 6.5a3.5 3.5 0 0 0 7 0L21 11ZM8 22h16"
        stroke="white"
        strokeWidth="1.6"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );
}

export default Logo;
