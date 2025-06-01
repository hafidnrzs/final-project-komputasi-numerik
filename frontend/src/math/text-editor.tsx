import { useState, useRef, useEffect } from "react";
import "mathlive";
import { MathfieldElement } from "mathlive";
import "./math.css"; // We'll create this CSS file next

export default function MathKeyboard() {
  const [value, setValue] = useState("");
  const mfRef = useRef<MathfieldElement | null>(null);

  useEffect(() => {
    console.log("value changed:", value);
  }, [value]);

  // Initialize mathfield
  useEffect(() => {
    const mf = new MathfieldElement();
    mf.value = value;
    mf.addEventListener("input", (evt) => {
      setValue((evt.target as MathfieldElement).value);
    });
    mfRef.current = mf;
    document.getElementById("mathfield-container")?.appendChild(mf);
    return () => {
      document.getElementById("mathfield-container")?.removeChild(mf);
    };
  }, []);

  // Insert symbol into mathfield
  const insertSymbol = (symbol: string) => {
    if (mfRef.current) {
      mfRef.current.insert(symbol, { focus: true });
    }
  };

  // Special operations
  const insertExponent = () => {
    if (mfRef.current) {
      mfRef.current.executeCommand("moveToSuperscript");
    }
  };

  const insertFraction = () => {
    if (mfRef.current) {
      mfRef.current.executeCommand("insertFraction");
    }
  };

  const insertSquareRoot = () => {
    if (mfRef.current) {
      mfRef.current.insert("\\sqrt{}");
      mfRef.current.executeCommand("moveToNextPlaceholder");
    }
  };

  const insertNthRoot = () => {
    if (mfRef.current) {
      mfRef.current.insert("\\sqrt[]{}");
      mfRef.current.executeCommand("moveToPreviousPlaceholder");
    }
  };

  return (
    <div className="math-input-container">
      {/* Math input field */}
      <div id="mathfield-container" className="mathfield" />

      {/* Basic keyboard */}
      <div className="keyboard-section">
        <h4>Basic</h4>
        <div className="keyboard-row">
          {["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"].map((char) => (
            <button key={char} onClick={() => insertSymbol(char)}>
              {char}
            </button>
          ))}
        </div>
        <div className="keyboard-row">
          {["k", "l", "m", "n", "o", "p", "q", "r", "s", "t"].map((char) => (
            <button key={char} onClick={() => insertSymbol(char)}>
              {char}
            </button>
          ))}
        </div>
        <div className="keyboard-row">
          {["u", "v", "w", "x", "y", "z"].map((char) => (
            <button key={char} onClick={() => insertSymbol(char)}>
              {char}
            </button>
          ))}
        </div>
      </div>

      {/* Operators */}
      <div className="keyboard-section">
        <h4>Operators</h4>
        <div className="keyboard-row">
          {["+", "-", "\\cdot", "=", "\\ge", "\\le", "(", ")", "|", "|"].map(
            (op) => (
              <button key={op} onClick={() => insertSymbol(op)}>
                {op.startsWith("\\") ? op.slice(1) : op}
              </button>
            )
          )}
        </div>
      </div>

      {/* Exponents & Fractions */}
      <div className="keyboard-section">
        <h4>Exponents & Fractions</h4>
        <div className="keyboard-row">
          <button onClick={insertExponent}>
            x<sup>n</sup>
          </button>
          <button onClick={() => insertSymbol("^{}")}>
            x<sup>□</sup>
          </button>
          <button onClick={() => insertSymbol("e^{}")}>
            e<sup>□</sup>
          </button>
          <button onClick={insertFraction}>
            <span className="fraction-button">a/b</span>
          </button>
          <button onClick={insertSquareRoot}>√□</button>
          <button onClick={insertNthRoot}>ⁿ√□</button>
        </div>
      </div>

      {/* Functions */}
      <div className="keyboard-section">
        <h4>Functions</h4>
        <div className="keyboard-row">
          {["\\sin", "\\cos", "\\tan", "\\cot", "\\sec", "\\csc"].map((fn) => (
            <button key={fn} onClick={() => insertSymbol(fn)}>
              {fn.slice(1)}
            </button>
          ))}
        </div>
        <div className="keyboard-row">
          {["\\log", "\\ln", "e^", "10^", "\\pi", "\\theta"].map((fn) => (
            <button key={fn} onClick={() => insertSymbol(fn)}>
              {fn.startsWith("\\") ? fn.slice(1) : fn}
            </button>
          ))}
        </div>
      </div>

      {/* Calculus */}
      <div className="keyboard-section">
        <h4>Calculus</h4>
        <div className="keyboard-row">
          {["\\frac{d}{dx}", "\\int", "\\sum", "\\prod", "\\lim"].map(
            (calc) => (
              <button key={calc} onClick={() => insertSymbol(calc)}>
                {calc.startsWith("\\") ? calc.slice(1) : calc}
              </button>
            )
          )}
        </div>
        <div className="keyboard-row">
          {["\\partial", "\\nabla", "\\infty"].map((calc) => (
            <button key={calc} onClick={() => insertSymbol(calc)}>
              {calc.slice(1)}
            </button>
          ))}
        </div>
      </div>

      {/* Actions */}
      <div className="keyboard-section">
        <h4>Actions</h4>
        <div className="keyboard-row actions-row">
          <button onClick={() => mfRef.current?.executeCommand("simplify")}>
            Simplify
          </button>
          <button onClick={() => mfRef.current?.executeCommand("solve")}>
            Solve for
          </button>
          <button onClick={() => insertSymbol("^{-1}")}>Inverse</button>
          <button onClick={() => mfRef.current?.executeCommand("tangentLine")}>
            Tangent Line
          </button>
        </div>
      </div>
    </div>
  );
}
