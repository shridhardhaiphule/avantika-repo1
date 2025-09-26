"use client";
import React, { Component } from 'react';
import { SemiConstants } from '../constants/SemiConstants';

interface CountryProps {
  inputCountry: string;
  onChange?: (value: string) => void;
  required?: boolean;
  className?: string;
}

interface CountryState {
  selectedCountry: string;
}

class Country extends Component<CountryProps, CountryState> {
  constructor(props: CountryProps) {
    super(props);
    this.state = {
      selectedCountry: props.inputCountry || ""
    };
  }

  componentDidUpdate(prevProps: CountryProps) {
    if (prevProps.inputCountry !== this.props.inputCountry) {
      this.setState({
        selectedCountry: this.props.inputCountry
      });
    }
  }

  handleCountryChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const value = e.target.value;
    this.setState({
      selectedCountry: value
    });

    if (this.props.onChange) {
      this.props.onChange(value);
    }
  };

  render() {
    const { required = false, className = "" } = this.props;
    const { selectedCountry } = this.state;

    return (
      <div>
        <label htmlFor="country" className="block text-sm font-medium text-slate-700 mb-2">
          Country *
        </label>
        <select
          id="country"
          name="country"
          value={selectedCountry}
          onChange={this.handleCountryChange}
          required={required}
          className={`w-full px-4 py-3 border border-slate-200 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-purple-500 bg-white/70 backdrop-blur-sm text-slate-900 transition-all duration-200 hover:bg-white/90 ${className}`}
        >
          {SemiConstants.COUNTRY_DATA.map((country, index) => (
            <option 
              key={index} 
              value={country.value} 
              disabled={country.disabled}
            >
              {country.label}
            </option>
          ))}
        </select>
      </div>
    );
  }
}

export default Country;