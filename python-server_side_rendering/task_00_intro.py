#!/usr/bin/env python3
"""
Task 0 - Simple Templating Program
Generates personalized invitation files from a template string and attendee data.
"""

import os


def generate_invitations(template, attendees):
    """Generate personalized invitation files based on a template and a list of attendees.

    Args:
        template (str): The invitation template with placeholders.
        attendees (list): A list of dictionaries containing attendee info.

    Returns:
        None
    """

    # --- Validate input types ---
    if not isinstance(template, str):
        print("Error: Invalid input type for template. Expected a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Invalid input type for attendees. Expected a list of dictionaries.")
        return

    # --- Handle empty inputs ---
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # --- Process each attendee ---
    for idx, attendee in enumerate(attendees, start=1):
        # Create a copy of the template for each attendee
        output_content = template

        # Expected placeholders
        placeholders = ["name", "event_title", "event_date", "event_location"]

        for key in placeholders:
            # Get value or "N/A" if missing or None
            value = attendee.get(key, "N/A")
            if value is None or str(value).strip() == "":
                value = "N/A"
            output_content = output_content.replace("{" + key + "}", str(value))

        # --- Write to output file ---
        output_filename = f"output_{idx}.txt"

        try:
            with open(output_filename, "w", encoding="utf-8") as file:
                file.write(output_content)
            print(f"Generated {output_filename}")
        except Exception as e:
            print(f"Error writing to {output_filename}: {e}")
