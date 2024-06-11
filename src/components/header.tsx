import { HelpCircle, Orbit, User, User2 } from "lucide-react";
import { Separator } from "./ui/separator";
import { NavLink } from "./nav-link";
import Image from "next/image";
import Link from "next/link";

export function Header() {
  return (
    <header className="bg-secondary">
      <div className="flex items-center px-6 py-5 gap-4">
        <Link href="/" >
          <Image src="/pymaps.png" alt="logo" width={120} height={120} />
        </Link>

        <Separator orientation="vertical" className="h-6 bg-muted-foreground" />

        <div className="w-full flex items-center justify-between">
          <nav className="flex text-lg">
            <NavLink href="/">
              Main
            </NavLink>
            <NavLink href="#">
              LS
            </NavLink>
            <NavLink href="#">
              FFT
            </NavLink>
            <NavLink href="#"> 
              Wavelt
            </NavLink>
            <NavLink href="#">
              Diagram 
            </NavLink>
          </nav>
          <div className="border">
            <HelpCircle className="size-6" />
          </div>
        </div>
      </div>
    </header>
  )
}