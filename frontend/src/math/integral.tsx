import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import React, { type FormEventHandler } from "react";
import { MathInput } from "./text-editor";
import axios from "axios";
import { Helmet } from "react-helmet";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import MathPreview from "./show-func-math";

interface SuccesProps {
  input_fungsi?: string;
  integral_fungsi?: string;
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
    h: "",
    a: "",
    b: "",
    N_segment: "",
    fungsi: "x^5 + \\frac{1}{2}x^3 - 4",
  });

  const handleSubmit: FormEventHandler = (e) => {
    e.preventDefault();
    const params = new URLSearchParams();
    params.append("metode", data.metode);
    params.append("fungsi_latex", data.fungsi);
    params.append("batas_bawah", data.a); // a = batas bawah
    params.append("batas_atas", data.b); // b = batas atas

    // Pengiriman parameter tergantung metode
    if (data.metode === "riemann") {
      params.append("h", data.h);
    } else if (data.metode === "trapezoida" || data.metode === "simpson") {
      params.append("N", data.N_segment); // gunakan N_segment dari state
    }

    axios
      .post("http://127.0.0.1:8000/integral/", params, {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      })
      .then((response) => {
        console.log(response.data.integral_fungsi);
        console.log("Response data:", response.data);
        if (response.data.hasil_analitik) {
          setResSucces({
            input_fungsi: response.data.input_fungsi,
            integral_fungsi: response.data.integral_fungsi,
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
        setResError({
          metode: data.metode || "Tidak Diketahui",
          message: error.response?.data?.detail || "Terjadi kesalahan",
        });
      });
  };

  return (
    <>
      <Helmet>
        <title>Komputasi Numerik - Integral</title>
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
          action={""}
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
                  <SelectItem value="riemann">Riemann</SelectItem>
                  <SelectItem value="trapezoida">Trapezoida</SelectItem>
                  <SelectItem value="simpson">Simpson</SelectItem>
                </SelectContent>
              </Select>
            </div>
          </div>
          {/* <div className="gap-2 grid grid-rows-1 grid-cols-12 w-full">
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
          </div> */}

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
                value={data.b}
                onChange={(e) => setData({ ...data, b: e.target.value })}
              />
            </div>
          </div>
          {/* {kerika simpson dan trapezoida h_step Hide} */}
          {data.metode === "riemann" && (
            <div className="gap-2 grid grid-rows-1 grid-cols-12 w-full">
              <div className="grid col-span-5">
                <Label htmlFor="h">Masukkan nilai h step</Label>
              </div>
              <div className="grid col-span-7">
                <Input
                  placeholder="Ukuran Langkah (step size)"
                  inputMode="numeric"
                  type="number"
                  id="h"
                  name="h"
                  className="w-full"
                  min={0.01}
                  autoComplete="off"
                  autoFocus
                  required={data.metode === "riemann"}
                  value={data.h}
                  onChange={(e) => setData({ ...data, h: e.target.value })}
                />
              </div>
            </div>
          )}

          {/* ketika reiman N_segment Hide */}
          {data.metode !== "riemann" && (
            <div className="gap-2 grid grid-rows-1 grid-cols-12 w-full">
              <div className="grid col-span-5">
                <Label htmlFor="N_segment">Masukkan nilai N segment</Label>
              </div>
              <div className="grid col-span-7">
                <Input
                  placeholder="Nilai Batas N segment"
                  inputMode="numeric"
                  type="number"
                  id="N_segment"
                  name="N_segment"
                  className="w-full"
                  min={1}
                  autoComplete="off"
                  autoFocus
                  required={
                    data.metode === "trapezoida" || data.metode === "simpson"
                  }
                  value={data.N_segment}
                  onChange={(e) =>
                    setData({ ...data, N_segment: e.target.value })
                  }
                />
              </div>
            </div>
          )}
          <div className="gap-2 flex-col w-full">
            <MathInput
              onChange={(value: string) => setData({ ...data, fungsi: value })}
              initialLatex={data.fungsi}
              submitButton={handleSubmit}
            />
          </div>
        </form>
        <div className="mt-8 border border-dashed rounded-2xl h-full p-4 flex flex-col gap-4 justify-start items-start w-full max-w-3xl mx-auto">
          <div className="flex flex-col gap-2 p-4">
            <h2 className="text-lg font-bold border-b-1">Hasil</h2>
            {resSucces ? (
              <>
                <div className="text-sm flex flex-col items-start space-y-2">
                  <span className="font-semibold">Fungsi</span>{" "}
                  <MathPreview initialLatex={resSucces.input_fungsi} />
                </div>
                <div className="text-sm flex flex-col items-start space-y-2">
                  <span className="font-semibold">Integral Fungsi </span>
                  <MathPreview initialLatex={resSucces?.integral_fungsi} />
                </div>
                <div className="text-sm flex flex-col items-start">
                  <span className="font-semibold mb-1">Metode</span>
                  <span className="capitalize">
                    {resSucces.metode.replace(/[_-]/g, " ")}
                  </span>
                </div>
                <div className="text-sm">
                  <span className="font-semibold">Hasil Numerik: </span>
                  {resSucces.hasil_numerik.toString()}
                </div>
                <div className="text-sm">
                  <span className="font-semibold">Hasil Analitik: </span>
                  {resSucces.hasil_analitik.toString()}
                </div>
                <div className="text-sm">
                  <span className="font-semibold">Error: </span>{" "}
                  {resSucces.error}
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
      {/* <div className="flex flex-col gap-4 rounded-xl p-4 w-full max-w-3xl mx-auto mt-8 border-dashed border-2 border-sidebar-border/70 dark:border-sidebar-border">
        <div className="items-center">
          <pre className="rounded bg-slate-300 p-4 font-mono text-sm whitespace-pre-wrap dark:bg-gray-800">
            {JSON.stringify(data, null, 2)}
          </pre>
        </div>
      </div> */}
    </>
  );
};

export default Turunan;
