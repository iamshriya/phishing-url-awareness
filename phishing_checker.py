import re
from urllib.parse import urlparse

REASONS = {
    "@": "The browser may treat text before @ as user information, hiding the actual hostname.",
    "HTTP": "HTTP does not encrypt the connection like HTTPS normally does.",
    "IP": "An IP address instead of a familiar domain can be harder to recognise.",
    "LONG": "An unusually long URL can hide confusing or misleading details.",
    "SUBDOMAINS": "Many hostname segments can make the actual domain harder to spot.",
    "PUNYCODE": "Punycode can represent domain names using characters that may look confusing."
}
def inspect_url(raw_url):
    """Check visible URL text for selected warning signs."""
    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url
    try:
        parsed = urlparse(candidate)
    except ValueError:
        return ["This text is not a valid URL format."]
    host = (parsed.hostname or "").lower()

    if not host:
        return ["Could not identify a hostname."]

    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")

    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")

    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")

    if not findings:
        findings.append(
            "No listed warning signs found. This does NOT prove safety."
        )

    return findings

INFO_MESSAGES = ("No URL entered", "Could not identify", "No listed warning")

def has_warnings(findings):
    return not findings[0].startswith(INFO_MESSAGES)

def main():
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")

    while True:
        raw_url = input("\nEnter a sample URL (or type q to quit): ")

        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break

        print("\nResult:")
        findings = inspect_url(raw_url)  
        for item in findings:
            print("- " + item)

            if "@" in item:
                print("  Why it matters: " + REASONS["@"])
            elif "HTTP" in item:
                print("  Why it matters: " + REASONS["HTTP"])
            elif "IP address" in item:
                print("  Why it matters: " + REASONS["IP"])
            elif "long" in item.lower():
                print("  Why it matters: " + REASONS["LONG"])
            elif "hostname segments" in item:
                print("  Why it matters: " + REASONS["SUBDOMAINS"])
            elif "punycode" in item.lower():
                print("  Why it matters: " + REASONS["PUNYCODE"])

            if has_warnings(findings):
                print("\nREVIEW CAREFULLY: " + str(len(findings)) + " warning sign(s) found.")


print("Never enter passwords from unexpected links.")


if __name__ == "__main__":
    main()