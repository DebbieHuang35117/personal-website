// app/skills/[slug]/page.tsx
interface SkillPageProps {
    params: { slug: string };
  }
  
  const skillDetails = {
    'communication-skills': {
      title: 'Communication Skills',
      overview: 'Effective communication is crucial in both professional and personal contexts.',
      keyExperiences: [
        'Leadership roles in Google Development Student Club',
        'Public Relations in Programming Competitions',
        'Teaching Assistant experiences'
      ],
      relevantProjects: [
        'Medical Diagnosis LLM Project',
        'Election Result Prediction'
      ]
    },
    'public-speaking': {
      title: 'Public Speaking',
      overview: 'Demonstrated ability to present complex ideas clearly and confidently.',
      achievements: [
        '1st Place in NTU English Debate',
        'Presentations in various academic and professional settings'
      ]
    },
    'project-management': {
      title: 'Project Management',
      overview: 'Experienced in leading and coordinating complex projects.',
      keyProjects: [
        'Scenic AI Window Manufacturing Planning',
        'Medical Case Manager LLM Project'
      ]
    }
    // Add more skill details as needed
  };
  
  export default function SkillPage({ params }: SkillPageProps) {
    const skill = skillDetails[params.slug as keyof typeof skillDetails];
  
    if (!skill) {
      return <div className="text-center text-2xl mt-10">Skill not found</div>;
    }
  
    return (
      <div className="max-w-4xl mx-auto p-8">
        <h1 className="text-3xl font-bold mb-6">{skill.title}</h1>
        
        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">Overview</h2>
          <p className="text-gray-600 dark:text-gray-300">{skill.overview}</p>
        </section>
  
        {skill.keyExperiences && (
          <section className="mb-8">
            <h2 className="text-2xl font-semibold mb-4">Key Experiences</h2>
            <ul className="list-disc list-inside space-y-2">
              {skill.keyExperiences.map((exp, index) => (
                <li key={index} className="text-gray-700 dark:text-gray-300">
                  {exp}
                </li>
              ))}
            </ul>
          </section>
        )}
  
        {skill.relevantProjects && (
          <section className="mb-8">
            <h2 className="text-2xl font-semibold mb-4">Relevant Projects</h2>
            <ul className="list-disc list-inside space-y-2">
              {skill.relevantProjects.map((project, index) => (
                <li key={index} className="text-gray-700 dark:text-gray-300">
                  {project}
                </li>
              ))}
            </ul>
          </section>
        )}
      </div>
    );
  }
  
  // Generate static params for build-time optimization
  export async function generateStaticParams() {
    return Object.keys(skillDetails).map((slug) => ({
      slug,
    }));
  }