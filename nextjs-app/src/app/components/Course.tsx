"use client";
import React, { Component } from 'react';
import { SemiConstants } from '../constants/SemiConstants';

interface CourseProps {
  inputCourse: string;
  onChange?: (value: string) => void;
  required?: boolean;
  className?: string;
}

interface CourseState {
  selectedCourse: string;
}

class Course extends Component<CourseProps, CourseState> {
  constructor(props: CourseProps) {
    super(props);
    this.state = {
      selectedCourse: props.inputCourse || ""
    };
  }

  componentDidUpdate(prevProps: CourseProps) {
    // Update local state if inputCourse prop changes
    if (prevProps.inputCourse !== this.props.inputCourse) {
      this.setState({
        selectedCourse: this.props.inputCourse
      });
    }
  }

  handleCourseChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const value = e.target.value;
    this.setState({
      selectedCourse: value
    });

    // Call parent onChange if provided
    if (this.props.onChange) {
      this.props.onChange(value);
    }
  };

  render() {
    const { required = false, className = "" } = this.props;
    const { selectedCourse } = this.state;

    return (
      <div>
        <label htmlFor="course" className="block text-sm font-medium text-slate-700 mb-2">
          Select Course *
        </label>
        <select
          id="course"
          name="course"
          value={selectedCourse}
          onChange={this.handleCourseChange}
          required={required}
          className={`w-full px-4 py-3 border border-slate-200 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-purple-500 bg-white/70 backdrop-blur-sm text-slate-900 transition-all duration-200 hover:bg-white/90 ${className}`}
        >
          {SemiConstants.COURSE_DATA.map((course, index) => (
            <option 
              key={index} 
              value={course.value} 
              disabled={course.disabled}
            >
              {course.label}
            </option>
          ))}
        </select>
      </div>
    );
  }
}

export default Course;