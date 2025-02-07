// app/components/ContactSection.tsx
import Link from 'next/link';
import { 
  Mail, 
  MapPin, 
  Globe, 
  Linkedin, 
  Github, 
  Twitter 
} from 'lucide-react';

export default function ContactSection() {
  const socialLinks = [
    {
      icon: Linkedin,
      href: "https://www.linkedin.com/in/debbie-huang-b813b7271/",
      color: "text-blue-600"
    },
    {
      icon: Github,
      href: "https://github.com/DebbieHuang35117",
      color: "text-gray-800 dark:text-white"
    }
  ];

  return (
    <div className="w-full max-w-4xl bg-gray-50 dark:bg-gray-800 rounded-lg p-8 shadow-md">
      <h2 className="text-2xl font-bold mb-6 text-center">Let's Connect</h2>
      
      <div className="space-y-4 text-center">
        {/* Contact Information */}
        <div className="flex flex-col sm:flex-row justify-center gap-6">
          <div className="flex items-center gap-3 justify-center">
            <Mail className="text-gray-600" />
            <a 
              href="mailto:debbiehuang35117@gmail.com"
              className="hover:text-blue-600 dark:hover:text-blue-400 transition-colors"
            >
              debbiehuang35117@gmail.com
            </a>
          </div>
          <div className="flex items-center gap-3 justify-center">
            <MapPin className="text-gray-600" />
            <span>Taipei, Taiwan</span>
          </div>
        </div>

        {/* Social Links */}
        <div className="flex justify-center gap-6 mt-6">
          {socialLinks.map((social) => (
            <Link 
              key={social.href}
              href={social.href}
              target="_blank"
              rel="noopener noreferrer"
              className={`
                ${social.color} 
                hover:scale-110 
                transition-transform 
                duration-300 
                ease-in-out
              `}
            >
              <social.icon size={24} />
            </Link>
          ))}
        </div>

        {/* Contact Button */}
        <div className="mt-8">
          <a 
            href="mailto:debbiehuang35117@gmail.com"
            className="
              inline-block 
              px-6 
              py-3 
              bg-blue-600 
              text-white 
              rounded-full 
              hover:bg-blue-700 
              transition-colors 
              duration-300 
              shadow-md 
              hover:shadow-lg
            "
          >
            Send me an Email
          </a>
        </div>
      </div>
    </div>
  );
}