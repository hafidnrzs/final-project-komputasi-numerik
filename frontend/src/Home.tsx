import React from "react";
import { Link } from "react-router-dom";
import { Button } from "./components/ui/button";

const Home = (props: React.HTMLAttributes<HTMLDivElement>) => {
  return (
    <div {...props} className="container mx-auto px-4 py-8">
      <div className="max-w-4xl mx-auto text-center space-y-6">
        <h1 className="text-4xl font-bold">Komputasi Numerik</h1>
        <p className="text-xl text-muted-foreground">
          Metode Numerik untuk Turunan dan Integrasi
        </p>

        <div className="grid md:grid-cols-2 gap-8 mt-12">
          <div className="p-6 border rounded-lg shadow-sm hover:shadow-md transition-shadow">
            <h2 className="text-2xl font-semibold mb-4">Turunan Numerik</h2>
            <p className="text-muted-foreground mb-6 text-left">
              Hitung turunan fungsi menggunakan berbagai metode numerik seperti:
              <ul className="list-disc list-inside mt-2 text-left">
                <li>Metode Selisih Maju</li>
                <li>Metode Selisih Mundur</li>
                <li>Metode Selisih Tengah</li>
              </ul>
            </p>
            <Link to="/turunan">
              <Button className="w-full">Coba Turunan</Button>
            </Link>
          </div>

          <div className="p-6 border rounded-lg shadow-sm hover:shadow-md transition-shadow">
            <h2 className="text-2xl font-semibold mb-4">Integrasi Numerik</h2>
            <p className="text-muted-foreground mb-6 text-left">
              Hitung integral fungsi menggunakan berbagai metode numerik
              seperti:
              <ul className="list-disc list-inside mt-2 text-left">
                <li>Metode Riemann</li>
                <li>Metode Trapezoida</li>
                <li>Metode Simpson</li>
              </ul>
            </p>
            <Link to="/integrasi">
              <Button className="w-full">Coba Integrasi</Button>
            </Link>
          </div>
        </div>

        <div className="mt-12 p-6 bg-muted/50 rounded-lg">
          <h2 className="text-2xl font-semibold mb-4">Tentang Aplikasi</h2>
          <p className="text-muted-foreground">
            Aplikasi ini membantu Anda menyelesaikan perhitungan turunan dan
            integrasi secara numerik. Masukkan fungsi matematika dalam format
            LaTeX, pilih metode yang diinginkan, dan dapatkan hasil perhitungan
            beserta analisis errornya.
          </p>

          <div className="flex justify-center items-center gap-2 mt-4">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              className="lucide lucide-github-icon lucide-github"
            >
              <path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4" />
              <path d="M9 18c-4.51 2-5-2-7-2" />
            </svg>
            <a
              href="https://github.com/hafidnrzs/final-project-komputasi-numerik"
              target="_blank"
              rel="noopener noreferrer"
              className="hover:underline"
            >
              Lihat di GitHub
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
