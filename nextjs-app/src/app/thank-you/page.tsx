'use client';

import React from 'react';
import Link from 'next/link';

interface FormData {
  part1: Record<string, unknown>;
  part2: Record<string, unknown>;
  part3: Record<string, unknown>;
  part4: Record<string, unknown>;
  part5: Record<string, unknown>;
  part6: Record<string, unknown>;
}

interface ThankYouState {
  formData: FormData;
  referenceNumber: string;
  isLoaded: boolean;
}

class ThankYouPage extends React.Component<Record<string, never>, ThankYouState> {
  constructor(props: Record<string, never>) {
    super(props);
    this.state = {
      formData: {
        part1: {},
        part2: {},
        part3: {},
        part4: {},
        part5: {},
        part6: {}
      },
      referenceNumber: `REF-${Date.now()}`,
      isLoaded: false
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

    this.setState({ 
      formData: completeData,
      isLoaded: true
    });

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

  safeStringValue = (value: unknown): string => {
    return typeof value === 'string' && value ? value : 'N/A';
  };

  safeArrayValue = (value: unknown): string[] => {
    return Array.isArray(value) ? value : [];
  };

  formatYesNo = (value: unknown): string => {
    return this.safeStringValue(value) === 'yes' ? 'Yes' : 'No';
  };

  render() {
    const { formData, referenceNumber, isLoaded } = this.state;

    if (!isLoaded) {
      return (
        <div className="min-h-screen bg-gradient-to-br from-purple-900 via-blue-900 to-indigo-900 flex flex-col items-center justify-center px-4">
          <div className="text-white text-2xl">Loading...</div>
        </div>
      );
    }

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
            
            {/* Part 1: General Information */}
            <div className="mb-8">
              <h3 className="text-2xl font-semibold text-blue-200 mb-4 border-b border-blue-300/30 pb-2">
                📋 General Information
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Clinic Name</label>
                  <div className="text-white font-semibold">{this.safeStringValue(formData.part1.clinicName)}</div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Contact Person</label>
                  <div className="text-white font-semibold">{this.safeStringValue(formData.part1.contactPerson)}</div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Email</label>
                  <div className="text-white font-semibold">{this.safeStringValue(formData.part1.email)}</div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Phone</label>
                  <div className="text-white font-semibold">{this.safeStringValue(formData.part1.phone)}</div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Address</label>
                  <div className="text-white font-semibold">{this.safeStringValue(formData.part1.address)}</div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Country</label>
                  <div className="text-white font-semibold">{this.safeStringValue(formData.part1.country)}</div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Years in Practice</label>
                  <div className="text-white font-semibold">{this.safeStringValue(formData.part1.yearsInPractice)}</div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Specialties</label>
                  <div className="text-white font-semibold">
                    {this.safeArrayValue(formData.part1.specialties).join(', ') || 'N/A'}
                  </div>
                </div>
              </div>
            </div>

            {/* Part 2: Qualifications */}
            <div className="mb-8">
              <h3 className="text-2xl font-semibold text-blue-200 mb-4 border-b border-blue-300/30 pb-2">
                🎓 Qualifications & Education
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Primary Qualification</label>
                  <div className="text-white font-semibold">{this.safeStringValue(formData.part2.primaryQualification)}</div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">University</label>
                  <div className="text-white font-semibold">{this.safeStringValue(formData.part2.university)}</div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Graduation Year</label>
                  <div className="text-white font-semibold">{this.safeStringValue(formData.part2.graduationYear)}</div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Additional Certifications</label>
                  <div className="text-white font-semibold">
                    {this.safeArrayValue(formData.part2.additionalCertifications).join(', ') || 'N/A'}
                  </div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20 md:col-span-2">
                  <label className="block text-blue-200 font-medium mb-1">Professional Memberships</label>
                  <div className="text-white font-semibold">
                    {this.safeArrayValue(formData.part2.professionalMemberships).join(', ') || 'N/A'}
                  </div>
                </div>
              </div>
            </div>

            {/* Part 3: Facilities */}
            <div className="mb-8">
              <h3 className="text-2xl font-semibold text-blue-200 mb-4 border-b border-blue-300/30 pb-2">
                🏥 Facilities & Equipment
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Clinic Size</label>
                  <div className="text-white font-semibold">{this.safeStringValue(formData.part3.clinicSize)}</div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Number of Chairs</label>
                  <div className="text-white font-semibold">{this.safeStringValue(formData.part3.numberOfChairs)}</div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">X-ray Equipment</label>
                  <div className="text-white font-semibold">{this.formatYesNo(formData.part3.xrayEquipment)}</div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Digital Records</label>
                  <div className="text-white font-semibold">{this.formatYesNo(formData.part3.digitalRecords)}</div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20 md:col-span-2">
                  <label className="block text-blue-200 font-medium mb-1">Equipment Available</label>
                  <div className="text-white font-semibold">
                    {this.safeArrayValue(formData.part3.equipmentAvailable).join(', ') || 'N/A'}
                  </div>
                </div>
              </div>
            </div>

            {/* Part 4: Services */}
            <div className="mb-8">
              <h3 className="text-2xl font-semibold text-blue-200 mb-4 border-b border-blue-300/30 pb-2">
                🦷 Services Offered
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Emergency Services</label>
                  <div className="text-white font-semibold">{this.formatYesNo(formData.part4.emergencyServices)}</div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Weekend Hours</label>
                  <div className="text-white font-semibold">{this.formatYesNo(formData.part4.weekendHours)}</div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Insurance Accepted</label>
                  <div className="text-white font-semibold">{this.formatYesNo(formData.part4.insuranceAccepted)}</div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Languages Spoken</label>
                  <div className="text-white font-semibold">
                    {this.safeArrayValue(formData.part4.languagesSpoken).join(', ') || 'N/A'}
                  </div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20 md:col-span-2">
                  <label className="block text-blue-200 font-medium mb-1">Treatment Services</label>
                  <div className="text-white font-semibold">
                    {this.safeArrayValue(formData.part4.treatmentServices).join(', ') || 'N/A'}
                  </div>
                </div>
              </div>
            </div>

            {/* Part 5: Pricing */}
            <div className="mb-8">
              <h3 className="text-2xl font-semibold text-blue-200 mb-4 border-b border-blue-300/30 pb-2">
                💰 Pricing & Packages
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Consultation Fee</label>
                  <div className="text-white font-semibold">{this.safeStringValue(formData.part5.consultationFee)}</div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Payment Methods</label>
                  <div className="text-white font-semibold">
                    {this.safeArrayValue(formData.part5.paymentMethods).join(', ') || 'N/A'}
                  </div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Bundled Packages</label>
                  <div className="text-white font-semibold">{this.formatYesNo(formData.part5.bundledPackages)}</div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Follow-up Care Included</label>
                  <div className="text-white font-semibold">{this.formatYesNo(formData.part5.followUpCareIncluded)}</div>
                </div>
              </div>
            </div>

            {/* Part 6: Reviews & Additional Info */}
            <div className="mb-8">
              <h3 className="text-2xl font-semibold text-blue-200 mb-4 border-b border-blue-300/30 pb-2">
                ⭐ Reviews & Additional Information
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Patient Reviews Available</label>
                  <div className="text-white font-semibold">{this.formatYesNo(formData.part6.patientReviewsAvailable)}</div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Average Rating</label>
                  <div className="text-white font-semibold">{this.safeStringValue(formData.part6.averageRating)}</div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Website</label>
                  <div className="text-white font-semibold">{this.safeStringValue(formData.part6.website)}</div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20">
                  <label className="block text-blue-200 font-medium mb-1">Social Media</label>
                  <div className="text-white font-semibold">
                    {this.safeArrayValue(formData.part6.socialMediaPresence).join(', ') || 'N/A'}
                  </div>
                </div>
                <div className="bg-white/10 rounded-lg p-4 border border-white/20 md:col-span-2">
                  <label className="block text-blue-200 font-medium mb-1">Additional Information</label>
                  <div className="text-white font-semibold">{this.safeStringValue(formData.part6.additionalInfo)}</div>
                </div>
              </div>
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