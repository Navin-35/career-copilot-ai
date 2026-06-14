import { Link } from "react-router-dom";

export default function Navbar() {

  return (
    <div className="bg-blue-600 text-white p-4 flex gap-6">

      <Link to="/">Home</Link>

      <Link to="/upload">
        Upload Resume
      </Link>

      <Link to="/skill-gap">
        Skill Gap
      </Link>

      <Link to="/roadmap">
        Roadmap
      </Link>

      <Link to="/chat">
        Career Chat
      </Link>

    </div>
  );
}