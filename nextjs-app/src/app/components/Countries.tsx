import React from 'react';
import countries from "../../../data/countries.json";

interface Country {
    short_name: string;
    long_name: string;
}

interface CountriesProps {
    selectedCountry: string;
    onCountryChange: (value: string) => void;
    }

class Countries extends React.Component<CountriesProps> {
    render() {
        const { selectedCountry, onCountryChange } = this.props;
        return (
            <select
                value={selectedCountry}
                onChange={(e) => onCountryChange(e.target.value)}
                className="border border-gray-300 rounded p-2 w-full"
            >
                <option value="">Select Country</option>
                {(countries as Country[]).map((country) => (
                    <option key={country.short_name} value={country.long_name}>
                        {country.long_name}
                    </option>
                ))}
            </select>
        );
    }
}

export default Countries;
