from certifications import get_certifications

career = "ML Engineer"

certs = get_certifications(career)

print("=" * 40)
print("Recommended Certifications")
print("=" * 40)

for cert in certs:
    print("•", cert)