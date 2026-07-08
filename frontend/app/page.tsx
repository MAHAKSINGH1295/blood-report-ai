export default function Home() {
  return (
    <main className="min-h-screen bg-slate-950 text-white flex items-center justify-center p-6">
      <div className="max-w-3xl w-full text-center">
        <h1 className="text-5xl font-bold mb-6">
          🩸 Blood Report Analyzer
        </h1>

        <p className="text-gray-300 text-lg mb-10">
          Upload your blood report and receive AI-powered explanations in
          simple, easy-to-understand language.
        </p>

        <div className="border-2 border-dashed border-gray-600 rounded-2xl p-12 mb-8">
          <p className="text-xl font-semibold">
            📄 Drag & Drop your Blood Report
          </p>

          <p className="text-gray-400 mt-2">
            Supports PDF, JPG and PNG files
          </p>
        </div>

        <button className="bg-red-600 hover:bg-red-700 transition px-8 py-3 rounded-xl text-lg font-semibold">
          Analyze Report
        </button>
      </div>
    </main>
  );
}