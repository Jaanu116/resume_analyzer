function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-black via-gray-900 to-cyan-950 text-white">

      {/* Navbar */}
      <nav className="flex justify-between items-center px-10 py-6">
        <h1 className="text-3xl font-bold text-cyan-400">
          ResumeAI
        </h1>

        <div className="space-x-6">
          <button className="hover:text-cyan-400 transition duration-300">
            Login
          </button>

          <button className="bg-cyan-500 px-5 py-2 rounded-lg hover:bg-cyan-600 transition duration-300 shadow-lg shadow-cyan-500/30">
            Signup
          </button>
        </div>
      </nav>

      {/* Hero Section */}
      <div className="flex flex-col items-center justify-center text-center mt-28 px-6">

        <h1 className="text-6xl font-extrabold leading-tight max-w-4xl">
          AI Powered{" "}
          <span className="text-cyan-400">
            Resume Analyzer
          </span>
        </h1>

        <p className="text-gray-300 mt-6 text-lg max-w-2xl leading-relaxed">
          Analyze your resume using AI, improve ATS score,
          detect missing skills, and receive intelligent
          recommendations for better job opportunities.
        </p>

        <button className="mt-10 bg-cyan-500 px-8 py-4 rounded-2xl text-lg font-semibold hover:bg-cyan-600 transition duration-300 shadow-xl shadow-cyan-500/30 hover:scale-105">
          Upload Resume
        </button>
      </div>

      {/* Feature Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 px-10 mt-24 pb-20">

        {/* Card 1 */}
        <div className="bg-white/10 backdrop-blur-lg border border-white/10 rounded-2xl p-8 hover:scale-105 transition duration-300 shadow-xl">
          <h2 className="text-2xl font-bold text-cyan-400">
            ATS Score
          </h2>

          <p className="text-gray-300 mt-4">
            Get an instant ATS compatibility score
            for your resume.
          </p>
        </div>

        {/* Card 2 */}
        <div className="bg-white/10 backdrop-blur-lg border border-white/10 rounded-2xl p-8 hover:scale-105 transition duration-300 shadow-xl">
          <h2 className="text-2xl font-bold text-cyan-400">
            Skill Detection
          </h2>

          <p className="text-gray-300 mt-4">
            Detect technical and professional skills
            automatically using AI.
          </p>
        </div>

        {/* Card 3 */}
        <div className="bg-white/10 backdrop-blur-lg border border-white/10 rounded-2xl p-8 hover:scale-105 transition duration-300 shadow-xl">
          <h2 className="text-2xl font-bold text-cyan-400">
            AI Suggestions
          </h2>

          <p className="text-gray-300 mt-4">
            Receive intelligent resume improvement
            recommendations instantly.
          </p>
        </div>

      </div>
    </div>
  );
}

export default Home;