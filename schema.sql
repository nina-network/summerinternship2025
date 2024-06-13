CREATE DATABASE internships;

CREATE TABLE 2025 (
    id SERIAL PRIMARY KEY,
    concentration VARCHAR(255),
    deadline VARCHAR(10),
    role_name VARCHAR(255),
    company VARCHAR(255),
    i_location VARCHAR(255),
    pay INT,
    grade VARCHAR(255),
    site_name VARCHAR(255)
);

INSERT INTO internships(concentration, deadline, role_name, company, i_location, pay, grade, site_name) VALUES ('Software, Systems, and Networks', '07/10/2024', 'Implementation Consultant Intern','Fast Enterprises, LLC', 'Onsite', 25, 'N/A', 'https://careers-fastenterprises.icims.com/jobs/1401/implementation-intern/job'),
('Software Engineering | Software, Systems, and Networks | Data Science | Cybersecurity', '08/20/2024', 'Global Technology Summer Analyst Program', 'Bank of America', 'Onsite (NC, etc.)', 23, 'Junior, Senior', 'https://campus.bankofamerica.com/careers/global_technology_summer_analyst_program__2025.html'),
('Data Science', '06/16/2024', 'Inside Sales & Investment Analyst Co-op', 'E3 Displays LLC', 'Onsite (VA)', 22, 'N/A', 'https://charlotte-csm.symplicity.com/students/app/jobs/detail/653e84eed71b6f7eddc05e4877cde339');