import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        brand: { DEFAULT: "#6842F5", deep: "#4830D9" },
        navy: { DEFAULT: "#101A33", slate: "#1B2742" },
        cloud: "#F4F6FB",
        ink: "#172033",
        success: "#16A34A",
        warning: "#F59E0B",
        danger: "#DC2626",
        info: "#2563EB",
      },
    },
  },
  plugins: [],
};
export default config;
