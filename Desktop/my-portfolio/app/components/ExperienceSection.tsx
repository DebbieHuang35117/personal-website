// app/components/ExperienceSection.tsx
import Link from 'next/link';

export default function ExperienceSection() {
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
      tags: ["LLM", "RAG", "TAIDE"]
    },
    {
      title: "Scenic AI Window Manufacturing",
      period: "Feb. 2024 - Present",
      description: "Modeling and implementing optimization algorithms for production planning in aluminum doors and windows manufacturing.",
      slug: "scenic-ai-manufacturing",
      tags: ["Optimization", "Manufacturing", "AI"]
    },
    {
      title: "Election Result Prediction",
      period: "Sept. 2023 - Jan. 2024",
      description: "Predicting election results using GPT-3.5 for data labeling and analyzing public sentiment through social media.",
      slug: "election-prediction",
      tags: ["GPT-3.5", "Sentiment Analysis", "NLP"]
    }
  ];

  return (
    <div className="w-full max-w-4xl">
      <h2 className="text-2xl font-bold mb-6">Experience and Activities</h2>
      <div className="space-y-6">
  {/* Experience Block */}
  <div className="bg-white shadow-lg rounded-xl p-6 border border-gray-200">
    <h3 className="text-lg font-bold text-gray-900">Business Development Director, GLO</h3>
    <p className="text-gray-600"></p>
    <span className="text-sm text-gray-500"></span>
  </div>

  {/* Another Experience Block */}
  <div className="bg-white shadow-lg rounded-xl p-6 border border-gray-200">
    <h3 className="text-lg font-bold text-gray-900">Marketing Strategy Director, GLO</h3>
    <p className="text-gray-600">Led social media strategy and content creation, increasing engagement by 40%.</p>
    <span className="text-sm text-gray-500">Jan 2024 - Present</span>
  </div>
</div>
    </div>
  );
}