EWB Phishing URL Awareness Checker

Overview

Phishing is an online scam in which attackers use deceptive links or messages to trick people into sharing sensitive information. This Python tool checks URL text for visible warning signs and helps users recognise potentially suspicious links.

Features

- Detects an @ symbol in the URL
- Flags unusually long URLs (over 100 characters)
- Flags IP-address hostnames
- Flags many hostname segments (5 or more)
- Flags punycode-style hostnames (xn--)
- Flags the HTTP scheme
- Checks multiple URLs without restarting, with a quit command
- Adds a Review Carefully summary when warnings are found
- Handles malformed input without crashing
- Explains each warning in simple words

Requirements

Python 3.10 or later. No extra packages.

How to Run

Windows: "python phishing_checker.py"

Mac/Linux: "python3 phishing_checker.py"

Example Output

Result:
- Uses an IP address instead of a familiar domain.
- Uses HTTP. HTTPS alone does not prove trust.
- Why it matters: An IP address instead of a familiar domain can be harder to recognise.
- Why it matters: HTTP does not encrypt the connection like HTTPS normally does.

REVIEW CAREFULLY: 2 warning sign(s) found.

Testing

#| Input| Expected| Actual| Result
1| https://www.example.com/login| No warning signs| No listed warning signs found| PASS
2| http://192.0.2.10/account| IP address + HTTP| Both warnings and explanations appeared| PASS
3| http://example.com@sample.invalid/login| @ symbol + HTTP| Both warnings and explanations appeared| PASS
4| https://a.b.c.d.e.example.invalid/path| Many hostname segments| Warning and explanation appeared| PASS
5| https://xn--example.invalid/| Punycode-style hostname| Warning and explanation appeared| PASS

Full test details are in "tests/test_samples.md".

Screenshots

"Sample run" (screenshots/sample_run.png)

"Test results" (screenshots/test_results.png)

Improvements

1. Continuous URL checking - Added a loop and quit command to check multiple URLs without restarting; tested with multiple URLs and the quit command.
2. Review Carefully summary - Added a count of warning signs; tested with an IP-address URL using HTTP.
3. Malformed input handling - Added try/except handling to return a clear message instead of crashing; tested with "http://[bad".
4. Warning explanations - Added a dictionary of simple explanations under warnings; tested with sample URLs that trigger different warnings.

Limitations

This is an educational tool. It only reads URL text. It does not visit URLs, scan for malware or prove that a URL is safe. No warning signs found does NOT mean a URL is safe.

Ethical Use

Use sample strings only. Do not collect credentials. Do not use this project to deceive anyone or to test websites without permission.

Author

[Shriti Shriya],[AI-POWERED CYBERSECURITY INTERNSHIP],EWD Courses