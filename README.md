# Sensor Streaming Backend

## Overview
This backend processes and serves real-time engine temperature data from vehicle sensors, forming part of a larger system:
1. **Embedded Systems**: Sensors stream data to this backend.
2. **Backend**: Processes data and exposes it via an API.
3. **Mobile App**: Displays data to users.

## Features
- **`/record`**: Records engine temperature data from sensors.
- **`/collect`**: Retrieves the latest engine temperature and calculates an average temperature for the mobile app.

## Tech Stack
- **Flask**: API backend.
- **Redis**: In-memory datastore.
- **Docker & Docker Compose**: For containerized deployment.
