import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import React, { type FormEventHandler } from "react";
import { MathInput } from "./text-editor";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import axios from "axios";
import { Helmet } from "react-helmet";

interface SuccesProps {
  metode: string;
  hasil_analitik: string | number;
  hasil_numerik: string | number;
  error: string | null;
}

interface ErrorProps {
  metode: string;
  message: string;
}

const Turunan = (props: React.HTMLAttributes<HTMLDivElement>) => {
  const [resSucces, setResSucces] = React.useState<SuccesProps | null>(null);
  const [resError, setResError] = React.useState<ErrorProps | null>(null);
  const [data, setData] = React.useState({
    metode: "",
    x: "",
    h_step: "",
    fungsi_latex: "x^5 + \\frac{1}{2}x^3 - 4",
  });

  const handleSubmit: FormEventHandler = (e) => {
    e.preventDefault();
    const escapedLatex = data.fungsi_latex.replace(/\\\\/g, "\\");
    // Buat params URLSearchParams
    const params = new URLSearchParams();
    params.append("metode", data.metode);
    params.append("x", data.x); // sudah string, backend akan menerima float
    params.append("h", data.h_step); // sudah string, backend akan menerima float
    params.append("fungsi_latex", escapedLatex);

    axios
      .post("http://127.0.0.1:8000/turunan/", params, {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      })
      .then((response) => {
        console.log("Response data:", response);
        if (response.data.hasil_analitik) {
          setResSucces({
            metode: response.data.metode,
            hasil_analitik: response.data.hasil_analitik,
            hasil_numerik: response.data.hasil_numerik,
            error: response.data.error_relatif,
          });
          setResError(null);
        } else if (response.data.message) {
          setResSucces(null);
          setResError({
            metode: response.data.metode,
            message: response.data.message,
          });
        }
      })
      .catch((error) => {
        console.error("Error submitting form:", error);
        setResError({
          metode: "Selisih Maju",
          message: error.response?.data?.detail || "Terjadi kesalahan",
        });
      });
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
          className="border border-dashed rounded-2xl h-full p-4 flex flex-col gap-4 justify-start items-start w-full max-w-3xl mx-auto"
          onSubmit={handleSubmit}
        >
          <div className="gap-2 grid grid-rows-1 grid-cols-12 w-full">
            <div className="grid col-span-5">
              <Label htmlFor="x">Masukkan metode</Label>
            </div>
            <div className="grid col-span-7">
              <Select
                value={data.metode}
                onValueChange={(value) => setData({ ...data, metode: value })}
                required
              >
                <SelectTrigger className="w-full">
                  <SelectValue placeholder="Pilih metode" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="selisih-maju">Selisih Maju</SelectItem>
                  <SelectItem value="selisih_tengahan">
                    Selisih Tengahan
                  </SelectItem>
                  <SelectItem value="selisih-mundur">Selisih Mundur</SelectItem>
                </SelectContent>
              </Select>
            </div>
          </div>
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
              <Label htmlFor="h_step">
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
                value={data.h_step}
                onChange={(e) => setData({ ...data, h_step: e.target.value })}
              />
            </div>
          </div>
          <div className="gap-2 flex-col w-full">
            <MathInput
              onChange={(value: string) =>
                setData({ ...data, fungsi_latex: value })
              }
              initialLatex={data.fungsi_latex}
              submitButton={handleSubmit}
            />
          </div>
        </form>
        <div className="mt-12 border border-dashed rounded-2xl h-full p-4 flex flex-col gap-4 justify-start items-start w-full max-w-3xl mx-auto">
          <div className="flex flex-col gap-2 p-4">
            <h2 className="text-lg font-semibold">Hasil:</h2>
            {resSucces ? (
              <>
                <div className="text-sm">
                  Metode: <strong>{resSucces.metode}</strong>
                </div>
                <div className="text-sm">
                  Error: <strong>{resSucces.error}</strong>
                </div>
                <div className="text-sm">
                  Hasil Analitik:{" "}
                  <strong>{resSucces.hasil_analitik.toString()}</strong>
                </div>
                <div className="text-sm">
                  Hasil Numerik:{" "}
                  <strong>{resSucces.hasil_numerik.toString()}</strong>
                </div>
              </>
            ) : null}
            {resError ? (
              <div className="text-sm text-red-500">
                <strong>Error:</strong> {resError.message}
              </div>
            ) : null}
            {!resSucces && !resError && (
              <p className="text-sm text-muted-foreground">
                Hasil turunan akan ditampilkan di sini setelah Anda mengisi
                semua input dan mengirimkan formulir.
              </p>
            )}
          </div>
        </div>
      </div>
      <div className="flex flex-col gap-4 rounded-xl p-4 w-full max-w-3xl mx-auto mt-8 border-dashed border-2 border-sidebar-border/70 dark:border-sidebar-border">
        <div className="items-center">
          <pre className="rounded bg-slate-300 p-4 font-mono text-sm whitespace-pre-wrap dark:bg-gray-800">
            {JSON.stringify(data, null, 2)}
          </pre>
        </div>
      </div>
    </>
  );
};

export default Turunan;
