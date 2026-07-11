"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [message, setMessage] = useState("Connecting to backend...");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/")
      .then((response) => response.json())
      .then((data) => setMessage(data.message))
      .catch(() => setMessage("Backend not connected"));
  }, []);

  return (
    <main className="min-h-screen flex flex-col items-center justify-center bg-slate-950 text-white">
      <h1 className="text-5xl font-bold mb-6">
        🩸 Blood Report Analyzer
      </h1>

      <p className="text-xl text-green-400 mb-8">
        {message}
      </p>

      <button className="bg-red-600 hover:bg-red-700 px-6 py-3 rounded-lg">
        Upload Blood Report
      </button>
    </main>
  );
}