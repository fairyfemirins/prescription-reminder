# Prescription Reminder App

A CLI tool to manage prescriptions, set reminders, check drug interactions, and find pharmacies.

## Features
- **Add Prescriptions**: Store medication details (name, dosage, frequency, start date).
- **Set Reminders**: Schedule reminders for medications.
- **Refill Notifications**: Notify when refills are needed.
- **Drug Interaction Checker**: Warn about potential drug interactions (mock implementation).
- **Pharmacy Locator**: Find nearby pharmacies (mock implementation).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Femirins/prescription-reminder.git
   cd prescription-reminder
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Usage
### Add a Prescription
```bash
python prescription_reminder.py add-prescription --name "Ibuprofen" --dosage "200mg" --frequency "2 times a day" --start-date "2026-05-24"
```

### Set a Reminder
```bash
python prescription_reminder.py set-reminder --name "Ibuprofen" --time "08:00"
```

### Check Refill Status
```bash
python prescription_reminder.py check-refill --name "Ibuprofen"
```

### Check Drug Interactions
```bash
python prescription_reminder.py check-interactions --name "Ibuprofen"
```

### Find Pharmacies
```bash
python prescription_reminder.py find-pharmacy --location "10001"
```

## Testing
Run unit tests:
```bash
python -m pytest tests/test_reminder.py -v
```

## License
This project is licensed under the MIT License.