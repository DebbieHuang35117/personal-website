// app/page.tsx
import Header from './components/Header';
import ContactFloater from './components/ContactFloater';
import ProfileSection from './components/ProfileSection';
import ProjectsSection from './components/ProjectsSection';
import ContactSection from './components/ContactSection';
import FunFacts from './components/FunFacts';
import Footer from './components/Footer';

export default function Home() {
  return (
    <div className="min-h-screen p-8 pb-20 sm:p-20">
      <div className="flex gap-12">
        <main className="flex flex-col gap-12 max-w-4xl">
          <Header />
          <ContactFloater />
          <ProfileSection />
          <ProjectsSection />
          <ContactSection />
        </main>
        <FunFacts />
      </div>
      <Footer />
    </div>
  );
}