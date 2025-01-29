# LearnDevops2025
This repository is to do practice on my devops learnings

Week 1:

The OSI (Open Systems Interconnection) model is a conceptual framework that describes how different network components communicate with each other. It has 7 layers, each responsible for a specific function in data transmission.

To simplify it, imagine sending a letter via postal service. Each OSI layer represents a step in the process of preparing, sending, delivering, and receiving the letter.

OSI Model Explained with a Real-Life Example (Postal System)
OSI Layer	Real-Life Example (Sending a Letter)	Technical Role
1. Physical	The postman physically delivers the letter.	Cables, Wi-Fi, or hardware transmitting bits.
2. Data Link	The envelope ensures correct delivery to the right mailbox.	MAC addresses, Ethernet, and switches ensure correct direct connections.
3. Network	The post office determines the best route for delivery.	IP addresses and routers find the best path for data.
4. Transport	The letter is sent with a tracking system ensuring delivery.	TCP/UDP ensures reliable or fast delivery of data packets.
5. Session	The sender and receiver maintain correspondence.	Manages sessions between devices (e.g., keeping a web login active).
6. Presentation	The recipient understands the language of the letter.	Encryption, compression, and data formatting (e.g., JPEG, ASCII).
7. Application	The recipient reads and understands the letter.	Web browsers, emails, and applications interact with users.
Breakdown of Each Layer with Simple Terms:
Physical Layer (Hardware & Transmission)

Transfers raw data (bits) through cables, Wi-Fi, or fiber optics.
Example: Your Wi-Fi router or LAN cable transmitting data.
Data Link Layer (Ensuring Direct Communication)

Ensures direct communication between two connected devices (like neighbors).
Uses MAC addresses to identify devices within the same network.
Example: A switch directing data to the correct device in your home network.
Network Layer (Routing & Addressing)

Finds the best route for data between networks using IP addresses.
Example: A router determining the best path to send data from your home to Google’s servers.
Transport Layer (Reliable Delivery)

Ensures complete and error-free transmission of data.
Uses TCP (reliable, ordered delivery) or UDP (fast, no order guarantee).
Example: TCP ensures all parts of an email arrive correctly; UDP helps stream a YouTube video without delay.
Session Layer (Managing Conversations)

Keeps track of communication between devices.
Example: Logging into a website and maintaining your session while browsing.
Presentation Layer (Data Formatting & Encryption)

Converts data into a readable format for the application.
Handles encryption, compression, and translation of data.
Example: SSL encrypting your banking details on a website.
Application Layer (User Interaction)

The interface that users interact with, like browsers and apps.
Example: Chrome, Gmail, Skype, and WhatsApp all function at this layer.
Summary in Simple Terms:
Think of sending a letter:

Physical: The postman moves the letter.
Data Link: The envelope protects the letter.
Network: The post office decides the best route.
Transport: The tracking system ensures safe delivery.
Session: The sender and receiver keep communicating.
Presentation: The letter is in the right language.
Application: The recipient reads and understands the letter.
