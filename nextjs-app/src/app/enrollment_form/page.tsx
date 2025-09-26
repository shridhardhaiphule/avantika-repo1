"use client";
import React, { Component } from "react";
import Image from "next/image";
import CountryDateTime from "../components/CountryDateTime";
import Country from "../components/Country";
import YearsInPractice from "../components/YearsInPractice";
import Specialities from "../components/Specialities";

interface EnrollmentFormState {
  formData: {
    fullName: string;
    clinicName: string;
    email: string;
    phone: string;
    clinicAddress: string;
    city: string;
    country: string;
    nearestAirport: string;
    languagesSpoken: string;
    yearsInPractice: string;
    specialities: string[];
  };
}

export default class EnrollmentForm extends Component<object, EnrollmentFormState> {
  constructor(props: object) {
    super(props);
    this.state = {
      formData: {
        fullName: "",
        clinicName: "",
        email: "",
        phone: "",
        clinicAddress: "",
        city: "",
        country: "",
        nearestAirport: "",
        languagesSpoken: "",
        yearsInPractice: "",
        specialities: []
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

  handleSpecialityChange = (speciality: string, checked: boolean) => {
    this.setState(prevState => ({
      formData: {
        ...prevState.formData,
        specialities: checked 
          ? [...prevState.formData.specialities, speciality]
          : prevState.formData.specialities.filter(s => s !== speciality)
      }
    }));
  };

  handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Enrollment form part 1 submitted:", this.state.formData);
    
    // Store form data in sessionStorage to pass to part 2
    sessionStorage.setItem('enrollmentFormPart1', JSON.stringify(this.state.formData));
    
    // Navigate to part 2
    window.location.href = '/enrollment_form_part2';
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
          
          <h1 className="text-3xl font-bold text-center mb-8 bg-gradient-to-r from-purple-600 to-blue-600 bg-clip-text text-transparent">
            Clinic Enrollment Form
          </h1>
          <h2 className="text-xl font-semibold text-center mb-8 text-slate-600">
            Page 1: General Information
          </h2>

          {/* Country DateTime Component */}
          <div className="mb-8">
            <CountryDateTime timezone="IST" />
          </div>

          <form onSubmit={this.handleSubmit} className="space-y-6">
            {/* Full Name */}
            <div>
              <label htmlFor="fullName" className="block text-sm font-medium text-slate-700 mb-2">
                Full Name *
              </label>
              <input
                type="text"
                id="fullName"
                name="fullName"
                value={formData.fullName}
                onChange={this.handleChange}
                required
                className="w-full px-4 py-3 border border-slate-200 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-purple-500 bg-white/70 backdrop-blur-sm text-slate-900 transition-all duration-200 hover:bg-white/90"
                placeholder="Enter your full name"
              />
            </div>

            {/* Clinic Name */}
            <div>
              <label htmlFor="clinicName" className="block text-sm font-medium text-slate-700 mb-2">
                Clinic Name *
              </label>
              <input
                type="text"
                id="clinicName"
                name="clinicName"
                value={formData.clinicName}
                onChange={this.handleChange}
                required
                className="w-full px-4 py-3 border border-slate-200 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-purple-500 bg-white/70 backdrop-blur-sm text-slate-900 transition-all duration-200 hover:bg-white/90"
                placeholder="Enter your clinic name"
              />
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {/* Email Address */}
              <div>
                <label htmlFor="email" className="block text-sm font-medium text-slate-700 mb-2">
                  Email Address *
                </label>
                <input
                  type="email"
                  id="email"
                  name="email"
                  value={formData.email}
                  onChange={this.handleChange}
                  required
                  className="w-full px-4 py-3 border border-slate-200 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-purple-500 bg-white/70 backdrop-blur-sm text-slate-900 transition-all duration-200 hover:bg-white/90"
                  placeholder="Enter your email address"
                />
              </div>

              {/* Phone Number */}
              <div>
                <label htmlFor="phone" className="block text-sm font-medium text-slate-700 mb-2">
                  Phone Number *
                </label>
                <input
                  type="tel"
                  id="phone"
                  name="phone"
                  value={formData.phone}
                  onChange={this.handleChange}
                  required
                  className="w-full px-4 py-3 border border-slate-200 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-purple-500 bg-white/70 backdrop-blur-sm text-slate-900 transition-all duration-200 hover:bg-white/90"
                  placeholder="Enter your phone number"
                />
              </div>
            </div>

            {/* Clinic Address */}
            <div>
              <label htmlFor="clinicAddress" className="block text-sm font-medium text-slate-700 mb-2">
                Clinic Address *
              </label>
              <input
                type="text"
                id="clinicAddress"
                name="clinicAddress"
                value={formData.clinicAddress}
                onChange={this.handleChange}
                required
                className="w-full px-4 py-3 border border-slate-200 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-purple-500 bg-white/70 backdrop-blur-sm text-slate-900 transition-all duration-200 hover:bg-white/90"
                placeholder="Enter your clinic address"
              />
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {/* City */}
              <div>
                <label htmlFor="city" className="block text-sm font-medium text-slate-700 mb-2">
                  City *
                </label>
                <input
                  type="text"
                  id="city"
                  name="city"
                  value={formData.city}
                  onChange={this.handleChange}
                  required
                  className="w-full px-4 py-3 border border-slate-200 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-purple-500 bg-white/70 backdrop-blur-sm text-slate-900 transition-all duration-200 hover:bg-white/90"
                  placeholder="Enter your city"
                />
              </div>

              {/* Country Dropdown */}
              <Country
                inputCountry={formData.country}
                onChange={(value) => this.setState(prevState => ({
                  formData: { ...prevState.formData, country: value }
                }))}
                required={true}
              />
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {/* Nearest Airport */}
              <div>
                <label htmlFor="nearestAirport" className="block text-sm font-medium text-slate-700 mb-2">
                  Nearest Airport
                </label>
                <input
                  type="text"
                  id="nearestAirport"
                  name="nearestAirport"
                  value={formData.nearestAirport}
                  onChange={this.handleChange}
                  className="w-full px-4 py-3 border border-slate-200 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-purple-500 bg-white/70 backdrop-blur-sm text-slate-900 transition-all duration-200 hover:bg-white/90"
                  placeholder="Enter nearest airport"
                />
              </div>

              {/* Languages Spoken */}
              <div>
                <label htmlFor="languagesSpoken" className="block text-sm font-medium text-slate-700 mb-2">
                  Languages Spoken at Clinic
                </label>
                <input
                  type="text"
                  id="languagesSpoken"
                  name="languagesSpoken"
                  value={formData.languagesSpoken}
                  onChange={this.handleChange}
                  className="w-full px-4 py-3 border border-slate-200 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-purple-500 bg-white/70 backdrop-blur-sm text-slate-900 transition-all duration-200 hover:bg-white/90"
                  placeholder="e.g., English, Spanish, French"
                />
              </div>
            </div>

            {/* Years in Practice Dropdown */}
            <YearsInPractice
              inputYears={formData.yearsInPractice}
              onChange={(value) => this.setState(prevState => ({
                formData: { ...prevState.formData, yearsInPractice: value }
              }))}
              required={true}
            />

            {/* Specialities Checkboxes */}
            <Specialities
              selectedSpecialities={formData.specialities}
              onChange={this.handleSpecialityChange}
            />

            <div className="flex gap-4 pt-6">
              <button
                type="submit"
                className="flex-1 bg-gradient-to-r from-purple-600 to-blue-600 hover:from-purple-700 hover:to-blue-700 text-white font-medium py-3 px-6 rounded-xl transition-all duration-300 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2 shadow-lg hover:shadow-xl transform hover:-translate-y-0.5"
              >
                Submit Enrollment
              </button>
              
              <button
                type="button"
                onClick={() => window.history.back()}
                className="flex-1 bg-gradient-to-r from-slate-500 to-slate-600 hover:from-slate-600 hover:to-slate-700 text-white font-medium py-3 px-6 rounded-xl transition-all duration-300 focus:outline-none focus:ring-2 focus:ring-slate-500 focus:ring-offset-2 shadow-lg hover:shadow-xl transform hover:-translate-y-0.5"
              >
                Go Back
              </button>
            </div>
          </form>
        </div>
      </main>
    </div>
    );
  }
}