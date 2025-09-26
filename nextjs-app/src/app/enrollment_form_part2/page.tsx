"use client";
import React, { Component } from "react";
import Image from "next/image";
import CountryDateTime from "../components/CountryDateTime";
import { SemiConstants } from "../constants/SemiConstants";

interface EnrollmentFormPart2State {
  formData: {
    isLicensed: string;
    licenseNumber: string;
    issuingAuthority: string;
    internationalAccreditations: string[];
    hasContinuingEducation: string;
  };
}

export default class EnrollmentFormPart2 extends Component<object, EnrollmentFormPart2State> {
  constructor(props: object) {
    super(props);
    this.state = {
      formData: {
        isLicensed: "",
        licenseNumber: "",
        issuingAuthority: "",
        internationalAccreditations: [],
        hasContinuingEducation: ""
      }
    };
  }

  handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    this.setState(prevState => ({
      formData: {
        ...prevState.formData,
        [name]: value
      }
    }));
  };

  handleRadioChange = (name: string, value: string) => {
    this.setState(prevState => ({
      formData: {
        ...prevState.formData,
        [name]: value
      }
    }));
  };

  handleAccreditationChange = (accreditation: string, checked: boolean) => {
    this.setState(prevState => {
      let newAccreditations = [...prevState.formData.internationalAccreditations];
      
      // If "None" is selected, clear all other selections
      if (accreditation === "None" && checked) {
        newAccreditations = ["None"];
      } 
      // If any other accreditation is selected, remove "None"
      else if (accreditation !== "None" && checked) {
        newAccreditations = newAccreditations.filter(acc => acc !== "None");
        newAccreditations.push(accreditation);
      } 
      // If unchecking an item
      else if (!checked) {
        newAccreditations = newAccreditations.filter(acc => acc !== accreditation);
      }

      return {
        formData: {
          ...prevState.formData,
          internationalAccreditations: newAccreditations
        }
      };
    });
  };

  handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Enrollment form part 2 submitted:", this.state.formData);
    
    // Store form data in sessionStorage to pass to part 3
    sessionStorage.setItem('enrollmentFormPart2', JSON.stringify(this.state.formData));
    
    // Navigate to part 3
    window.location.href = '/enrollment_form_part3';
  };

  handleGoBack = () => {
    window.history.back();
  };

  render() {
    const { formData } = this.state;
    
    return (
      <div className="font-sans min-h-screen p-8 pb-20 gap-16 sm:p-20 bg-gradient-to-br from-purple-50 via-blue-50 to-indigo-100">
        <main className="max-w-2xl mx-auto">
          <div className="bg-white/90 backdrop-blur-sm rounded-2xl shadow-2xl border border-white/20 p-8">
            <div className="flex items-center justify-center mb-8">
              <Image
                className="dark:invert mr-4"
                src="/next.svg"
                alt="Next.js logo"
                width={120}
                height={25}
                priority
              />
            </div>
            
            <h1 className="text-3xl font-bold text-center mb-4 bg-gradient-to-r from-purple-600 to-blue-600 bg-clip-text text-transparent">
              Clinic Enrollment Form
            </h1>
            <h2 className="text-xl font-semibold text-center mb-8 text-slate-600">
              Page 2: Qualifications & Licensing
            </h2>

            {/* Country DateTime Component */}
            <div className="mb-8">
              <CountryDateTime timezone="IST" />
            </div>

            <form onSubmit={this.handleSubmit} className="space-y-6">
              
              {/* Licensed to Practice Dentistry */}
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-3">
                  Are you licensed to practice dentistry in your country? *
                </label>
                <div className="flex space-x-6">
                  {SemiConstants.YES_NO_OPTIONS.map((option, index) => (
                    <div key={index} className="flex items-center">
                      <input
                        type="radio"
                        id={`licensed-${option.value}`}
                        name="isLicensed"
                        value={option.value}
                        checked={formData.isLicensed === option.value}
                        onChange={(e) => this.handleRadioChange("isLicensed", e.target.value)}
                        required
                        className="h-4 w-4 text-purple-600 focus:ring-purple-500 border-slate-300"
                      />
                      <label 
                        htmlFor={`licensed-${option.value}`} 
                        className="ml-3 text-sm text-slate-700 cursor-pointer"
                      >
                        {option.label}
                      </label>
                    </div>
                  ))}
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {/* License Number */}
                <div>
                  <label htmlFor="licenseNumber" className="block text-sm font-medium text-slate-700 mb-2">
                    License Number
                  </label>
                  <input
                    type="text"
                    id="licenseNumber"
                    name="licenseNumber"
                    value={formData.licenseNumber}
                    onChange={this.handleChange}
                    className="w-full px-4 py-3 border border-slate-200 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-purple-500 bg-white/70 backdrop-blur-sm text-slate-900 transition-all duration-200 hover:bg-white/90"
                    placeholder="Enter your license number"
                  />
                </div>

                {/* Issuing Authority */}
                <div>
                  <label htmlFor="issuingAuthority" className="block text-sm font-medium text-slate-700 mb-2">
                    Issuing Authority
                  </label>
                  <input
                    type="text"
                    id="issuingAuthority"
                    name="issuingAuthority"
                    value={formData.issuingAuthority}
                    onChange={this.handleChange}
                    className="w-full px-4 py-3 border border-slate-200 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-purple-500 bg-white/70 backdrop-blur-sm text-slate-900 transition-all duration-200 hover:bg-white/90"
                    placeholder="Enter issuing authority"
                  />
                </div>
              </div>

              {/* International Accreditations */}
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-3">
                  International Accreditations
                </label>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                  {SemiConstants.INTERNATIONAL_ACCREDITATIONS.map((accreditation, index) => (
                    <div key={index} className="flex items-center">
                      <input
                        type="checkbox"
                        id={`accreditation-${accreditation.value}`}
                        name="internationalAccreditations"
                        value={accreditation.value}
                        checked={formData.internationalAccreditations.includes(accreditation.value)}
                        onChange={(e) => this.handleAccreditationChange(accreditation.value, e.target.checked)}
                        className="h-4 w-4 text-purple-600 focus:ring-purple-500 border-slate-300 rounded"
                      />
                      <label 
                        htmlFor={`accreditation-${accreditation.value}`} 
                        className="ml-3 text-sm text-slate-700 cursor-pointer"
                      >
                        {accreditation.label}
                      </label>
                    </div>
                  ))}
                </div>
              </div>

              {/* Continuing Education */}
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-3">
                  Do you undergo regular continuing education? *
                </label>
                <div className="flex space-x-6">
                  {SemiConstants.YES_NO_OPTIONS.map((option, index) => (
                    <div key={index} className="flex items-center">
                      <input
                        type="radio"
                        id={`education-${option.value}`}
                        name="hasContinuingEducation"
                        value={option.value}
                        checked={formData.hasContinuingEducation === option.value}
                        onChange={(e) => this.handleRadioChange("hasContinuingEducation", e.target.value)}
                        required
                        className="h-4 w-4 text-purple-600 focus:ring-purple-500 border-slate-300"
                      />
                      <label 
                        htmlFor={`education-${option.value}`} 
                        className="ml-3 text-sm text-slate-700 cursor-pointer"
                      >
                        {option.label}
                      </label>
                    </div>
                  ))}
                </div>
              </div>

              <div className="flex gap-4 pt-6">
                <button
                  type="button"
                  onClick={this.handleGoBack}
                  className="flex-1 bg-gradient-to-r from-slate-500 to-slate-600 hover:from-slate-600 hover:to-slate-700 text-white font-medium py-3 px-6 rounded-xl transition-all duration-300 focus:outline-none focus:ring-2 focus:ring-slate-500 focus:ring-offset-2 shadow-lg hover:shadow-xl transform hover:-translate-y-0.5"
                >
                  Go Back
                </button>
                
                <button
                  type="submit"
                  className="flex-1 bg-gradient-to-r from-purple-600 to-blue-600 hover:from-purple-700 hover:to-blue-700 text-white font-medium py-3 px-6 rounded-xl transition-all duration-300 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2 shadow-lg hover:shadow-xl transform hover:-translate-y-0.5"
                >
                  Continue to Part 3 →
                </button>
              </div>
            </form>
          </div>
        </main>
      </div>
    );
  }
}