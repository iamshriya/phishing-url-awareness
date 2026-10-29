Test Results

Python version used: Python 3.15.2
Operating system: Windows 11
Date: 2026-10-29

#| Input| Expected result| Actual result| Pass/Fail
1| "https://www.example.com/login"| No listed warning signs| No listed warning signs found. This does NOT prove safety.| PASS
2| "http://192.0.2.10/account"| IP address + HTTP| Uses an IP address instead of a familiar domain. Uses HTTP. HTTPS alone does not prove trust.| PASS
3| "http://example.com@sample.invalid/login"| @ symbol + HTTP| Contains an @ symbol; inspect carefully. Uses HTTP. HTTPS alone does not prove trust.| PASS
4| "https://a.b.c.d.e.example.invalid/path"| Many hostname segments| Contains many hostname segments/subdomains.| PASS
5| "https://xn--example.invalid/"| Punycode-style hostname| Contains a punycode-style hostname.| PASS

Notes

- I learned that a URL can contain several warning signs, such as an IP address, an @ symbol, or HTTP.
- I was surprised that a URL with no listed warning signs is not necessarily safe.
- The checker only examines visible URL text; it does not open the URL or prove whether a website is trustworthy.