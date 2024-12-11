#!/bin/bash

# Get battery information using acpi
BATTERY_INFO=$(acpi -b)

# Extract percentage from the output
BATTERY_PERCENTAGE=$(echo "$BATTERY_INFO" | grep -oP '\d+%' | head -1)

# Display the battery percentage
echo $BATTERY_PERCENTAGE

