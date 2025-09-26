"use client";
import React, { Component } from 'react';
import { SemiConstants } from '../constants/SemiConstants';

interface SpecialitiesProps {
  selectedSpecialities: string[];
  onChange?: (speciality: string, checked: boolean) => void;
  className?: string;
}

class Specialities extends Component<SpecialitiesProps> {
  handleSpecialityChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { value, checked } = e.target;
    if (this.props.onChange) {
      this.props.onChange(value, checked);
    }
  };

  render() {
    const { selectedSpecialities = [], className = "" } = this.props;

    return (
      <div className={className}>
        <label className="block text-sm font-medium text-slate-700 mb-3">
          Specialities *
        </label>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
          {SemiConstants.SPECIALITIES_DATA.map((speciality, index) => (
            <div key={index} className="flex items-center">
              <input
                type="checkbox"
                id={`speciality-${speciality.value}`}
                name="specialities"
                value={speciality.value}
                checked={selectedSpecialities.includes(speciality.value)}
                onChange={this.handleSpecialityChange}
                className="h-4 w-4 text-purple-600 focus:ring-purple-500 border-slate-300 rounded"
              />
              <label 
                htmlFor={`speciality-${speciality.value}`} 
                className="ml-3 text-sm text-slate-700 cursor-pointer"
              >
                {speciality.label}
              </label>
            </div>
          ))}
        </div>
      </div>
    );
  }
}

export default Specialities;