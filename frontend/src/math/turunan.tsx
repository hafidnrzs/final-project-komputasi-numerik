import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import React from "react";
import { MathInput } from "./text-editor";
import { Helmet } from "react-helmet";

const Turunan = (props: React.HTMLAttributes<HTMLDivElement>) => {
  const [data, setData] = React.useState({
    x: "",
    h: "",
    a: "",
    b: "",
    function: "x^5 + \\frac{1}{2}x^3 - 4",
  });

  const handleSubmit = () => {
    // Handle form submission logic here
    console.log("Form submitted with data:", data);
  };

  return (
    <>
      <Helmet>
        <title>Komputasi Numerik - Turunan</title>
        <link
          rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/mathlive/0.105.3/mathlive-fonts.css"
        />
        <link
          rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/mathlive/0.105.3/mathlive.css"
        />
      </Helmet>
      <div {...props}>
        <form
          onSubmit={handleSubmit}
          className="border border-dashed rounded-2xl h-full p-4 flex flex-col gap-4 justify-start items-start w-full max-w-3xl mx-auto"
        >
          <div className="gap-2 grid grid-rows-1 grid-cols-12 w-full">
            <div className="grid col-span-5">
              <Label htmlFor="x">
                Masukkan nilai <pre>X</pre>
              </Label>
            </div>
            <div className="grid col-span-7">
              <Input
                inputMode="numeric"
                type="number"
                id="x"
                name="x"
                className="w-full"
                autoComplete="off"
                autoFocus
                required
                placeholder="nilai x"
                value={data.x}
                onChange={(e) => setData({ ...data, x: e.target.value })}
              />
            </div>
          </div>
          <div className="gap-2 grid grid-rows-1 grid-cols-12 w-full">
            <div className="grid col-span-5">
              <Label htmlFor="h">
                Masukkan nilai <pre>h</pre>
              </Label>
            </div>
            <div className="grid col-span-7">
              <Input
                placeholder="Ukuran Langkah (step size)"
                inputMode="numeric"
                type="number"
                id="h"
                name="h"
                className="w-full"
                autoComplete="off"
                autoFocus
                required
                value={data.h}
                onChange={(e) => setData({ ...data, h: e.target.value })}
              />
            </div>
          </div>
          <div className="gap-2 grid grid-rows-1 grid-cols-12 w-full">
            <div className="grid col-span-5">
              <Label htmlFor="a">Masukkan nilai Batas Atas</Label>
            </div>
            <div className="grid col-span-7">
              <Input
                placeholder="Nilai Batas Atas (a)"
                inputMode="numeric"
                type="number"
                id="a"
                name="a"
                className="w-full"
                autoComplete="off"
                autoFocus
                required
                value={data.a}
                onChange={(e) => setData({ ...data, a: e.target.value })}
              />
            </div>
          </div>
          <div className="gap-2 grid grid-rows-1 grid-cols-12 w-full">
            <div className="grid col-span-5">
              <Label htmlFor="b">Masukkan nilai Batas Bawah</Label>
            </div>
            <div className="grid col-span-7">
              <Input
                placeholder="Nilai Batas Bawah (b)"
                inputMode="numeric"
                type="number"
                id="b"
                name="b"
                className="w-full"
                autoComplete="off"
                autoFocus
                required
                value={data.b}
                onChange={(e) => setData({ ...data, b: e.target.value })}
              />
            </div>
          </div>
          <div className="gap-2 flex-col w-full">
            <MathInput
              onChange={(value: string) =>
                setData({ ...data, function: value })
              }
            />
          </div>
        </form>
      </div>
    </>
  );
};

export default Turunan;
