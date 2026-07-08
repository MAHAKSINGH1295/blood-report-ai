export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-red-950 text-white flex items-center justify-center px-6">
      <div className="max-w-4xl w-full text-center">

        <h1 className="text-6xl font-extrabold mb-6">
          🩸 Blood Report Analyzer
        </h1>

        <p className="text-xl text-gray-300 mb-12">
          Upload your blood report and receive AI-powered explanations,
          abnormal value detection, and personalized health insights.
        </p>

        <div className="border-2 border-dashed border-red-500 rounded-3xl p-16 bg-white/5 backdrop-blur-sm">

          <div className="text-6xl mb-5">
              📄
          </div>

          <h2 className="text-2xl font-bold">
            Drag & Drop your Blood Report
          </h2>

          <p className="text-gray-400 mt-3">
            PDF • JPG • PNG
          </p>

          <button className="mt-10 bg-red-600 hover:bg-red-700 transition px-8 py-4 rounded-xl text-lg font-semibold">
            Upload Report
          </button>

        </div>

      </div>
    </main>
  );
}