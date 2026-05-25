function Home() {
  return (
    <div className="min-h-screen bg-black text-white">
      
      <nav className="flex justify-between items-center px-10 py-6">
        <h1 className="text-3xl font-bold text-cyan-400">
          ResumeAI
        </h1>

        <div className="space-x-6">
          <button className="hover:text-cyan-400">
            Login
          </button>

          <button className="bg-cyan-500 px-5 py-2 rounded-lg hover:bg-cyan-600">
            Signup
          </button>
        </div>
      </nav>

      <div className="flex flex-col items-center justify-center text-center mt-32 px-5">
        
        <h1 className="text-6xl font-bold leading-tight">
          AI Powered <span className="text-cyan-400">Resume Analyzer</span>
        </h1>

        <p className="text-gray-400 mt-6 text-lg max-w-2xl">
          Analyze your resume using AI, get ATS scores,
          detect missing skills, and receive smart improvement suggestions.
        </p>

        <button className="mt-10 bg-cyan-500 px-8 py-4 rounded-xl text-lg hover:bg-cyan-600 transition duration-300">
          Upload Resume
        </button>

      </div>
    </div>
  );
}

export default Home;