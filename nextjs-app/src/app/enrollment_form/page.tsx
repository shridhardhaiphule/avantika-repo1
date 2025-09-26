"use client";
import React, { Component } from "react";
import Image from "next/image";
import CountryDateTime from "../components/CountryDateTime";
import Course from "../components/Course";
import Countries from "../components/Countries";


interface EnrollmentFormState {
  formData: {
    firstName: string;
    lastName: string;
    email: string;
    phone: string;
    course: string;
    comments: string;
    country: string;
  };
}

export default class EnrollmentForm extends Component<object, EnrollmentFormState> {
  constructor(props: object) {
    super(props);
    this.state = {
      formData: {
        firstName: "",
        lastName: "",
        email: "",
        phone: "",
        course: "ui-ux-design",
        comments: "",
        country: "India"
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

  handleCourseChange = (courseValue: string) => {
    this.setState(prevState => ({
      formData: {
        ...prevState.formData,
        course: courseValue
      }
    }));
  };

  handleCountryChange = (countryValue: string) => {
    this.setState(prevState => ({
      formData: {
        ...prevState.formData,
        country: countryValue
      }
    }));
  }

  handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Enrollment form submitted:", this.state.formData);
    // Handle form submission here
    alert("Enrollment form submitted successfully!");
  };

  render() {
    const { formData } = this.state;
    
    return (
    <div className="font-sans min-h-screen p-8 pb-20 gap-16 sm:p-20 bg-white">
      <main className="max-w-2xl mx-auto">
        <div className="bg-white rounded-lg shadow-lg p-8">
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
          
          <h1 className="text-3xl font-bold text-center mb-8 text-gray-900">
            Course Enrollment Form
          </h1>

          {/* Country DateTime Component */}
          <div className="mb-8">
            <CountryDateTime timezone="IST" />
          </div>

          <form onSubmit={this.handleSubmit} className="space-y-6">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label htmlFor="firstName" className="block text-sm font-medium text-gray-700 mb-2">
                  First Name *
                </label>
                <input
                  type="text"
                  id="firstName"
                  name="firstName"
                  value={formData.firstName}
                  onChange={this.handleChange}
                  required
                  className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white text-gray-900"
                  placeholder="Enter your first name"
                />
              </div>

              <div>
                <label htmlFor="lastName" className="block text-sm font-medium text-gray-700 mb-2">
                  Last Name *
                </label>
                <input
                  type="text"
                  id="lastName"
                  name="lastName"
                  value={formData.lastName}
                  onChange={this.handleChange}
                  required
                  className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white text-gray-900"
                  placeholder="Enter your last name"
                />
              </div>
            </div>

            <div>
              <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-2">
                Email Address *
              </label>
              <input
                type="email"
                id="email"
                name="email"
                value={formData.email}
                onChange={this.handleChange}
                required
                className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white text-gray-900"
                placeholder="Enter your email address"
              />
            </div>

            <div>
              <label htmlFor="phone" className="block text-sm font-medium text-gray-700 mb-2">
                Phone Number
              </label>
              <input
                type="tel"
                id="phone"
                name="phone"
                value={formData.phone}
                onChange={this.handleChange}
                className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white text-gray-900"
                placeholder="Enter your phone number"
              />
            </div>

            <Course
              inputCourse={formData.course}
              onChange={this.handleCourseChange}
              required={true}
            />

            {/* Countries Component */}
            <div>
              <label htmlFor="Country" className="block text-sm font-medium text-gray-700 mb-2">
                Select Country *
              </label>
              <Countries
                selectedCountry={formData.country}
                onCountryChange={this.handleCountryChange}
              />
            </div>

            <div>
              <label htmlFor="comments" className="block text-sm font-medium text-gray-700 mb-2">
                Additional Comments
              </label>
              <textarea
                id="comments"
                name="comments"
                value={formData.comments}
                onChange={this.handleChange}
                rows={4}
                className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white text-gray-900"
                placeholder="Any additional information or questions..."
              />
            </div>

            <div className="flex gap-4 pt-6">
              <button
                type="submit"
                className="flex-1 bg-blue-600 hover:bg-blue-700 text-white font-medium py-3 px-6 rounded-md transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
              >
                Submit Enrollment
              </button>
              
              <button
                type="button"
                onClick={() => window.history.back()}
                className="flex-1 bg-gray-600 hover:bg-gray-700 text-white font-medium py-3 px-6 rounded-md transition-colors focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-2"
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