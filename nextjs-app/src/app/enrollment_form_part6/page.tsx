'use client';

import React from 'react';
import { SemiConstants } from '../constants/SemiConstants';

interface FormData {
  beforeAfterPhotos: string;
  patientReviews: string;
  internationalClients: string;
}

interface EnrollmentFormPart6State {
  formData: FormData;
}

class EnrollmentFormPart6 extends React.Component<Record<string, never>, EnrollmentFormPart6State> {
  constructor(props: Record<string, never>) {
    super(props);
    this.state = {
      formData: {
        beforeAfterPhotos: '',
        patientReviews: '',
        internationalClients: ''
      }
    };
  }

  componentDidMount() {
    // Load previous form data if available
    const part1Data = sessionStorage.getItem('enrollmentFormPart1');
    const part2Data = sessionStorage.getItem('enrollmentFormPart2');
    const part3Data = sessionStorage.getItem('enrollmentFormPart3');
    const part4Data = sessionStorage.getItem('enrollmentFormPart4');
    const part5Data = sessionStorage.getItem('enrollmentFormPart5');
    
    if (part1Data) {
      console.log('Part 1 data:', JSON.parse(part1Data));
    }
    if (part2Data) {
      console.log('Part 2 data:', JSON.parse(part2Data));
    }
    if (part3Data) {
      console.log('Part 3 data:', JSON.parse(part3Data));
    }
    if (part4Data) {
      console.log('Part 4 data:', JSON.parse(part4Data));
    }
    if (part5Data) {
      console.log('Part 5 data:', JSON.parse(part5Data));
    }
  }

  handleRadioChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    this.setState(prevState => ({
      formData: {
        ...prevState.formData,
        [name]: value
      }
    }));
  };

  handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    // Validate required fields
    if (!this.state.formData.beforeAfterPhotos || 
        !this.state.formData.patientReviews || 
        !this.state.formData.internationalClients) {
      alert('Please fill in all required fields.');
      return;
    }

    console.log("Enrollment form part 6 submitted:", this.state.formData);
    
    // Store form data in sessionStorage
    sessionStorage.setItem('enrollmentFormPart6', JSON.stringify(this.state.formData));
    
    // Get all form data for final submission
    const part1Data = sessionStorage.getItem('enrollmentFormPart1');
    const part2Data = sessionStorage.getItem('enrollmentFormPart2');
    const part3Data = sessionStorage.getItem('enrollmentFormPart3');
    const part4Data = sessionStorage.getItem('enrollmentFormPart4');
    const part5Data = sessionStorage.getItem('enrollmentFormPart5');
    
    const completeFormData = {
      part1: part1Data ? JSON.parse(part1Data) : {},
      part2: part2Data ? JSON.parse(part2Data) : {},
      part3: part3Data ? JSON.parse(part3Data) : {},
      part4: part4Data ? JSON.parse(part4Data) : {},
      part5: part5Data ? JSON.parse(part5Data) : {},
      part6: this.state.formData
    };
    
    console.log("Complete enrollment application data:", completeFormData);
    
    // Navigate to thank you page (session storage will be cleared there)
    window.location.href = '/thank-you';
  };

  render() {
    return (
      <div className="min-h-screen bg-gradient-to-br from-purple-900 via-blue-900 to-indigo-900 flex items-center justify-center p-4">
        <div className="w-full max-w-4xl bg-white/10 backdrop-blur-lg rounded-3xl shadow-2xl border border-white/20 p-8">
          <div className="text-center mb-8">
            <h1 className="text-4xl font-bold text-white mb-2">Clinic Enrollment</h1>
            <p className="text-xl text-blue-100">Part 6: Reviews & References</p>
            <div className="flex justify-center mt-4">
              <div className="flex space-x-2">
                <div className="w-3 h-3 rounded-full bg-green-400"></div>
                <div className="w-3 h-3 rounded-full bg-green-400"></div>
                <div className="w-3 h-3 rounded-full bg-green-400"></div>
                <div className="w-3 h-3 rounded-full bg-green-400"></div>
                <div className="w-3 h-3 rounded-full bg-green-400"></div>
                <div className="w-3 h-3 rounded-full bg-blue-400"></div>
              </div>
            </div>
          </div>

          <form onSubmit={this.handleSubmit} className="space-y-6">
            {/* Reviews & References Section */}
            <div className="bg-white/5 rounded-xl p-6 border border-white/10">
              <h2 className="text-2xl font-semibold text-white mb-6 border-b border-white/20 pb-2">
                Reviews & References
              </h2>

              {/* Can you share before-and-after photos? */}
              <div className="mb-6">
                <label className="block text-sm font-medium text-white mb-3">
                  Can you share before-and-after photos? *
                </label>
                <div className="space-y-2">
                  {SemiConstants.BEFORE_AFTER_PHOTOS_OPTIONS.map((option, index) => (
                    <label key={index} className="flex items-center space-x-3 text-white cursor-pointer">
                      <input
                        type="radio"
                        name="beforeAfterPhotos"
                        value={option.value}
                        checked={this.state.formData.beforeAfterPhotos === option.value}
                        onChange={this.handleRadioChange}
                        className="w-4 h-4 text-blue-600 bg-white/10 border-white/20 focus:ring-blue-500"
                      />
                      <span className="text-sm">{option.label}</span>
                    </label>
                  ))}
                </div>
              </div>

              {/* Do you collect patient reviews or testimonials? */}
              <div className="mb-6">
                <label className="block text-sm font-medium text-white mb-3">
                  Do you collect patient reviews or testimonials? *
                </label>
                <div className="space-y-2">
                  {SemiConstants.YES_NO_OPTIONS.map((option, index) => (
                    <label key={index} className="flex items-center space-x-3 text-white cursor-pointer">
                      <input
                        type="radio"
                        name="patientReviews"
                        value={option.value}
                        checked={this.state.formData.patientReviews === option.value}
                        onChange={this.handleRadioChange}
                        className="w-4 h-4 text-blue-600 bg-white/10 border-white/20 focus:ring-blue-500"
                      />
                      <span className="text-sm">{option.label}</span>
                    </label>
                  ))}
                </div>
              </div>

              {/* Are you willing to connect prospective patients with past international clients? */}
              <div className="mb-6">
                <label className="block text-sm font-medium text-white mb-3">
                  Are you willing to connect prospective patients with past international clients? *
                </label>
                <div className="space-y-2">
                  {SemiConstants.YES_NO_OPTIONS.map((option, index) => (
                    <label key={index} className="flex items-center space-x-3 text-white cursor-pointer">
                      <input
                        type="radio"
                        name="internationalClients"
                        value={option.value}
                        checked={this.state.formData.internationalClients === option.value}
                        onChange={this.handleRadioChange}
                        className="w-4 h-4 text-blue-600 bg-white/10 border-white/20 focus:ring-blue-500"
                      />
                      <span className="text-sm">{option.label}</span>
                    </label>
                  ))}
                </div>
              </div>
            </div>

            {/* Navigation Buttons */}
            <div className="flex justify-between pt-6">
              <button
                type="button"
                onClick={() => window.history.back()}
                className="px-6 py-3 bg-white/10 text-white border border-white/20 rounded-xl hover:bg-white/20 transition-all duration-300 font-medium"
              >
                ← Back to Part 5
              </button>
              
              <button
                type="submit"
                className="px-8 py-3 bg-gradient-to-r from-green-600 to-blue-600 text-white rounded-xl hover:from-green-700 hover:to-blue-700 transition-all duration-300 font-medium shadow-lg"
              >
                Submit Application
              </button>
            </div>
          </form>
        </div>
      </div>
    );
  }
}

export default EnrollmentFormPart6;