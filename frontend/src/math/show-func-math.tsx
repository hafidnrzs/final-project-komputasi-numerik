import { addStyles, StaticMathField } from "react-mathquill";

interface MathInputProps {
  initialLatex?: string;
}

addStyles();

const MathPreview = ({ initialLatex }: MathInputProps) => {
  // Tambahkan styles MathQuill

  return (
    <div className="flex flex-col items-center" contentEditable={false}>
      <StaticMathField className="text-2xl">
        {initialLatex || ""}
      </StaticMathField>
    </div>
  );
};
export default MathPreview;
