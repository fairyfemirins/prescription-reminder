#!/usr/bin/env python3
"""
Prescription Reminder App
A CLI tool to manage prescriptions, set reminders, check drug interactions, and find pharmacies.
"""

import click
import json
import os
from datetime import datetime, timedelta

# File to store prescription data
DATA_FILE = os.path.expanduser("~/.prescription_reminder_data.json")


def load_data():
    """Load prescription data from file."""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    """Save prescription data to file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def add_prescription_logic(name, dosage, frequency, start_date):
    """Core logic for adding a prescription."""
    data = load_data()
    prescriptions = data.get("prescriptions", [])
    
    prescription = {
        "name": name,
        "dosage": dosage,
        "frequency": frequency,
        "start_date": start_date,
        "reminders": [],
        "refill_date": (datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=30)).strftime("%Y-%m-%d"),
    }
    
    prescriptions.append(prescription)
    data["prescriptions"] = prescriptions
    save_data(data)
    return prescription


def set_reminder_logic(name, time):
    """Core logic for setting a reminder."""
    data = load_data()
    prescriptions = data.get("prescriptions", [])
    
    for prescription in prescriptions:
        if prescription["name"] == name:
            prescription["reminders"].append(time)
            save_data(data)
            return True
    
    return False


def check_refill_logic(name):
    """Core logic for checking refill status."""
    data = load_data()
    prescriptions = data.get("prescriptions", [])
    
    for prescription in prescriptions:
        if prescription["name"] == name:
            refill_date = prescription["refill_date"]
            today = datetime.now().strftime("%Y-%m-%d")
            return refill_date <= today, refill_date
    
    return None, None


@click.group()
def cli():
    """Prescription Reminder App"""
    pass


@cli.command()
@click.option("--name", prompt="Medication name", help="Name of the medication")
@click.option("--dosage", prompt="Dosage (e.g., 500mg)", help="Dosage of the medication")
@click.option("--frequency", prompt="Frequency (e.g., 2 times a day)", help="How often to take the medication")
@click.option("--start-date", prompt="Start date (YYYY-MM-DD)", help="Start date of the prescription")
def add_prescription(name, dosage, frequency, start_date):
    """Add a new prescription."""
    add_prescription_logic(name, dosage, frequency, start_date)
    click.echo(f"Added prescription: {name}")


@cli.command()
@click.option("--name", prompt="Medication name", help="Name of the medication to set a reminder for")
@click.option("--time", prompt="Reminder time (HH:MM)", help="Time for the reminder")
def set_reminder(name, time):
    """Set a reminder for a prescription."""
    if set_reminder_logic(name, time):
        click.echo(f"Reminder set for {name} at {time}")
    else:
        click.echo(f"Prescription not found: {name}")


@cli.command()
@click.option("--name", prompt="Medication name", help="Name of the medication to check refill")
def check_refill(name):
    """Check if a prescription needs a refill."""
    needs_refill, refill_date = check_refill_logic(name)
    if needs_refill is None:
        click.echo(f"Prescription not found: {name}")
    elif needs_refill:
        click.echo(f"Refill needed for {name} (Refill date: {refill_date})")
    else:
        click.echo(f"No refill needed for {name} until {refill_date}")


@cli.command()
@click.option("--name", prompt="Medication name", help="Name of the medication to check interactions")
def check_interactions(name):
    """Check for drug interactions (mock implementation)."""
    click.echo(f"No interactions found for {name} (mock response)")


@cli.command()
@click.option("--location", prompt="Your location (e.g., ZIP code)", help="Your location to find nearby pharmacies")
def find_pharmacy(location):
    """Find nearby pharmacies (mock implementation)."""
    click.echo(f"Pharmacies near {location}: CVS, Walgreens, Rite Aid (mock response)")


if __name__ == "__main__":
    cli()