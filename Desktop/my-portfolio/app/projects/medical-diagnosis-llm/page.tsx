// app/projects/[slug]/page.tsx
"use client"
import Image from 'next/image';
import { motion } from 'framer-motion';

export default function ProjectPage({ params }: { params: { slug: string } }) {
  // Example project data - you would have this for each project
  const project = {
    title: "Medical Diagnosis LLM",
    unit: "NTU CS Lab",
    period: "Jun. 2024 - Present",
    summary: "Enhancing multidisciplinary medical diagnosis via LLM with RAG",
    technologies: ["LLM", "RAG", "Medical AI", "Python"],
    thumbnail: "/ntu-logo.png",
    challenges: [
      "Handling complex medical terminology",
      "Ensuring high accuracy across specialties",
      "Processing large medical datasets"
    ],
    keyFeatures: [
      "Multi-specialty diagnosis support",
      "Real-time medical reference integration",
      "Adaptive learning capabilities"
    ],
    results: "Improved diagnosis accuracy by 35% across multiple medical specialties"
  };

  return (
    <motion.div 
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="max-w-4xl mx-auto p-8"
    >
      {/* Hero Section */}
      <div className="mb-12">
        <motion.h1 
          initial={{ y: -20 }}
          animate={{ y: 0 }}
          className="text-4xl font-bold mb-4"
        >
          {project.title}
        </motion.h1>
        <p className="text-gray-600 text-lg mb-4">{project.period}</p>
        <div className="flex flex-wrap gap-2">
          {project.technologies.map((tech) => (
            <span key={tech} className="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm">
              {tech}
            </span>
          ))}
        </div>
      </div>

      {/* Project Overview */}
      <section className="mb-12">
        <h2 className="text-2xl font-semibold mb-4">Project Overview</h2>
        <div className="prose dark:prose-invert">
          <p>{project.summary}</p>
        </div>
      </section>

      {/* Key Features */}
      <motion.section 
        initial={{ y: 20, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ delay: 0.2 }}
        className="mb-12"
      >
        <h2 className="text-2xl font-semibold mb-4">Key Features</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {project.keyFeatures.map((feature, index) => (
            <div 
              key={index}
              className="p-4 bg-gray-50 dark:bg-gray-800 rounded-lg"
            >
              {feature}
            </div>
          ))}
        </div>
      </motion.section>

      {/* Challenges and Solutions */}
      <motion.section 
        initial={{ y: 20, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ delay: 0.4 }}
        className="mb-12"
      >
        <h2 className="text-2xl font-semibold mb-4">Challenges</h2>
        <div className="space-y-4">
          {project.challenges.map((challenge, index) => (
            <div 
              key={index}
              className="flex items-start gap-3"
            >
              <span className="text-blue-500">•</span>
              <p>{challenge}</p>
            </div>
          ))}
        </div>
      </motion.section>

      {/* Results */}
      <motion.section 
        initial={{ y: 20, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ delay: 0.6 }}
        className="mb-12"
      >
        <h2 className="text-2xl font-semibold mb-4">Results & Impact</h2>
        <div className="p-6 bg-green-50 dark:bg-green-900/20 rounded-lg">
          <p className="text-lg">{project.results}</p>
        </div>
      </motion.section>

      {/* Back Button */}
      <div className="mt-12">
        <button 
          onClick={() => window.history.back()}
          className="px-6 py-2 bg-gray-100 dark:bg-gray-800 rounded-lg hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors"
        >
          ← Back to Projects
        </button>
      </div>
    </motion.div>
  );
}