'use client';

import React from 'react';
import { SemiConstants } from '../constants/SemiConstants';

interface FormData {
  standardPricing: string;
  bundledPackages: string;
  paymentMethods: string[];
  financingOptions: string;
}

interface EnrollmentFormPart5State {
  formData: FormData;
}

class EnrollmentFormPart5 extends React.Component<Record<string, never>, EnrollmentFormPart5State> {
  constructor(props: Record<string, never>) {
    super(props);
    this.state = {
      formData: {
        standardPricing: '',
        bundledPackages: '',
        paymentMethods: [],
        financingOptions: ''
      }
    };
  }

  componentDidMount() {
    // Load previous form data if available
    const part1Data = sessionStorage.getItem('enrollmentFormPart1');
    const part2Data = sessionStorage.getItem('enrollmentFormPart2');
    const part3Data = sessionStorage.getItem('enrollmentFormPart3');
    const part4Data = sessionStorage.getItem('enrollmentFormPart4');
    
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
  }

  handleCheckboxChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value, checked } = e.target;
    
    if (name === 'paymentMethods') {
      this.setState(prevState => {
        const updatedMethods = checked
          ? [...prevState.formData.paymentMethods, value]
          : prevState.formData.paymentMethods.filter(method => method !== value);
        
        return {
          formData: {
            ...prevState.formData,
            paymentMethods: updatedMethods
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
    if (!this.state.formData.standardPricing || 
        !this.state.formData.bundledPackages || 
        this.state.formData.paymentMethods.length === 0 ||
        !this.state.formData.financingOptions) {
      alert('Please fill in all required fields.');
      return;
    }

    console.log("Enrollment form part 5 submitted:", this.state.formData);
    
    // Store form data in sessionStorage to pass to part 6
    sessionStorage.setItem('enrollmentFormPart5', JSON.stringify(this.state.formData));
    
    // Navigate to part 6
    window.location.href = '/enrollment_form_part6';
  };

  render() {
    return (
      <div className="min-h-screen bg-gradient-to-br from-purple-900 via-blue-900 to-indigo-900 flex items-center justify-center p-4">
        <div className="w-full max-w-4xl bg-white/10 backdrop-blur-lg rounded-3xl shadow-2xl border border-white/20 p-8">
          <div className="text-center mb-8">
            <h1 className="text-4xl font-bold text-white mb-2">Clinic Enrollment</h1>
            <p className="text-xl text-blue-100">Part 5: Pricing & Packages</p>
            <div className="flex justify-center mt-4">
              <div className="flex space-x-2">
                <div className="w-3 h-3 rounded-full bg-green-400"></div>
                <div className="w-3 h-3 rounded-full bg-green-400"></div>
                <div className="w-3 h-3 rounded-full bg-green-400"></div>
                <div className="w-3 h-3 rounded-full bg-green-400"></div>
                <div className="w-3 h-3 rounded-full bg-blue-400"></div>
              </div>
            </div>
          </div>

          <form onSubmit={this.handleSubmit} className="space-y-6">
            {/* Pricing & Packages Section */}
            <div className="bg-white/5 rounded-xl p-6 border border-white/10">
              <h2 className="text-2xl font-semibold text-white mb-6 border-b border-white/20 pb-2">
                Pricing & Packages
              </h2>

              {/* Do you have standard pricing for popular treatments? */}
              <div className="mb-6">
                <label className="block text-sm font-medium text-white mb-3">
                  Do you have standard pricing for popular treatments? *
                </label>
                <div className="space-y-2">
                  {SemiConstants.STANDARD_PRICING_OPTIONS.map((option, index) => (
                    <label key={index} className="flex items-center space-x-3 text-white cursor-pointer">
                      <input
                        type="radio"
                        name="standardPricing"
                        value={option.value}
                        checked={this.state.formData.standardPricing === option.value}
                        onChange={this.handleRadioChange}
                        className="w-4 h-4 text-blue-600 bg-white/10 border-white/20 focus:ring-blue-500"
                      />
                      <span className="text-sm">{option.label}</span>
                    </label>
                  ))}
                </div>
              </div>

              {/* Do you offer bundled packages? */}
              <div className="mb-6">
                <label className="block text-sm font-medium text-white mb-3">
                  Do you offer bundled packages? *
                </label>
                <div className="space-y-2">
                  {SemiConstants.BUNDLED_PACKAGES_OPTIONS.map((option, index) => (
                    <label key={index} className="flex items-center space-x-3 text-white cursor-pointer">
                      <input
                        type="radio"
                        name="bundledPackages"
                        value={option.value}
                        checked={this.state.formData.bundledPackages === option.value}
                        onChange={this.handleRadioChange}
                        className="w-4 h-4 text-blue-600 bg-white/10 border-white/20 focus:ring-blue-500"
                      />
                      <span className="text-sm">{option.label}</span>
                    </label>
                  ))}
                </div>
              </div>

              {/* Payment Methods Accepted */}
              <div className="mb-6">
                <label className="block text-sm font-medium text-white mb-3">
                  Payment Methods Accepted *
                </label>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
                  {SemiConstants.PAYMENT_METHODS_OPTIONS.map((method, index) => (
                    <label key={index} className="flex items-center space-x-3 text-white cursor-pointer">
                      <input
                        type="checkbox"
                        name="paymentMethods"
                        value={method.value}
                        checked={this.state.formData.paymentMethods.includes(method.value)}
                        onChange={this.handleCheckboxChange}
                        className="w-4 h-4 text-blue-600 bg-white/10 border-white/20 rounded focus:ring-blue-500"
                      />
                      <span className="text-sm">{method.label}</span>
                    </label>
                  ))}
                </div>
              </div>

              {/* Are financing options available? */}
              <div className="mb-6">
                <label className="block text-sm font-medium text-white mb-3">
                  Are financing options available? *
                </label>
                <div className="space-y-2">
                  {SemiConstants.YES_NO_OPTIONS.map((option, index) => (
                    <label key={index} className="flex items-center space-x-3 text-white cursor-pointer">
                      <input
                        type="radio"
                        name="financingOptions"
                        value={option.value}
                        checked={this.state.formData.financingOptions === option.value}
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
                ← Back to Part 4
              </button>
              
              <button
                type="submit"
                className="px-8 py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-xl hover:from-blue-700 hover:to-purple-700 transition-all duration-300 font-medium shadow-lg"
              >
                Continue to Part 6 →
              </button>
            </div>
          </form>
        </div>
      </div>
    );
  }
}

export default EnrollmentFormPart5;