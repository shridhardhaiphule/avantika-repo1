'use client';

import React from 'react';
import { SemiConstants } from '../constants/SemiConstants';

interface FormData {
  dentalChairs: string;
  treatmentRooms: string;
  dentalTechnologies: string[];
  clinicAccreditation: string;
  infectionControlProtocols: string;
  emergencyEquipment: string;
}

interface EnrollmentFormPart3State {
  formData: FormData;
}

class EnrollmentFormPart3 extends React.Component<Record<string, never>, EnrollmentFormPart3State> {
  constructor(props: Record<string, never>) {
    super(props);
    this.state = {
      formData: {
        dentalChairs: '',
        treatmentRooms: '',
        dentalTechnologies: [],
        clinicAccreditation: '',
        infectionControlProtocols: '',
        emergencyEquipment: ''
      }
    };
  }

  componentDidMount() {
    // Load previous form data if available
    const part1Data = sessionStorage.getItem('enrollmentFormPart1');
    const part2Data = sessionStorage.getItem('enrollmentFormPart2');
    
    if (part1Data) {
      console.log('Part 1 data:', JSON.parse(part1Data));
    }
    if (part2Data) {
      console.log('Part 2 data:', JSON.parse(part2Data));
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
    
    if (name === 'dentalTechnologies') {
      this.setState(prevState => {
        const updatedTechnologies = checked
          ? [...prevState.formData.dentalTechnologies, value]
          : prevState.formData.dentalTechnologies.filter(tech => tech !== value);
        
        return {
          formData: {
            ...prevState.formData,
            dentalTechnologies: updatedTechnologies
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
    if (!this.state.formData.dentalChairs || 
        !this.state.formData.treatmentRooms || 
        !this.state.formData.infectionControlProtocols) {
      alert('Please fill in all required fields.');
      return;
    }

    console.log("Enrollment form part 3 submitted:", this.state.formData);
    
    // Store form data in sessionStorage to pass to part 4
    sessionStorage.setItem('enrollmentFormPart3', JSON.stringify(this.state.formData));
    
    // Navigate to part 4
    window.location.href = '/enrollment_form_part4';
  };

  render() {
    return (
      <div className="min-h-screen bg-gradient-to-br from-purple-900 via-blue-900 to-indigo-900 flex items-center justify-center p-4">
        <div className="w-full max-w-4xl bg-white/10 backdrop-blur-lg rounded-3xl shadow-2xl border border-white/20 p-8">
          <div className="text-center mb-8">
            <h1 className="text-4xl font-bold text-white mb-2">Clinic Enrollment</h1>
            <p className="text-xl text-blue-100">Part 3: Clinic & Facility Information</p>
            <div className="flex justify-center mt-4">
              <div className="flex space-x-2">
                <div className="w-3 h-3 rounded-full bg-green-400"></div>
                <div className="w-3 h-3 rounded-full bg-green-400"></div>
                <div className="w-3 h-3 rounded-full bg-blue-400"></div>
              </div>
            </div>
          </div>

          <form onSubmit={this.handleSubmit} className="space-y-6">
            {/* Clinic & Facility Section */}
            <div className="bg-white/5 rounded-xl p-6 border border-white/10">
              <h2 className="text-2xl font-semibold text-white mb-6 border-b border-white/20 pb-2">
                Clinic & Facility
              </h2>

              {/* Number of Dental Chairs */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                <div>
                  <label htmlFor="dentalChairs" className="block text-sm font-medium text-white mb-2">
                    Number of Dental Chairs *
                  </label>
                  <select
                    id="dentalChairs"
                    name="dentalChairs"
                    value={this.state.formData.dentalChairs}
                    onChange={this.handleInputChange}
                    className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-black placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    required
                  >
                    {SemiConstants.DENTAL_CHAIRS_OPTIONS.map((option, index) => (
                      <option 
                        key={index} 
                        value={option.value} 
                        disabled={option.disabled}
                        className="bg-white text-black"
                      >
                        {option.label}
                      </option>
                    ))}
                  </select>
                </div>

                {/* Number of Treatment Rooms */}
                <div>
                  <label htmlFor="treatmentRooms" className="block text-sm font-medium text-white mb-2">
                    Number of Treatment Rooms *
                  </label>
                  <select
                    id="treatmentRooms"
                    name="treatmentRooms"
                    value={this.state.formData.treatmentRooms}
                    onChange={this.handleInputChange}
                    className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-black placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    required
                  >
                    {SemiConstants.TREATMENT_ROOMS_OPTIONS.map((option, index) => (
                      <option 
                        key={index} 
                        value={option.value} 
                        disabled={option.disabled}
                        className="bg-white text-black"
                      >
                        {option.label}
                      </option>
                    ))}
                  </select>
                </div>
              </div>

              {/* Dental Technologies & Equipment */}
              <div className="mb-6">
                <label className="block text-sm font-medium text-white mb-3">
                  Dental Technologies & Equipment
                </label>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
                  {SemiConstants.DENTAL_TECHNOLOGIES_OPTIONS.map((tech, index) => (
                    <label key={index} className="flex items-center space-x-3 text-white cursor-pointer">
                      <input
                        type="checkbox"
                        name="dentalTechnologies"
                        value={tech.value}
                        checked={this.state.formData.dentalTechnologies.includes(tech.value)}
                        onChange={this.handleCheckboxChange}
                        className="w-4 h-4 text-blue-600 bg-white/10 border-white/20 rounded focus:ring-blue-500"
                      />
                      <span className="text-sm">{tech.label}</span>
                    </label>
                  ))}
                </div>
              </div>

              {/* Clinic Accreditation */}
              <div className="mb-6">
                <label htmlFor="clinicAccreditation" className="block text-sm font-medium text-white mb-2">
                  Clinic Accreditation
                </label>
                <textarea
                  id="clinicAccreditation"
                  name="clinicAccreditation"
                  value={this.state.formData.clinicAccreditation}
                  onChange={this.handleInputChange}
                  rows={4}
                  className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-black placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-vertical"
                  placeholder="Please describe your clinic's accreditations and certifications..."
                />
              </div>

              {/* Infection Control & Sterilization Protocols */}
              <div className="mb-6">
                <label htmlFor="infectionControlProtocols" className="block text-sm font-medium text-white mb-2">
                  Infection Control & Sterilization Protocols *
                </label>
                <textarea
                  id="infectionControlProtocols"
                  name="infectionControlProtocols"
                  value={this.state.formData.infectionControlProtocols}
                  onChange={this.handleInputChange}
                  rows={4}
                  className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-black placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-vertical"
                  placeholder="Please describe your infection control and sterilization protocols..."
                  required
                />
              </div>

              {/* Emergency Medical Equipment */}
              <div className="mb-6">
                <label className="block text-sm font-medium text-white mb-3">
                  Emergency Medical Equipment
                </label>
                <div className="space-y-2">
                  {SemiConstants.EMERGENCY_EQUIPMENT_OPTIONS.map((option, index) => (
                    <label key={index} className="flex items-center space-x-3 text-white cursor-pointer">
                      <input
                        type="radio"
                        name="emergencyEquipment"
                        value={option.value}
                        checked={this.state.formData.emergencyEquipment === option.value}
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
                ← Back to Part 2
              </button>
              
              <button
                type="submit"
                className="px-8 py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-xl hover:from-blue-700 hover:to-purple-700 transition-all duration-300 font-medium shadow-lg"
              >
                Continue to Part 4 →
              </button>
            </div>
          </form>
        </div>
      </div>
    );
  }
}

export default EnrollmentFormPart3;