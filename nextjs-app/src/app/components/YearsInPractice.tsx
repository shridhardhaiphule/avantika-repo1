"use client";
import React, { Component } from 'react';
import { SemiConstants } from '../constants/SemiConstants';

interface YearsInPracticeProps {
  inputYears: string;
  onChange?: (value: string) => void;
  required?: boolean;
  className?: string;
}

interface YearsInPracticeState {
  selectedYears: string;
}

class YearsInPractice extends Component<YearsInPracticeProps, YearsInPracticeState> {
  constructor(props: YearsInPracticeProps) {
    super(props);
    this.state = {
      selectedYears: props.inputYears || ""
    };
  }

  componentDidUpdate(prevProps: YearsInPracticeProps) {
    if (prevProps.inputYears !== this.props.inputYears) {
      this.setState({
        selectedYears: this.props.inputYears
      });
    }
  }

  handleYearsChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const value = e.target.value;
    this.setState({
      selectedYears: value
    });

    if (this.props.onChange) {
      this.props.onChange(value);
    }
  };

  render() {
    const { required = false, className = "" } = this.props;
    const { selectedYears } = this.state;

    return (
      <div>
        <label htmlFor="yearsInPractice" className="block text-sm font-medium text-slate-700 mb-2">
          Years in Practice *
        </label>
        <select
          id="yearsInPractice"
          name="yearsInPractice"
          value={selectedYears}
          onChange={this.handleYearsChange}
          required={required}
          className={`w-full px-4 py-3 border border-slate-200 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-purple-500 bg-white/70 backdrop-blur-sm text-slate-900 transition-all duration-200 hover:bg-white/90 ${className}`}
        >
          {SemiConstants.YEARS_IN_PRACTICE_DATA.map((years, index) => (
            <option 
              key={index} 
              value={years.value} 
              disabled={years.disabled}
            >
              {years.label}
            </option>
          ))}
        </select>
      </div>
    );
  }
}

export default YearsInPractice;