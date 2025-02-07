// app/components/FunFacts.tsx
'use client'
import Image from 'next/image';
import { useState } from "react";

{/*adding copy paste function*/}

export default function FunFacts() {

    const funFacts = [
      {
        emoji: "🏸",
        fact: "Badminton Enthusiast: played badminton for 7 years, won badminton contests nationwide"
      },
      {
        emoji: "🗺️",
        fact: "World map collector: I like to travel plus being the big foodie!"
      },
      {
        emoji: "💪",
        fact: "Athletic Lover: I like working out and staying active"
      },
      {
        emoji: "🌏",
        fact: "Bilingual Growth Background: 10 years of bilingual education at Korrnell Academy"
      }
      // Add more personal facts
    ];

    const [copiedFact, setCopiedFact] = useState(null);

    const handleCopy = async (text) => {
      try {
        await navigator.clipboard.writeText(text);
        setCopiedFact(text);
        setTimeout(() => setCopiedFact(null), 2000); // Reset after 2s
      } catch (err) {
        console.error("Failed to copy:", err);
      }
    };
  
    return (
      <div className="right-12 top-40 max-w-xs">
        <div className='text-xl'>Fun facts about me</div>
        {funFacts.map((item, index) => (
          <div key={index} className="flex items-center gap-3 space-y-2">
            <span className="text-2xl">{item.emoji}</span>
            {item.hyperlink ? (
              <a
                href={item.hyperlink}
                target="_blank"
                rel="noopener noreferrer"
                className="hover:underline"
              >
                <p>{item.fact}</p>
              </a>
            ) : (
              <p>{item.fact}</p>
            )}
          </div>
        ))}
      </div>
    );
  }