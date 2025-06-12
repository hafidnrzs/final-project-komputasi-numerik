/* eslint-disable no-useless-escape */
/* eslint-disable @typescript-eslint/no-explicit-any */
import { useState, useRef, useEffect } from "react";
import { addStyles, EditableMathField } from "react-mathquill";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible";

// Tambahkan styles MathQuill
addStyles();

interface MathInputProps {
  onChange?: (latex: string) => void;
  initialLatex?: string;
  submitButton?: React.EventHandler<React.SyntheticEvent>;
}

const MathInput = ({
  onChange,
  initialLatex,
  submitButton,
}: MathInputProps) => {
  const [latex, setLatex] = useState<string>(
    initialLatex || "\\frac{1}{2}x^2 + 3x + 4"
  );
  const [isFocused, setIsFocused] = useState<boolean>(false);
  const mathFieldRef = useRef<any>(null);
  const wrapperRef = useRef<HTMLDivElement>(null);

  // Filter untuk hanya mengizinkan pecahan dan pangkat
  const filterMathInput = (latexStr: string) => {
    // Hanya izinkan karakter tertentu: angka, huruf, +, -, *, /, (, ), ^, \, {, }
    const filtered = latexStr.replace(
      /[^0-9a-zA-Z\+\-\*\/\(\)\^\{\}\\=\.\,]/g,
      ""
    );

    // Validasi struktur dasar pecahan dan pangkat
    const hasValidFractions = filtered.split("\\frac").length <= 3; // Maksimal 2 pecahan
    const hasValidExponents = filtered.split("^").length <= 3; // Maksimal 2 pangkat

    return hasValidFractions && hasValidExponents ? filtered : latex;
  };

  const handleChange = (mathField: any) => {
    const newLatex = mathField.latex();
    const filteredLatex = filterMathInput(newLatex);
    setLatex(filteredLatex);
    if (onChange) {
      onChange(filteredLatex);
    }
  };

  // Fokus ke MathQuill ketika wrapper diklik
  const handleWrapperClick = () => {
    if (mathFieldRef.current) {
      mathFieldRef.current.focus();
    }
  };

  useEffect(() => {
    handleChange(mathFieldRef.current);
  }, [initialLatex, mathFieldRef]);

  return (
    <div className="space-y-4">
      <div className="flex flex-row gap-2 mb-2">
        <Button
          size={"icon"}
          variant={"outline"}
          onClick={() => {
            if (mathFieldRef.current) {
              const currentLatex = mathFieldRef.current.latex();
              // Tambahkan pangkat jika belum ada
              mathFieldRef.current.latex(currentLatex + "^n");
            }
          }}
          type="button"
        >
          <span className="text-lg">x</span>
          <sup className="text-xs align-super">n</sup>
        </Button>
        <Button
          size={"icon"}
          variant={"outline"}
          onClick={() => {
            if (mathFieldRef.current) {
              const currentLatex = mathFieldRef.current.latex();
              // Tambahkan pecahan jika belum ada
              mathFieldRef.current.latex(currentLatex + "\\frac{1}{2}"); // Contoh pecahan
            }
          }}
          type="button"
        >
          <div className="flex flex-col items-center justify-center">
            {/* Pembilang (angka atas) */}
            <div className="text-center text-sm">1</div>

            {/* Garis pecahan */}
            <div className="w-4 border-t border-black"></div>

            {/* Penyebut (angka bawah) */}
            <div className="text-center text-sm">2</div>
          </div>
        </Button>
      </div>
      <div
        ref={wrapperRef}
        onClick={handleWrapperClick}
        className={`p-2 border rounded-md ${
          isFocused ? "ring-2 ring-primary" : ""
        }`}
      >
        <EditableMathField
          autoFocus={true}
          latex={latex}
          onChange={(e) => {
            setLatex(e.latex());
            handleChange(e);
          }}
          mathquillDidMount={(mathField) => {
            mathFieldRef.current = mathField;
          }}
          onFocus={() => setIsFocused(true)}
          onBlur={() => setIsFocused(false)}
          config={{
            // Hanya izinkan perintah pecahan dan pangkat
            restrictMismatchedBrackets: true,
          }}
        />
      </div>

      {/* Collapsible Shadcn Textarea untuk tampilan/edit alternatif */}
      <Collapsible>
        <CollapsibleTrigger asChild>
          <Button
            variant="outline"
            className="mb-2 w-full font-normal hover:cursor-pointer"
            type="button"
          >
            Tampilkan/Sembunyikan Teks Latex
          </Button>
        </CollapsibleTrigger>
        <CollapsibleContent>
          <div className="text-sm text-muted-foreground">
            <p>Format yang didukung:</p>
            <ul className="list-disc pl-5">
              <li>
                Pecahan:{" "}
                <code className="bg-gray-200 text-slate-500 rounded px-1">
                  {"\\frac{1}{2}"}
                </code>
              </li>
              <li>
                Pangkat:{" "}
                <code className="bg-gray-200 text-slate-500 rounded px-1">
                  {"x^2"}
                </code>
              </li>
            </ul>
          </div>
          <Textarea
            value={latex}
            onChange={(e) => {
              const filtered = filterMathInput(e.target.value);
              setLatex(filtered);
              if (mathFieldRef.current) {
                mathFieldRef.current.latex(filtered);
              }
            }}
            placeholder="Ketik ekspresi matematika (hanya pecahan dan pangkat)"
            className="font-mono h-20 mt-2"
          />
        </CollapsibleContent>
      </Collapsible>

      <div className="text-sm text-muted-foreground justify-end flex-row flex">
        <div className="">
          <Button
            variant={"default"}
            type="button"
            onClick={(e) => {
              if (submitButton) submitButton(e);
            }}
          >
            Hitung
          </Button>
        </div>
      </div>
    </div>
  );
};

export { MathInput };
