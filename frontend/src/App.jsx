import {
  BrowserRouter,
  Routes,
  Route,
  Link
} from "react-router-dom";

import Home from "./pages/Home";
import UploadResume from "./pages/UploadResume";

function App() {

  return (

    <BrowserRouter>

      <nav className="bg-blue-600 text-white p-4 flex gap-4">

        <Link to="/">
          Home
        </Link>

        <Link to="/upload">
          Upload Resume
        </Link>

      </nav>

      <Routes>

        <Route
          path="/"
          element={<Home />}
        />

        <Route
          path="/upload"
          element={<UploadResume />}
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;