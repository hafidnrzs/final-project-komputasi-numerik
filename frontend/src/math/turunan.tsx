import { Label } from "@/components/ui/label";
import React from "react";

const Turunan = (props: React.HTMLAttributes<HTMLDivElement>) => {
  return (
    <div {...props}>
      <form
        action=""
        className="border h-full p-4  flex flex-col gap-4 justify-start items-start w-full max-w-3xl mx-auto"
      >
        <div className="gap-2 grid">
          <Label htmlFor="x">
            Masukkan nilai <pre>X</pre>
          </Label>
        </div>
      </form>
    </div>
  );
};

export default Turunan;
