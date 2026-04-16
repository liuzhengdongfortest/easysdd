# quality-check.py

import os
import sys

def check_code_quality(directory):
    # Placeholder for code quality checks
    print(f"Checking code quality in directory: {directory}")
    # Implement code quality checks here
    # For example, check for linting errors, code complexity, etc.

def analyze_project_health(directory):
    # Placeholder for project health analysis
    print(f"Analyzing project health in directory: {directory}")
    # Implement project health checks here
    # For example, check for outdated dependencies, test coverage, etc.

def main():
    if len(sys.argv) != 2:
        print("Usage: python quality-check.py <directory>")
        sys.exit(1)

    project_directory = sys.argv[1]

    if not os.path.isdir(project_directory):
        print(f"Error: {project_directory} is not a valid directory.")
        sys.exit(1)

    check_code_quality(project_directory)
    analyze_project_health(project_directory)

if __name__ == "__main__":
    main()