import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./Home";
import { Helmet } from "react-helmet";
import Turunan from "./math/turunan";
import Integrasi from "./math/integral";
import { Navbar1 } from "./components/navbar1";

const App = () => {
  return (
    <>
      <Helmet>
        <title>Komputasi Numerik</title>
        <meta
          name="description"
          content="Aplikasi Komputasi Numerik untuk menghitung turunan dan integral numerik."
        />
      </Helmet>
      <Router>
        <div className="w-full flex items-center justify-center flex-col">
          <Navbar1 />

          <Routes>
            <Route
              path="/"
              element={
                <Home className="flex flex-col w-full max-w-7xl mx-auto items-center justify-center" />
              }
            />
            <Route
              path="/turunan"
              element={
                <Turunan className="flex flex-col w-full max-w-7xl mx-auto items-center justify-center" />
              }
            />
            <Route
              path="/integrasi"
              element={
                <Integrasi className="flex flex-col w-full max-w-7xl mx-auto items-center justify-center" />
              }
            />
            <Route
              path="*"
              element={
                <NotFound className="flex flex-col w-full max-w-7xl mx-auto items-center justify-center" />
              }
            />
          </Routes>
        </div>
      </Router>
    </>
  );
};

const NotFound = (props: React.HTMLAttributes<HTMLDivElement>) => {
  return (
    <div {...props}>
      <h1>404 - Page Not Found</h1>
      <p>The page you are looking for does not exist.</p>
    </div>
  );
};

export default App;
