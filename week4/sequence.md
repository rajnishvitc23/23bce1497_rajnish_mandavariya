# Sequence Diagram  
## Real-Time Bus Tracking System

### Overview
This sequence diagram shows how different components of the system interact to retrieve and display real-time bus location data.

### Participants
- User  
- Web App (Frontend)  
- Backend API  
- Location Service  
- MongoDB Database  
- Map UI  

### Sequence Flow
1. User opens the bus tracking application.
2. Web App sends a request to the Backend API for bus location data.
3. Backend API forwards the request to the Location Service.
4. Location Service queries MongoDB for bus coordinates.
5. MongoDB returns the location data.
6. Backend API sends processed data back to the Web App.
7. Web App updates the Map UI with bus markers.
8. User views real-time bus locations on the map.

### Summary
The sequence ensures that bus location data flows from the database through backend services to the frontend map interface, allowing users to track buses in real time.