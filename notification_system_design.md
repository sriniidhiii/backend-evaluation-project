# Notification System Design

## Overview
This project implements a backend system with logging middleware that captures application events and sends them to an external logging API.

## Architecture
- Backend: Node.js with Express
- Logging Middleware: Custom reusable function
- External API: Evaluation logging service

## Flow
1. User registers and gets clientID and clientSecret
2. User authenticates and receives access_token
3. Backend uses access_token to send logs to API

## Logging Middleware
A reusable function:
Log(stack, level, package, message)

It sends logs using HTTP POST request with:
- stack (backend/frontend)
- level (info, error, etc.)
- package (route, handler, etc.)
- message (log message)

## API Integration
- Register API
- Auth API
- Log API

## Technologies Used
- Node.js
- Express.js
- Axios

## Conclusion
The system ensures proper logging and monitoring of backend events using a structured logging mechanism.
