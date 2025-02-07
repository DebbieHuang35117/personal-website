import Image from "next/image";

export default function Footer() {
  return (
    <footer className="row-start-3 flex gap-6 flex-wrap items-center justify-center">
      <a
        className="flex items-center gap-2 hover:underline hover:underline-offset-4"
        href="https://github.com/DebbieHuang35117"
        target="_blank"
        rel="noopener noreferrer"
      >
        <Image
          aria-hidden
          src="/icons/github_logo.png"
          alt="github icon"
          width={16}
          height={16}
        />
        My Github
      </a>
      <a
        className="flex items-center gap-2 hover:underline hover:underline-offset-4"
        href="https://www.linkedin.com/in/debbie-huang-b813b7271/"
        target="_blank"
        rel="noopener noreferrer"
      >
        <Image
          aria-hidden
          src="/icons/linkedin_logo.png"
          alt="LinkedIn icon"
          width={16}
          height={16}
        />
        My LinkedIn
      </a>
      <a
        className="flex items-center gap-2 hover:underline hover:underline-offset-4"
        href="https://www.linkedin.com/in/debbie-huang-b813b7271/"
        target="_blank"
        rel="noopener noreferrer"
      >
        <Image
          aria-hidden
          src="/globe.svg"
          alt="Globe icon"
          width={16}
          height={16}
        />
        Have some fun? →
      </a>
    </footer>
  );
}