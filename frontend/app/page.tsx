"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [message, setMessage] = useState("Loading backend...");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/")
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch(() => setMessage("Backend not connected"));
  }, []);

  return (
    <main className="min-h-screen flex flex-col items-center justify-center bg-slate-950 text-white">
      <h1 className="text-5xl font-bold mb-6">
        🩸 Blood Report Analyzer
      </h1>

      <p className="text-xl mb-8">
        {message}
      </p>

      <button className="bg-red-600 px-6 py-3 rounded-xl hover:bg-red-700">
        Upload Blood Report
      </button>
    </main>
  );
}