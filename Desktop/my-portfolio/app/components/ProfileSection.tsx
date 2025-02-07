// app/components/ProfileSection.tsx
import Image from "next/image";
import Link from 'next/link'

export default function ProfileSection() {
  return (
    <div className="flex flex-col items-center gap-8 max-w-3xl">
      
      {/* Bio Section */}
      <div className="flex items-center gap-6 p-0.1 rounded-lg mt-4">
        <Image
            className="rounded-full object-cover"
            src="/Debbie Huang.jpg"
            alt="Debbie Huang's profile photo"
            width={180}
            height={180}
            priority
        />
        <div> {/* Change the size of space between each paragraph */}
        <h2 className="text-2xl">🌟 About Me</h2>
        <br />
        <p className="text-base">
          I am an Information Management major with a Computer Science minor at National Taiwan University, 
          combining technical expertise with leadership experience. Currently involved in cutting-edge projects 
          in <span className="font-bold">medical AI</span> and <span className="font-bold">manufacturing optimization</span>.<br /> <br />

          As a <span className="font-bold">Business Development Director</span> at Global Leadership Organization and former <span className="font-bold">Academic Director</span> at 
          Google Development Student Club, my self-position mission is that <br /> <span className="italic font-bold">I hope bridge the gap between technology and business solutions</span>.
        </p>
        </div>
      </div>

      {/* Education */}
      <div className="w-full">
        <h3 className="font-semibold text-2xl mb-3">Education</h3>
        <div className="flex items-center gap-6 bg-gray-50 dark:bg-gray-800 p-4 rounded-lg">
          <Image
            src="/ntu-logo.png"  // Make sure to place your NTU logo in the public folder
            alt="National Taiwan University Logo"
            width={75}
            height={75}
            className="object-contain"
          />
          <div>
            <p className="font-medium">BS in National Taiwan University</p>
            <p className="text-gray-600">Information Management Major, Computer Science Minor<br /> Enrolled in Intelligence Medicine Program</p>
            <p className="text-sm text-gray-500">Academic Ranking 1st Place in 2022</p>
          </div>
        </div>
        <div className="flex items-center gap-6 bg-gray-50 dark:bg-gray-800 p-4 rounded-lg mt-4">
        <Image
            src="/hku-logo.png"  // Make sure to place your NTU logo in the public folder
            alt="The University of Hong Kong Logo"
            width={75}
            height={75}
            className="object-contain"
          />
          <div>
            <p className="font-medium">The University of Hong Kong</p>
            <p className="text-gray-600">Exchange Student Program</p>
            <p className="text-sm text-gray-500">GPA: ? / 4.0</p>
          </div>
        </div>
      </div>

      {/* Technical Skills */}
      <div className="w-full">
        <h3 className="font-semibold text-2xl mb-3">Technical Skills</h3>
        <div className="space-y-3">
            <div>
                <h4 className="font-medium mb-2">Languages</h4>

                <div>
                    <div className="flex flex-wrap gap-2">
                        <p className="font-medium">Chinese: Fluent</p>
                    </div>
                    <div>
                        <p className="font-medium">English: Proficient</p>
                        <p className="text-gray-600">TOEFL 106, GEPT high-intermediate level</p>
                    </div></div>
                        <div className="flex flex-wrap gap-2">
                        {['Chinese', 'English'].map((skill) => (
                            <span key={skill} className="px-3 py-1 bg-gray-100 dark:bg-gray-800 rounded-full text-sm">
                            {skill}
                            </span>
                        ))}
                        </div>
            </div>
          <div>
            <h4 className="font-medium mb-2">Programming Languages & Tools</h4>
            <div className="flex flex-wrap gap-2">
              {['C', 'C++', 'Python', 'SQL', 'PyTorch', 'Gurobi', 'Arduino'].map((skill) => (
                <span key={skill} className="px-3 py-1 bg-gray-100 dark:bg-gray-800 rounded-full text-sm">
                  {skill}
                </span>
              ))}
            </div>
          </div>
          <div>
            <h4 className="font-medium mb-2">Areas of Expertise (click for relevant projects) </h4>
            <div className="flex flex-wrap gap-2">
            {[
                { skill: 'Deep Learning', slug: 'deep-learning' },
                { skill: 'Information Retrieval', slug: 'information-retrieval' },
                { skill: 'Large Language Models', slug: 'large-language-models' },
                { skill: 'Data Analysis', slug: 'data-analysis' },
                { skill: 'Database', slug: 'database' },
                { skill: 'Backend', slug: 'backend' }
            ].map(({ skill, slug }) => (
                <Link 
                key={skill} 
                href={`/skills/${slug}`}
                className="px-3 py-1 bg-gray-100 dark:bg-gray-800 rounded-full text-sm hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors"
                >
                {skill}
                </Link>
            ))}
            </div>
          </div>
        </div>
      </div>

      {/* Soft Skills */}
      <div className="w-full">
        <h3 className="font-semibold text-2xl mb-3">Soft Skills</h3>
        <div className="space-y-3">

        <div>
            <h4 className="font-medium mb-2">Soft Skills that I am confident about (click for relevant experiences) </h4>
            <div className="flex flex-wrap gap-2">
  {[
    { skill: 'Communication', slug: 'communication-skills' },
    { skill: 'Public Speaking', slug: 'public-speaking' },
    { skill: 'Leadership', slug: 'leadership' },
    { skill: 'Team Management', slug: 'team-management' },
    { skill: 'Project Management', slug: 'project-management' },
    { skill: 'Marketing Strategy', slug: 'marketing-strategy' },
    { skill: 'Business Development', slug: 'business-development' },
    { skill: 'Meeting Facilitation', slug: 'meeting-facilitation' }
  ].map(({ skill, slug }) => (
    <Link 
      key={skill} 
      href={`/skills/${slug}`}
      className="px-3 py-1 bg-gray-100 dark:bg-gray-800 rounded-full text-sm hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors"
    >
      {skill}
    </Link>
  ))}
</div>
          </div>
        </div>
      </div>

      {/* Contact Information */}
      <div className="w-full text-center sm:text-left">
        <h3 className="font-semibold text-xl mb-3">Contact</h3>
        <div className="space-y-2">
          <p>📧 debbiehuang35117@gmail.com</p>
          <p>📍 Taipei, Taiwan</p>
          <p>🌐 Fluent in Chinese and English</p>
        </div>
      </div>
    </div>
  );
}