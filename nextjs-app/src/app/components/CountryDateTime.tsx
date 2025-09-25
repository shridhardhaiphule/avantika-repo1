"use client";
import React, { Component } from 'react';

interface CountryDateTimeProps {
  timezone?: string;
}

interface CountryDateTimeState {
  currentTime: string;
  currentDate: string;
}

class CountryDateTime extends Component<CountryDateTimeProps, CountryDateTimeState> {
  private intervalId: NodeJS.Timeout | null = null;

  // Timezone mappings
  private timezoneMap: Record<string, string> = {
    'IST': 'Asia/Kolkata',
    'GMT': 'GMT',
    'EST': 'America/New_York',
    'PST': 'America/Los_Angeles'
  };

  constructor(props: CountryDateTimeProps) {
    super(props);
    this.state = {
      currentTime: '',
      currentDate: ''
    };
  }

  componentDidMount() {
    this.updateTime();
    // Update time every second
    this.intervalId = setInterval(() => {
      this.updateTime();
    }, 1000);
  }

  componentWillUnmount() {
    if (this.intervalId) {
      clearInterval(this.intervalId);
    }
  }

  updateTime = () => {
    const { timezone = 'IST' } = this.props;
    const timezoneString = this.timezoneMap[timezone] || timezone;
    
    try {
      const now = new Date();
      
      // Format time
      const timeOptions: Intl.DateTimeFormatOptions = {
        timeZone: timezoneString,
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: true
      };
      
      // Format date
      const dateOptions: Intl.DateTimeFormatOptions = {
        timeZone: timezoneString,
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      };
      
      const formattedTime = now.toLocaleTimeString('en-US', timeOptions);
      const formattedDate = now.toLocaleDateString('en-US', dateOptions);
      
      this.setState({
        currentTime: formattedTime,
        currentDate: formattedDate
      });
    } catch (error) {
      console.error('Error formatting time:', error);
      this.setState({
        currentTime: 'Error loading time',
        currentDate: 'Error loading date'
      });
    }
  };

  getTimezoneDisplayName = (timezone: string): string => {
    const displayNames: Record<string, string> = {
      'IST': 'Indian Standard Time',
      'GMT': 'Greenwich Mean Time',
      'EST': 'Eastern Standard Time',
      'PST': 'Pacific Standard Time'
    };
    return displayNames[timezone] || timezone;
  };

  render() {
    const { timezone = 'IST' } = this.props;
    const { currentTime, currentDate } = this.state;

    return (
      <div className="bg-gradient-to-r from-blue-50 to-indigo-50 border border-blue-200 rounded-lg p-4 shadow-sm">
        <div className="text-center">
          <h3 className="text-lg font-semibold text-blue-900 mb-2">
            Current Time - {timezone}
          </h3>
          <p className="text-sm text-blue-700 mb-3">
            {this.getTimezoneDisplayName(timezone)}
          </p>
          
          <div className="space-y-2">
            <div className="bg-white rounded-md p-3 shadow-sm">
              <p className="text-xs text-gray-500 uppercase tracking-wide mb-1">Date</p>
              <p className="text-lg font-medium text-gray-900">{currentDate}</p>
            </div>
            
            <div className="bg-white rounded-md p-3 shadow-sm">
              <p className="text-xs text-gray-500 uppercase tracking-wide mb-1">Time</p>
              <p className="text-2xl font-bold text-blue-600 font-mono">{currentTime}</p>
            </div>
          </div>
          
          <div className="mt-3 text-xs text-gray-500">
            Updates every second
          </div>
        </div>
      </div>
    );
  }
}

export default CountryDateTime;