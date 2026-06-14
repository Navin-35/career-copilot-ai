import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import Navbar from "./components/Navbar";

import Home from "./pages/Home";
import UploadResume from "./pages/UploadResume";
import SkillGap from "./pages/SkillGap";
import Roadmap from "./pages/Roadmap";
import CareerChat from "./pages/CareerChat";

function App() {
  return (
    <BrowserRouter>

      <Navbar />

      <Routes>

        <Route
          path="/"
          element={<Home />}
        />

        <Route
          path="/upload"
          element={<UploadResume />}
        />

        <Route
          path="/skill-gap"
          element={<SkillGap />}
        />

        <Route
          path="/roadmap"
          element={<Roadmap />}
        />

        <Route
          path="/chat"
          element={<CareerChat />}
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;