'use client';

import React from 'react';
import Link from 'next/link';

interface ThankYouState {
  applicationData: string;
  referenceNumber: string;
}

class ThankYouPage extends React.Component<Record<string, never>, ThankYouState> {
  constructor(props: Record<string, never>) {
    super(props);
    this.state = {
      applicationData: '',
      referenceNumber: `REF-${Date.now()}`
    };
  }

  componentDidMount() {
    // Load all form data from sessionStorage
    const part1Data = sessionStorage.getItem('enrollmentFormPart1');
    const part2Data = sessionStorage.getItem('enrollmentFormPart2');
    const part3Data = sessionStorage.getItem('enrollmentFormPart3');
    const part4Data = sessionStorage.getItem('enrollmentFormPart4');
    const part5Data = sessionStorage.getItem('enrollmentFormPart5');
    const part6Data = sessionStorage.getItem('enrollmentFormPart6');
    
    const completeData = {
      part1: part1Data ? JSON.parse(part1Data) : {},
      part2: part2Data ? JSON.parse(part2Data) : {},
      part3: part3Data ? JSON.parse(part3Data) : {},
      part4: part4Data ? JSON.parse(part4Data) : {},
      part5: part5Data ? JSON.parse(part5Data) : {},
      part6: part6Data ? JSON.parse(part6Data) : {}
    };

    // Convert to readable string format
    const formattedData = JSON.stringify(completeData, null, 2);
    this.setState({ applicationData: formattedData });

    // Clear all session storage data after loading
    setTimeout(() => {
      sessionStorage.removeItem('enrollmentFormPart1');
      sessionStorage.removeItem('enrollmentFormPart2');
      sessionStorage.removeItem('enrollmentFormPart3');
      sessionStorage.removeItem('enrollmentFormPart4');
      sessionStorage.removeItem('enrollmentFormPart5');
      sessionStorage.removeItem('enrollmentFormPart6');
    }, 2000);
  }

  render() {
    const { applicationData, referenceNumber } = this.state;

    return (
      <div className="min-h-screen bg-gradient-to-br from-purple-900 via-blue-900 to-indigo-900 p-4">
        <div className="max-w-6xl mx-auto">
          {/* Header */}
          <div className="text-center mb-8 pt-8">
            <div className="bg-white/10 backdrop-blur-lg rounded-3xl shadow-2xl border border-white/20 p-8 mb-8">
              <h1 className="text-5xl font-bold text-white mb-4">🎉 Thank You!</h1>
              <p className="text-xl text-green-100 mb-2">Your dental clinic enrollment application has been submitted successfully!</p>
              <p className="text-lg text-blue-100">We will review your information and contact you soon.</p>
              <p className="text-lg text-white mt-4">
                Application Reference: <span className="font-mono text-green-300">{referenceNumber}</span>
              </p>
            </div>
          </div>

          {/* Application Data */}
          <div className="bg-white/10 backdrop-blur-lg rounded-3xl shadow-2xl border border-white/20 p-8 mb-8">
            <h2 className="text-3xl font-bold text-white mb-6 text-center border-b border-white/20 pb-4">
              Submitted Application Data
            </h2>
            
            <div className="bg-black/20 rounded-xl p-6 border border-white/10">
              <pre className="text-green-300 text-sm overflow-auto max-h-96 whitespace-pre-wrap">
                {applicationData || 'Loading application data...'}
              </pre>
            </div>
          </div>

          {/* Footer with Home Link */}
          <div className="text-center pb-8">
            <div className="bg-white/10 backdrop-blur-lg rounded-3xl shadow-2xl border border-white/20 p-6">
              <p className="text-lg text-white mb-4">
                Keep your reference number for future correspondence.
              </p>
              <Link href="/" className="inline-block px-8 py-3 bg-gradient-to-r from-green-600 to-blue-600 text-white rounded-xl hover:from-green-700 hover:to-blue-700 transition-all duration-300 font-medium shadow-lg text-lg">
                🏠 Return to Home Page
              </Link>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default ThankYouPage;