function ResultCard({ result }) {
  const { fake_probability, real_probability, is_fake, message, analyzed_text } = result

  // Dairesel grafik için SVG path hesaplama
  const radius = 60
  const circumference = 2 * Math.PI * radius
  const fakeOffset = circumference - (fake_probability / 100) * circumference
  const realOffset = circumference - (real_probability / 100) * circumference

  return (
    <div className="mt-6 space-y-6">
      {/* Ana Sonuç Kartı - Gradient ve Renkli */}
      <div className={`relative overflow-hidden rounded-2xl shadow-2xl ${
        is_fake 
          ? 'bg-gradient-to-br from-red-50 via-orange-50 to-red-100 border-2 border-red-200' 
          : 'bg-gradient-to-br from-green-50 via-emerald-50 to-green-100 border-2 border-green-200'
      }`}>
        {/* Arka plan deseni */}
        <div className="absolute inset-0 opacity-10">
          <div className="absolute inset-0" style={{
            backgroundImage: 'radial-gradient(circle at 2px 2px, currentColor 1px, transparent 0)',
            backgroundSize: '24px 24px'
          }}></div>
        </div>
        
        <div className="relative p-8">
          <div className="flex flex-col md:flex-row items-center gap-6">
            {/* Büyük İkon */}
            <div className={`flex-shrink-0 w-24 h-24 rounded-full flex items-center justify-center shadow-lg ${
              is_fake ? 'bg-gradient-to-br from-red-400 to-red-600' : 'bg-gradient-to-br from-green-400 to-green-600'
            }`}>
              {is_fake ? (
                <svg className="w-12 h-12 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                </svg>
              ) : (
                <svg className="w-12 h-12 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              )}
            </div>
            
            <div className="flex-1 text-center md:text-left">
              <h3 className={`text-3xl font-bold mb-3 ${is_fake ? 'text-red-800' : 'text-green-800'}`}>
                {message}
              </h3>
              <p className={`text-lg ${is_fake ? 'text-red-600' : 'text-green-600'}`}>
                {is_fake ? 'Bu haberi paylaşmadan önce dikkatli olun!' : 'Bu haber güvenilir görünüyor.'}
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Grafik ve İstatistikler */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Dairesel Grafik */}
        <div className="card bg-gradient-to-br from-white to-gray-50">
          <h4 className="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2">
            <svg className="w-5 h-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
            Olasılık Dağılımı
          </h4>
          <div className="flex items-center justify-center">
            <div className="relative w-48 h-48">
              <svg className="transform -rotate-90" width="192" height="192">
                {/* Arka plan daire */}
                <circle
                  cx="96"
                  cy="96"
                  r={radius}
                  stroke="currentColor"
                  strokeWidth="12"
                  fill="none"
                  className="text-gray-200"
                />
                {/* Sahte olasılık */}
                <circle
                  cx="96"
                  cy="96"
                  r={radius}
                  stroke="currentColor"
                  strokeWidth="12"
                  fill="none"
                  strokeDasharray={circumference}
                  strokeDashoffset={fakeOffset}
                  strokeLinecap="round"
                  className="text-red-500 transition-all duration-1000"
                />
                {/* Gerçek olasılık */}
                <circle
                  cx="96"
                  cy="96"
                  r={radius - 14}
                  stroke="currentColor"
                  strokeWidth="12"
                  fill="none"
                  strokeDasharray={circumference}
                  strokeDashoffset={realOffset}
                  strokeLinecap="round"
                  className="text-green-500 transition-all duration-1000"
                />
              </svg>
              <div className="absolute inset-0 flex flex-col items-center justify-center">
                <div className="text-3xl font-bold text-gray-800">{fake_probability}%</div>
                <div className="text-sm text-gray-500">Sahte</div>
              </div>
            </div>
          </div>
          <div className="mt-4 flex justify-center gap-6">
            <div className="text-center">
              <div className="text-2xl font-bold text-red-600">{fake_probability}%</div>
              <div className="text-xs text-gray-600">Sahte</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-green-600">{real_probability}%</div>
              <div className="text-xs text-gray-600">Gerçek</div>
            </div>
          </div>
        </div>

        {/* Detaylı Progress Bar'lar */}
        <div className="card bg-gradient-to-br from-white to-blue-50">
          <h4 className="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2">
            <svg className="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
            Detaylı Analiz
          </h4>
          
          <div className="space-y-6">
            {/* Sahte Olasılığı */}
            <div>
              <div className="flex justify-between items-center mb-2">
                <div className="flex items-center gap-2">
                  <div className="w-3 h-3 rounded-full bg-gradient-to-r from-red-400 to-red-600"></div>
                  <span className="font-semibold text-gray-700">Sahte Olasılığı</span>
                </div>
                <span className="text-xl font-bold text-red-600">{fake_probability}%</span>
              </div>
              <div className="w-full bg-gray-200 rounded-full h-4 overflow-hidden shadow-inner">
                <div
                  className="h-full rounded-full bg-gradient-to-r from-red-400 via-red-500 to-red-600 transition-all duration-1000 ease-out flex items-center justify-end pr-2"
                  style={{ width: `${fake_probability}%` }}
                >
                  {fake_probability > 10 && (
                    <span className="text-white text-xs font-bold">{fake_probability}%</span>
                  )}
                </div>
              </div>
            </div>
            
            {/* Gerçek Olasılığı */}
            <div>
              <div className="flex justify-between items-center mb-2">
                <div className="flex items-center gap-2">
                  <div className="w-3 h-3 rounded-full bg-gradient-to-r from-green-400 to-green-600"></div>
                  <span className="font-semibold text-gray-700">Güvenilir Olasılığı</span>
                </div>
                <span className="text-xl font-bold text-green-600">{real_probability}%</span>
              </div>
              <div className="w-full bg-gray-200 rounded-full h-4 overflow-hidden shadow-inner">
                <div
                  className="h-full rounded-full bg-gradient-to-r from-green-400 via-green-500 to-green-600 transition-all duration-1000 ease-out flex items-center justify-end pr-2"
                  style={{ width: `${real_probability}%` }}
                >
                  {real_probability > 10 && (
                    <span className="text-white text-xs font-bold">{real_probability}%</span>
                  )}
                </div>
              </div>
            </div>

            {/* Risk Seviyesi */}
            <div className="pt-4 border-t border-gray-200">
              <div className="flex items-center justify-between mb-2">
                <span className="font-semibold text-gray-700">Risk Seviyesi</span>
                <span className={`px-3 py-1 rounded-full text-sm font-bold ${
                  fake_probability > 70 ? 'bg-red-100 text-red-800' :
                  fake_probability > 50 ? 'bg-orange-100 text-orange-800' :
                  'bg-yellow-100 text-yellow-800'
                }`}>
                  {fake_probability > 70 ? 'Yüksek' : fake_probability > 50 ? 'Orta' : 'Düşük'}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Analiz Edilen Metin Önizlemesi */}
      {analyzed_text && (
        <div className="card bg-gradient-to-br from-gray-50 to-white">
          <h4 className="font-bold text-gray-800 mb-4 flex items-center gap-2 text-lg">
            <svg className="w-5 h-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            Analiz Edilen Metin
          </h4>
          <div className="bg-white rounded-lg p-4 border border-gray-200 shadow-sm">
            <p className="text-gray-700 text-sm leading-relaxed whitespace-pre-wrap">
              {analyzed_text}
            </p>
          </div>
        </div>
      )}
    </div>
  )
}

export default ResultCard

