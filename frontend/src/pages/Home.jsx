import { Link } from "react-router-dom";

export default function Home() {

  const cards = [
    {
      title: "Upload Resume",
      path: "/upload"
    },
    {
      title: "Skill Gap Analysis",
      path: "/skill-gap"
    },
    {
      title: "Learning Roadmap",
      path: "/roadmap"
    },
    {
      title: "Career Chat",
      path: "/chat"
    }
  ];

  return (
    <div className="p-8">

      <h1 className="text-4xl font-bold mb-8">
        AI Career Copilot
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

        {cards.map((card) => (

          <Link
            key={card.title}
            to={card.path}
          >
            <div className="border rounded-xl shadow-lg p-8 hover:shadow-2xl transition">

              <h2 className="text-2xl font-bold">

                {card.title}

              </h2>

            </div>

          </Link>

        ))}

      </div>

    </div>
  );
}