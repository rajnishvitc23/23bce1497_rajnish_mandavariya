# Agile Project Documentation  
## Real-Time Bus Tracking System

---

# 1. Vision & Purpose

This document provides lightweight and evolving Agile documentation for the **Real-Time Bus Tracking System**, following Agile principles of clarity, collaboration, and continuous improvement.

The goal of the system is to provide **real-time tracking of buses on a map**, allowing passengers and administrators to monitor bus locations, routes, and estimated arrival times through a web interface.

---

# 2. Project Scope

The Real-Time Bus Tracking System enables users to monitor public transport buses in real time using GPS-based location updates.

The system consists of a **frontend web interface displaying buses on an interactive map**, a **backend API for processing location data**, and a **database to store bus routes and coordinates**. GPS devices or simulators send periodic location updates to the backend, which are processed and displayed on the map.

---

# 3. User Personas

Primary users of the system include:

- **Passengers** – view live bus locations and routes.
- **Transport Operators** – monitor buses and route activity.
- **System Administrators** – manage system configuration and data.

---

# 4. Core User Stories

Key functionality is defined using user stories and acceptance criteria in the table below.

| Story ID | User Story | Priority | Acceptance Criteria |
|--------|------------|----------|--------------------|
| US-1 | User opens map to view buses | High | Map loads successfully |
| US-2 | System receives GPS coordinates | High | Location data stored correctly |
| US-3 | Bus location displayed on map | High | Marker updates in real time |
| US-4 | Admin manages bus routes | Medium | Routes added/updated successfully |
| US-5 | System logs bus movement data | Low | Logs stored and accessible |

---

# 5. Product Backlog

| Story ID | Feature | Priority | Description |
|--------|---------|----------|-------------|
| PB-1 | User Map Interface | High | Interactive map showing bus positions |
| PB-2 | Backend API | High | REST API to handle bus location updates |
| PB-3 | GPS Data Integration | High | Receive location updates from devices |
| PB-4 | Database Management | Medium | Store routes, buses, and coordinates |
| PB-5 | Admin Dashboard | Low | Monitor buses and manage routes |

---

# 6. Sprint Plan

| Sprint | Focus | Deliverables |
|------|------|-------------|
| Sprint 1 | Backend Setup | Node.js server, database connection |
| Sprint 2 | API Development | Bus location update endpoints |
| Sprint 3 | Frontend Map UI | Interactive map with bus markers |
| Sprint 4 | Real-Time Updates | Location update handling and testing |

---

# 7. Milestones

| Checkpoint | Date | Deliverables |
|------------|------|-------------|
| Checkpoint 1 | February 20, 2026 | Backend API with database |
| Checkpoint 2 | March 5, 2026 | Map interface with bus tracking |
| Checkpoint 3 | March 20, 2026 | Fully functional real-time tracking system |

---

# 8. Definition of Done

| Criteria | Description |
|---------|-------------|
| Code | Implemented and reviewed |
| Testing | All system functions tested |
| Demo | Working bus tracking demonstration |
| Documentation | Updated project documentation |

---

# 9. Risks & Mitigation

| Risk | Impact | Mitigation |
|-----|-------|-----------|
| GPS data inaccuracies | High | Use validation and smoothing |
| Real-time update delays | Medium | Optimize backend processing |
| Map rendering performance | Medium | Efficient frontend rendering |
| Server downtime | Low | Error handling and monitoring |

---

# 10. Summary

The Agile framework allows the Real-Time Bus Tracking System to evolve through iterative development. Features are delivered incrementally, ensuring continuous testing, feedback, and improvement throughout the development process.