#!/usr/bin/env python3
"""
Unit tests for the Prescription Reminder App.
"""

import json
import os
import pytest
from datetime import datetime, timedelta
from prescription_reminder import (
    load_data,
    save_data,
    add_prescription_logic,
    set_reminder_logic,
    check_refill_logic,
)

# Mock data file for testing
TEST_DATA_FILE = os.path.expanduser("~/.test_prescription_reminder_data.json")


@pytest.fixture(autouse=True)
def mock_data_file(monkeypatch):
    """Mock the data file for testing."""
    monkeypatch.setattr("prescription_reminder.DATA_FILE", TEST_DATA_FILE)
    
    # Clean up before and after tests
    if os.path.exists(TEST_DATA_FILE):
        os.remove(TEST_DATA_FILE)
    yield
    if os.path.exists(TEST_DATA_FILE):
        os.remove(TEST_DATA_FILE)


def test_add_prescription_logic():
    """Test adding a prescription."""
    prescription = add_prescription_logic("Aspirin", "100mg", "1 time a day", "2026-05-24")
    assert prescription["name"] == "Aspirin"
    data = load_data()
    assert len(data["prescriptions"]) == 1


def test_set_reminder_logic():
    """Test setting a reminder."""
    add_prescription_logic("Aspirin", "100mg", "1 time a day", "2026-05-24")
    result = set_reminder_logic("Aspirin", "09:00")
    assert result is True
    data = load_data()
    assert "09:00" in data["prescriptions"][0]["reminders"]


def test_check_refill_logic():
    """Test checking refill status."""
    add_prescription_logic("Aspirin", "100mg", "1 time a day", "2026-05-24")
    needs_refill, refill_date = check_refill_logic("Aspirin")
    assert needs_refill is False
    assert refill_date == (datetime.strptime("2026-05-24", "%Y-%m-%d") + timedelta(days=30)).strftime("%Y-%m-%d")