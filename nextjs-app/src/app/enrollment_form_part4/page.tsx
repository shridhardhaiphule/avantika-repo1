'use client';

import React from 'react';
import { SemiConstants } from '../constants/SemiConstants';

interface FormData {
  dentalTreatments: string[];
  cosmeticDentistry: string;
  materialsBrands: string;
  treatmentGuarantees: string;
}

interface EnrollmentFormPart4State {
  formData: FormData;
}

class EnrollmentFormPart4 extends React.Component<Record<string, never>, EnrollmentFormPart4State> {
  constructor(props: Record<string, never>) {
    super(props);
    this.state = {
      formData: {
        dentalTreatments: [],
        cosmeticDentistry: '',
        materialsBrands: '',
        treatmentGuarantees: ''
      }
    };
  }

  componentDidMount() {
    // Load previous form data if available
    const part1Data = sessionStorage.getItem('enrollmentFormPart1');
    const part2Data = sessionStorage.getItem('enrollmentFormPart2');
    const part3Data = sessionStorage.getItem('enrollmentFormPart3');
    
    if (part1Data) {
      console.log('Part 1 data:', JSON.parse(part1Data));
    }
    if (part2Data) {
      console.log('Part 2 data:', JSON.parse(part2Data));
    }
    if (part3Data) {
      console.log('Part 3 data:', JSON.parse(part3Data));
    }
  }

  handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    this.setState(prevState => ({
      formData: {
        ...prevState.formData,
        [name]: value
      }
    }));
  };

  handleCheckboxChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value, checked } = e.target;
    
    if (name === 'dentalTreatments') {
      this.setState(prevState => {
        const updatedTreatments = checked
          ? [...prevState.formData.dentalTreatments, value]
          : prevState.formData.dentalTreatments.filter(treatment => treatment !== value);
        
        return {
          formData: {
            ...prevState.formData,
            dentalTreatments: updatedTreatments
          }
        };
      });
    }
  };

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
    if (this.state.formData.dentalTreatments.length === 0 || 
        !this.state.formData.cosmeticDentistry || 
        !this.state.formData.treatmentGuarantees) {
      alert('Please fill in all required fields.');
      return;
    }

    console.log("Enrollment form part 4 submitted:", this.state.formData);
    
    // Store form data in sessionStorage to pass to part 5
    sessionStorage.setItem('enrollmentFormPart4', JSON.stringify(this.state.formData));
    
    // Navigate to part 5
    window.location.href = '/enrollment_form_part5';
  };

  render() {
    return (
      <div className="min-h-screen bg-gradient-to-br from-purple-900 via-blue-900 to-indigo-900 flex items-center justify-center p-4">
        <div className="w-full max-w-4xl bg-white/10 backdrop-blur-lg rounded-3xl shadow-2xl border border-white/20 p-8">
          <div className="text-center mb-8">
            <h1 className="text-4xl font-bold text-white mb-2">Clinic Enrollment</h1>
            <p className="text-xl text-blue-100">Part 4: Services Offered</p>
            <div className="flex justify-center mt-4">
              <div className="flex space-x-2">
                <div className="w-3 h-3 rounded-full bg-green-400"></div>
                <div className="w-3 h-3 rounded-full bg-green-400"></div>
                <div className="w-3 h-3 rounded-full bg-green-400"></div>
                <div className="w-3 h-3 rounded-full bg-blue-400"></div>
              </div>
            </div>
          </div>

          <form onSubmit={this.handleSubmit} className="space-y-6">
            {/* Services Offered Section */}
            <div className="bg-white/5 rounded-xl p-6 border border-white/10">
              <h2 className="text-2xl font-semibold text-white mb-6 border-b border-white/20 pb-2">
                Services Offered
              </h2>

              {/* Dental Treatments & Specializations */}
              <div className="mb-6">
                <label className="block text-sm font-medium text-white mb-3">
                  Dental Treatments & Specializations *
                </label>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
                  {SemiConstants.DENTAL_TREATMENTS_OPTIONS.map((treatment, index) => (
                    <label key={index} className="flex items-center space-x-3 text-white cursor-pointer">
                      <input
                        type="checkbox"
                        name="dentalTreatments"
                        value={treatment.value}
                        checked={this.state.formData.dentalTreatments.includes(treatment.value)}
                        onChange={this.handleCheckboxChange}
                        className="w-4 h-4 text-blue-600 bg-white/10 border-white/20 rounded focus:ring-blue-500"
                      />
                      <span className="text-sm">{treatment.label}</span>
                    </label>
                  ))}
                </div>
              </div>

              {/* Do you offer cosmetic dentistry? */}
              <div className="mb-6">
                <label className="block text-sm font-medium text-white mb-3">
                  Do you offer cosmetic dentistry? *
                </label>
                <div className="space-y-2">
                  {SemiConstants.YES_NO_OPTIONS.map((option, index) => (
                    <label key={index} className="flex items-center space-x-3 text-white cursor-pointer">
                      <input
                        type="radio"
                        name="cosmeticDentistry"
                        value={option.value}
                        checked={this.state.formData.cosmeticDentistry === option.value}
                        onChange={this.handleRadioChange}
                        className="w-4 h-4 text-blue-600 bg-white/10 border-white/20 focus:ring-blue-500"
                      />
                      <span className="text-sm">{option.label}</span>
                    </label>
                  ))}
                </div>
              </div>

              {/* Materials & Brands Used */}
              <div className="mb-6">
                <label htmlFor="materialsBrands" className="block text-sm font-medium text-white mb-2">
                  Materials & Brands Used
                </label>
                <textarea
                  id="materialsBrands"
                  name="materialsBrands"
                  value={this.state.formData.materialsBrands}
                  onChange={this.handleInputChange}
                  rows={4}
                  className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-black placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-vertical"
                  placeholder="Please describe the materials and brands you use in your dental procedures..."
                />
              </div>

              {/* Do you provide treatment guarantees or warranties? */}
              <div className="mb-6">
                <label className="block text-sm font-medium text-white mb-3">
                  Do you provide treatment guarantees or warranties? *
                </label>
                <div className="space-y-2">
                  {SemiConstants.TREATMENT_GUARANTEES_OPTIONS.map((option, index) => (
                    <label key={index} className="flex items-center space-x-3 text-white cursor-pointer">
                      <input
                        type="radio"
                        name="treatmentGuarantees"
                        value={option.value}
                        checked={this.state.formData.treatmentGuarantees === option.value}
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
                ← Back to Part 3
              </button>
              
              <button
                type="submit"
                className="px-8 py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-xl hover:from-blue-700 hover:to-purple-700 transition-all duration-300 font-medium shadow-lg"
              >
                Continue to Part 5 →
              </button>
            </div>
          </form>
        </div>
      </div>
    );
  }
}

export default EnrollmentFormPart4;