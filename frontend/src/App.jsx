import { useState } from 'react'
import Navbar from './components/Navbar'
import InputForm from './components/InputForm'
import ResultCard from './components/ResultCard'
import axios from 'axios'

function App() {
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const analyzeNews = async (text, url) => {
    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const response = await axios.post('http://localhost:8000/api/analyze/', {
        text: text || null,
        url: url || null
      })

      setResult(response.data)
    } catch (err) {
      if (err.response?.data?.detail) {
        setError(err.response.data.detail)
      } else {
        setError('Bir hata oluştu. Lütfen tekrar deneyin.')
      }
      console.error('Analiz hatası:', err)
    } finally {
      setLoading(false)
    }
  }

  const handleReset = () => {
    setResult(null)
    setError(null)
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
      <Navbar />
      <main className="container mx-auto px-4 py-8 max-w-4xl">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-800 mb-3">
            Sahte Haber Tespit Sistemi
          </h1>
          <p className="text-gray-600 text-lg">
            Türkçe haberlerin güvenilirliğini analiz edin
          </p>
        </div>

        <InputForm 
          onSubmit={analyzeNews} 
          loading={loading}
          onReset={handleReset}
        />

        {error && (
          <div className="mt-6 card bg-red-50 border-red-200">
            <div className="flex items-center gap-3">
              <svg className="w-6 h-6 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <p className="text-red-800 font-medium">{error}</p>
            </div>
          </div>
        )}

        {result && (
          <ResultCard result={result} />
        )}

        <div className="mt-12 text-center text-gray-500 text-sm">
          <p>
            Bu sistem yapay zeka tabanlı analiz yapar. Sonuçlar %100 kesin değildir.
          </p>
        </div>
      </main>
    </div>
  )
}

export default App

