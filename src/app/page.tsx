import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Search } from "lucide-react";

export default function Home() {
  return (
    <main className="flex-1 p-4 w-full space-y-4">
      <div className="flex gap-4 items-center max-w-sm">
        <div className="flex items-center gap-1">
            <Input id="id" placeholder="id" className="rounded-r-none" />
            <Button size="icon" className="rounded-s-none ring-0 foc">
              <Search />
            </Button>
        </div>
        <Select defaultValue="sec">
          <SelectTrigger>
            <SelectValue />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="sec">Sec</SelectItem>
          </SelectContent>
        </Select>
      </div>
      <div className="w-full">
        <div className="flex items-center justify-between px-4 py-2">
          <span>(1/700)</span>
          <span>ID: 123</span>
          <span>Setor: 25</span>
          <span>(2/3)</span>
        </div>
        <canvas className="border w-full h-96"></canvas>
      </div>
    </main>
  )
}
