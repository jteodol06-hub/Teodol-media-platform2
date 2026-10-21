import Sidebar from "@/components/Sidebar";

const stats = [
  { label: "Files processed", value: "24", trend: "12% from last week" },
  { label: "Minutes processed", value: "1,482", trend: "16% from last week" },
  { label: "Tokens used", value: "324,560", trend: "16% from last week" },
];

export default function Dashboard() {
  return (
    <div className="flex min-h-screen">
      <Sidebar active="/dashboard" />
      <main className="flex-1 p-8">
        <h1 className="text-2xl font-semibold">Good evening, Josephine</h1>
        <p className="mb-6 text-sm text-slate-500">Here&apos;s what&apos;s happening with your workspace today.</p>
        <div className="grid gap-4 sm:grid-cols-3">
          {stats.map((s) => (
            <div key={s.label} className="rounded-xl border border-slate-200 bg-white p-5">
              <div className="text-sm text-slate-500">{s.label}</div>
              <div className="text-3xl font-semibold">{s.value}</div>
              <div className="text-xs text-success">↑ {s.trend}</div>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
}
