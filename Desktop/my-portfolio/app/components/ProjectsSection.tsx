// app/components/ProjectsSection.tsx
import Link from 'next/link';
import Image from 'next/image';

export default function ProjectsSection() {
  const projects = [
    {
      title: "Medical Diagnosis LLM",
      period: "Jun. 2024 - Present",
      description: "Enhancing multidisciplinary medical diagnosis via LLM with RAG. Fine-tuning models to assist doctors in diagnosing across various medical specialties.",
      slug: "medical-diagnosis-llm",
      tags: ["LLM", "RAG", "Medical AI"]
    },
    {
      title: "Medical Case Manager LLM",
      period: "Jun. 2024 - Present",
      description: "Implementing Retrieval-Augmented Generation technique to fine-tune LLM to the medical field. Optimizing TAIDE for Taiwan's cultural characteristics.",
      slug: "medical-case-manager",
      github: "https://github.com/2024-sinica-medLLM",
      tags: ["LLM", "RAG", "TAIDE"]
    },
    {
      title: "Scenic AI Window Manufacturing",
      period: "Feb. 2024 - Present",
      description: "Modeling and implementing optimization algorithms for production planning in aluminum doors and windows manufacturing.",
      slug: "scenic-ai-manufacturing",
      url: "https://2024-ntuim-project.github.io/docs/",
      github: "https://github.com/2024-ntuim-project/or-prototype",
      tags: ["Optimization", "Manufacturing", "AI"]
    },
    {
      title: "Election Result Prediction",
      period: "Sept. 2023 - Jan. 2024",
      description: "Predicting election results using GPT-3.5 for data labeling and analyzing public sentiment through social media.",
      slug: "election-prediction",
      url: "https://drive.google.com/file/d/1zB6CFNv4Bi_FpBc5mIVUM4I0Uo42GFYU/view?usp=sharing",
      tags: ["GPT-3.5", "Sentiment Analysis", "NLP"]
    }
  ];

  return (
    <div className="w-full max-w-3xl">
      <h2 className="text-2xl font-bold mb-6">Projects</h2>
      <div className="grid grid-cols-1 gap-6">
        {projects.map((project) => (
          <Link 
            href={project.url ? project.url : `/projects/${project.slug}`} 
            key={project.slug}
            className="block group"
          >
            <div className="border border-gray-200 dark:border-gray-700 rounded-lg p-6 transition-all duration-300 hover:shadow-lg hover:border-gray-300 dark:hover:border-gray-600">
              <div className="flex justify-between items-start mb-2">
                <h3 className="text-xl font-semibold group-hover:text-blue-600 dark:group-hover:text-blue-400">
                  {project.title}
                </h3>
                {project.github ? (
                    <a
                        href={project.github}
                        target="_blank"
                        rel="noopener noreferrer"
                        aria-label="GitHub Repository"
                        className="relative z-10 bg-white p-2 rounded-md shadow-md"
                    >
                        <Image 
                        src="/icons/github_logo.png"
                        alt="GitHub"
                        width={24}
                        height={24}
                        className="object-contain transition-transform transform hover:scale-110 hover:opacity-80"
                        />
                    </a>
                    ) : ( ""
                    )
                }
                <span className="text-sm text-gray-500">{project.period}</span>
              </div>
              <p className="text-gray-600 dark:text-gray-300 mb-4">
                {project.description}
              </p>
              <div className="flex flex-wrap gap-2">
                {project.tags.map((tag) => (
                  <span
                    key={tag}
                    className="px-3 py-1 bg-gray-100 dark:bg-gray-800 rounded-full text-sm"
                  >
                    {tag}
                  </span>
                ))}
              </div>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}