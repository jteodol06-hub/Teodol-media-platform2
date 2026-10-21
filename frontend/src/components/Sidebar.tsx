import Link from "next/link";
import { BarChart3, FileText, Folder, Home, Key, Plus, Settings, Users } from "lucide-react";

const items = [
  { href: "/dashboard", label: "Home", icon: Home },
  { href: "/jobs/new", label: "New Job", icon: Plus },
  { href: "/projects", label: "Projects", icon: Folder },
  { href: "/files", label: "Files", icon: FileText },
  { href: "/team", label: "Team", icon: Users },
  { href: "/api-keys", label: "API Keys", icon: Key },
  { href: "/analytics", label: "Analytics", icon: BarChart3 },
];

export default function Sidebar({ active = "/dashboard" }: { active?: string }) {
  return (
    <aside className="flex w-56 shrink-0 flex-col bg-navy p-4 text-white">
      <div className="mb-6 px-2 text-lg font-semibold">Teodol</div>
      <nav className="flex flex-1 flex-col gap-1">
        {items.map(({ href, label, icon: Icon }) => (
          <Link
            key={href}
            href={href}
            className={`flex items-center gap-3 rounded-lg px-3 py-2 text-sm ${
              active === href ? "bg-navy-slate text-white" : "text-slate-300 hover:bg-navy-slate"
            }`}
          >
            <Icon size={17} className={active === href ? "text-brand" : ""} />
            {label}
          </Link>
        ))}
      </nav>
      <Link href="/settings" className="flex items-center gap-3 px-3 py-2 text-sm text-slate-300">
        <Settings size={17} /> Settings
      </Link>
    </aside>
  );
}
