🔐 SQL Injection Detector with WAF Detection

A Python-based security testing tool designed to detect SQL Injection vulnerabilities and identify Web Application Firewall (WAF) behavior in web applications.
The tool supports both single URL and bulk URL scanning, providing clear, color-coded terminal output for easy analysis.

 Features
 SQL Injection Detection

Uses error-based, logical, and union-based SQL injection payloads

Identifies database error messages from:

MySQL

SQL Server

Oracle

PostgreSQL

// Web Application Firewall (WAF) Detection

Detects WAF behavior based on:

HTTP status codes (403, 406, 429)

Significant response length variations

Helps distinguish between true vulnerabilities and blocked payloads

// Flexible Scanning Modes

Single URL scan

Bulk URL scanning using a urls.txt file

// User-Friendly Output

Color-coded terminal output using Colorama

Clear vulnerability and WAF alerts

Scan summary for each target

// Tech Stack

Language: Python 3

Libraries:

requests

colorama

Platform: Cross-platform (Linux / Windows / macOS)

// Installation
// Clone the Repository
git clone https://github.com/your-username/sqli-detector.git
cd sqli-detector

// Install Required Libraries
pip install requests colorama

// Usage

Run the script:

python sqli_detector.py

Choose Scan Type

1 → Scan a single URL

2 → Scan multiple URLs from a file

// Input Format
// Single URL

Enter a URL with a parameter:

http://example.com/page.php?id=

// Bulk URLs

Create a urls.txt file:

http://example.com/page.php?id=
http://test.com/item.php?item_id=
http://vulnerable-site.com/index.php?product_id=

// Example Output
// Vulnerable Target
[*] Starting SQL Injection scan for: http://example.com/page.php?id=
[+] SQL Injection Found with payload: ' OR 1=1--
[!] WAF Detected → HTTP 403 (Payload: ')
[!] Scan complete.
[!!!] The target might be VULNERABLE to SQL Injection.

// Secure Target
[*] Starting SQL Injection scan for: http://secure-site.com/item.php?id=
[-] No vulnerability with payload: '
[!] Scan complete.
[+] The target is NOT vulnerable to SQL Injection.

💣 Payloads Used

The tool tests a wide range of SQL Injection payloads including:

'

''

' OR 1=1--

' OR '1'='1

' UNION SELECT NULL,NULL,NULL--

ORDER BY 1--

AND 1=1

AND 1=0

Payloads are designed to trigger:

SQL syntax errors

Logical condition bypass

Column enumeration

// How It Works

Fetches a baseline response

Appends SQL payloads to the target parameter

Analyzes:

HTTP status codes

Response length changes

Database error messages

Flags:

SQL Injection vulnerabilities

WAF interference
