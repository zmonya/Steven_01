""" 
Authentication and Authorization in CodeIgniter
Selected Slides 
:
Slide 3:
Covers definitions of authentication and session management.

Authentication: Verifying user identity.
Session Management: Securely managing user sessions post-authentication.
Importance: Data security and controlled access to resources.
Slide 5:
Key Components of Authentication:

Methods: Password-based, Token-based (JWT), Multi-factor Authentication (MFA).
Techniques for session management: Cookies, Tokens.
Importance: Prevent unauthorized access and session hijacking.
Slide 7:
Password Authentication:

Explanation of hashing (e.g., SHA-256) and salting.
Combination of both methods to secure passwords.
Slide 8:
Detailed Salting Process:

How salting works to make hashes unique.
Protects against attacks like rainbow tables.
Slide 9:
Token-Based Authentication:

Emphasis on JSON Web Tokens (JWT) for stateless sessions.
MFA: Adding extra security layers (SMS, OTP).
Slide 12:
Implementing Authentication in CodeIgniter 4:

Using CodeIgniter libraries for setting up authentication.
Controllers and models for login, logout, and registration.
Database integration to store hashed passwords and user roles.
Slide 13:
Role-Based Access Control (RBAC):

User roles (Admin, Editor, User).
Restricting access to resources based on roles.
CodeIgniter filters/middleware for implementing RBAC.
Slide 16:
Session Security Considerations:

Preventing session hijacking: Secure cookies, HTTPS, HTTP-only flags.
Managing session expiry and logout functionality.
Slide 17:
Token Expiry and Renewal:

Setting token expiration to ensure security.
Automatic token renewal practices.
Slide 22:
Best Practices for Secure Authentication:

Use secure connections (HTTPS).
Hash passwords using bcrypt/Argon2.
Implement session timeouts, limit login attempts, and audit regularly.
Slide 24:
Key Takeaways:

Importance of secure authentication and session management.
RBAC to enforce permissions.
Following security best practices to safeguard applications.

Software Acquisition
Selected Slides 
:
Slide 2:
Definition:

Software acquisition involves obtaining software through various methods 
(purchase, download, or bundled with hardware).
Slide 3:
Types of Software:

Retail Software, OEM Software (bundled), Shareware (free trial), Freeware.
Slide 4:
Open Source Software:

Source code availability for customization.
Examples: Linux, Apache, OpenOffice.
Slide 5:
Public Domain Software:

Free software without copyrights or restrictions.
Differences from Freeware explained.
Slide 6:
Demo Software:

Restricted functionality to demonstrate capabilities.
Requires purchase for full access.
Slide 9:
Build vs Buy:

Key considerations: cost, expertise, and scope.
Buy for quicker deployment and better support.
Slide 10:
Technical Criteria:

Evaluating integration, design, security, and cost when buying software.
Slide 11:
Intuitive Design:

Importance of user-friendly software for higher adoption and satisfaction.
Slide 12:
Security:

Ensuring scalability and data protection with tools like CDN and WAF.
Slide 13:
Integration:

Two-way integration with enterprise systems (ERP, QMS).
Slide 14:
Data Lakes & Machine Learning:

Leveraging data lakes for quick queries and predictions through ML.
Slide 15:
Buy Decision Factors:

Scenarios favoring buying software over building it in-house.
Software Testing
Selected Slides 
:
Slide 3:
Importance of Software Testing:

Identifies errors early.
Ensures reliability, security, and customer satisfaction.
Slide 12:
Manual Testing:

Advantages: No coding knowledge required, suitable for unplanned changes.
Types: Black-box, White-box, Grey-box testing.
Techniques: Boundary Value Analysis, State Transition, Error Guessing.
 """