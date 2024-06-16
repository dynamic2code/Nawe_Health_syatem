# Donation Tracker

## Overview
Donation Tracker is a comprehensive platform designed to streamline the process of blood, kidney, and other critical donations. This platform provides functionalities for tracking donations, managing documentation, and communicating with donors. It aims to enhance the efficiency and transparency of the donation process while ensuring the safety and privacy of donors and recipients.

## Features

### User Registration and Authentication
- Secure user registration for donors and administrators
- Login and logout functionality
- Profile management

### Donation Tracking
- Track blood, kidney, and other types of donations
- Historical donation records for donors

### Documentation Management
- Upload and manage necessary documents for donations
- Secure document storage with access control

### Communication Tools
- Automated email and sms notifications and reminders for donors
- Direct messaging between donors and administrators
- Updates and alerts about donation campaigns and drives

### Search and Matching
- Search for eligible donors based on blood type, location, and other criteria
- Match donors with recipients based on medical compatibility
- Real-time availability status of donors

### Donation Campaigns and Drives
- Create and manage donation campaigns
- Track campaign progress and donor participation
- Publicize campaigns through integrated social media tools

### Reporting and Analytics
- Generate detailed reports on donation statistics
- Analyze donor demographics and trends
- Monitor the impact and success of donation drives

## Installation

To get started with Donation Tracker, follow these steps:

### Prerequisites
- Python 3.8 or higher
- Django 3.2 or higher
- PostgreSQL or SQLite

### Steps
1. **Clone the repository**
    ```sh
    git clone https://github.com/dynamic2code/donation_tracking.git
    cd donation-tracker
    ```

2. **Create a virtual environment**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure the database**
    - Set up PostgreSQL (or use SQLite for development)
    - Update `DATABASES` settings in `settings.py`

5. **Apply migrations**
    ```sh
    python manage.py migrate
    ```

6. **Create a superuser**
    ```sh
    python manage.py createsuperuser
    ```

7. **Run the server**
    ```sh
    python manage.py runserver
    ```

8. **Access the application**
    Open your browser and navigate to `http://127.0.0.1:8000`

## Usage

### Donors
- Register and log in to the platform.
- Complete your profile and health details.
- Track the status of your donations.
- Receive notifications and reminders about upcoming donation drives.

### Administrators
- Manage donor information and verify eligibility.
- Coordinate donation campaigns and drives.
- Communicate with donors and provide necessary updates.
- Access reports and analytics to monitor progress and impact.

## Contributing

We welcome contributions from the community. If you want to contribute to Donation Tracker, please follow these steps:

1. **Fork the repository**
2. **Create a new branch**
    ```sh
    git checkout -b feature/your-feature-name
    ```
3. **Make your changes**
4. **Commit your changes**
    ```sh
    git commit -m 'Add some feature'
    ```
5. **Push to the branch**
    ```sh
    git push origin feature/your-feature-name
    ```
6. **Create a pull request**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

We would like to thank all the donors and contributors who made this project possible. Your support and dedication are invaluable.

## Contact

If you have any questions or need further assistance, please contact us at support@donationtracker.com.

