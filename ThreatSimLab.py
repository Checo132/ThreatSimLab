import hashlib
import itertools
import string
import time

def print_blue_welcome():
    BLUE = "\033[94m"
    RESET = "\033[0m"
    print(f"{BLUE}Welcome to ThreatSimLab: An Interactive Cybersecurity Learning Platform{RESET}\n")

def print_colored(text, color_code):
    RESET = "\033[0m"
    print(f"{color_code}{text}{RESET}")

def phishing_simulation():
    BLUE = "\033[94m"
    RED = "\033[91m"
    RESET = "\033[0m"
    print(f"\n{BLUE}--- Phishing Attack Simulation ---{RESET}\n")

    print("Emulating a phishing email attempt...")
    fake_email = {
        "from": "support@yourbank.com",
        "subject": "URGENT: Account Verification Required",
        "body": "Dear user,\n\nWe detected unusual activity on your account. Please verify your credentials at http://fakebank-login.com to avoid suspension.\n\nBest,\nYourBank Security Team"
    }
    print("\n--- Email Content ---")
    for k, v in fake_email.items():
        print(f"{k.title()}: {v}\n")
    print("Take note of the suspicious link and urgent tone—classic phishing strategies.")
    print(f"{BLUE}Defense Tip: Avoid clicking on unfamiliar links or sharing credentials via email. Always verify the sender and enable MFA wherever possible.{RESET}\n")

    print("\nQuestions & Answers:\n")
    print("1. What is the main goal of a phishing attack?\n")
    print("A) Steal confidential information")
    print("B) Speed up your computer")
    print("C) Install legitimate software")
    print("D) Improve security\n")
    answer1 = input("Your answer: ").strip().lower()
    if answer1 == 'a':
        print_colored("Correct!", BLUE)
    else:
        print_colored("Incorrect. The correct answer is A.", RED)

    print("\n2. Which of the following is a sign of a phishing email?\n")
    print("A) Unexpected sense of urgency")
    print("B) Strange sender address")
    print("C) Suspicious links")
    print("D) All of the above\n")
    answer2 = input("Your answer: ").strip().lower()
    if answer2 == 'd':
        print_colored("Correct!", BLUE)
    else:
        print_colored("Incorrect. The correct answer is D.", RED)
    print()

def malware_simulation():
    BLUE = "\033[94m"
    RED = "\033[91m"
    RESET = "\033[0m"
    print(f"\n{BLUE}--- Malware (Ransomware) Simulation ---{RESET}\n")

    print("Demonstrating how ransomware encrypts user files...")
    files = ["report.docx", "photo.jpg", "presentation.pptx"]
    print("Files before infection:", files)
    encrypted_files = [f + ".encrypted" for f in files]
    time.sleep(1)
    print("Files after ransomware activity:", encrypted_files)
    print("These files are now locked until a decryption key is provided (if ever).")
    print(f"{BLUE}Defense Tip: Regularly back up data, avoid suspicious downloads, and keep security software updated.{RESET}\n")

    print("\nQuestions & Answers:\n")
    print("1. What type of malware encrypts your data for ransom?\n")
    print("A) Worm")
    print("B) Trojan")
    print("C) Ransomware")
    print("D) Rootkit\n")
    answer1 = input("Your answer: ").strip().lower()
    if answer1 == 'c':
        print_colored("Correct!", BLUE)
    else:
        print_colored("Incorrect. The correct answer is C.", RED)

    print("\n2. What is a key defense against ransomware?\n")
    print("A) Frequent backups")
    print("B) Using public Wi-Fi")
    print("C) Disabling antivirus")
    print("D) Ignoring updates\n")
    answer2 = input("Your answer: ").strip().lower()
    if answer2 == 'a':
        print_colored("Correct!", BLUE)
    else:
        print_colored("Incorrect. The correct answer is A.", RED)
    print()

def ddos_simulation():
    BLUE = "\033[94m"
    RED = "\033[91m"
    RESET = "\033[0m"
    print(f"\n{BLUE}--- DDoS Attack Simulation ---{RESET}\n")

    print("Simulating a flood of requests overloading a web server...")
    server_capacity = 5
    requests = 0
    print("Server capacity: 5 concurrent requests.")
    for i in range(10):
        requests += 1
        if requests > server_capacity:
            print(f"Request {i+1}: Server OVERLOADED! (DDoS impact)")
        else:
            print(f"Request {i+1}: Server OK")
        time.sleep(0.2)
    print(f"\n{BLUE}Defense Tip: Use rate limiting, firewalls, CDNs, and traffic monitoring to mitigate DDoS risks.{RESET}\n")

    print("\nQuestions & Answers:\n")
    print("1. What does DDoS stand for?\n")
    print("A) Distributed Denial of Service")
    print("B) Direct Data on Server")
    print("C) Data Delivery over SSL")
    print("D) Digital Denial of Security\n")
    answer1 = input("Your answer: ").strip().lower()
    if answer1 == 'a':
        print_colored("Correct!", BLUE)
    else:
        print_colored("Incorrect. The correct answer is A.", RED)

    print("\n2. What is a common defense against DDoS attacks?\n")
    print("A) Rate limiting")
    print("B) Ignoring traffic")
    print("C) Using weak passwords")
    print("D) Disabling firewalls\n")
    answer2 = input("Your answer: ").strip().lower()
    if answer2 == 'a':
        print_colored("Correct!", BLUE)
    else:
        print_colored("Incorrect. The correct answer is A.", RED)
    print()

def social_engineering_simulation():
    BLUE = "\033[94m"
    RED = "\033[91m"
    RESET = "\033[0m"
    print(f"\n{BLUE}--- Social Engineering Simulation ---{RESET}\n")

    print("Simulating a fake tech support call asking for credentials...")
    print("""
    [Phone rings]
    "Hello, this is IT support. We detected a virus on your computer.
    Can you please provide your login password so we can fix the issue?"
    """)
    print("This demonstrates a classic pretexting attack.")
    print(f"{BLUE}Defense Tip: Never share login details over the phone. Always verify identities and report suspicious behavior to your security team.{RESET}\n")

    print("\nQuestions & Answers:\n")
    print("1. What is social engineering in cybersecurity?\n")
    print("A) Manipulating people to give up confidential info")
    print("B) Engineering social networks")
    print("C) Building secure systems")
    print("D) Encrypting data\n")
    answer1 = input("Your answer: ").strip().lower()
    if answer1 == 'a':
        print_colored("Correct!", BLUE)
    else:
        print_colored("Incorrect. The correct answer is A.", RED)

    print("\n2. What should you do if someone calls asking for your password?\n")
    print("A) Tell them your password")
    print("B) Refuse and report the request")
    print("C) Ignore and hang up")
    print("D) Change your password\n")
    answer2 = input("Your answer: ").strip().lower()
    if answer2 == 'b':
        print_colored("Correct!", BLUE)
    else:
        print_colored("Incorrect. The correct answer is B.", RED)
    print()

def advanced_simulation():
    BLUE = "\033[94m"
    RED = "\033[91m"
    RESET = "\033[0m"
    print(f"\n{BLUE}--- Advanced Attack Simulation: Brute-Force Password Attack ---{RESET}\n")

    print("Simulating a brute-force password guessing attempt...")
    password = "ab1"
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    found = False
    for length in range(1, 4):
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess_pw = ''.join(guess)
            if guess_pw == password:
                print(f"Password '{password}' cracked after {attempts} guesses.")
                found = True
                break
        if found:
            break
    print(f"{BLUE}Defense Tip: Use complex passwords, enable lockout policies, and activate multi-factor authentication.{RESET}\n")

    print("\nQuestions & Answers:\n")
    print("1. What is a brute-force attack?\n")
    print("A) Guessing passwords by trying all combinations")
    print("B) Sending phishing emails")
    print("C) Encrypting files")
    print("D) Using social media\n")
    answer1 = input("Your answer: ").strip().lower()
    if answer1 == 'a':
        print_colored("Correct!", BLUE)
    else:
        print_colored("Incorrect. The correct answer is A.", RED)

    print("\n2. What is an effective defense against brute-force attacks?\n")
    print("A) Account lockout policies")
    print("B) Using your name as password")
    print("C) Disabling antivirus")
    print("D) Ignoring security updates\n")
    answer2 = input("Your answer: ").strip().lower()
    if answer2 == 'a':
        print_colored("Correct!", BLUE)
    else:
        print_colored("Incorrect. The correct answer is A.", RED)
    print()

def main():
    print_blue_welcome()
    while True:
        print("\nChoose a cybersecurity topic to explore:\n")
        print("1. Phishing Attacks")
        print("2. Malware & Ransomware")
        print("3. Distributed Denial of Service (DDoS)")
        print("4. Social Engineering")
        print("5. Advanced Cybersecurity Topics")
        print("6. Exit\n")
        choice = input("Enter your choice (1-6): ").strip()
        if choice == '1':
            phishing_simulation()
        elif choice == '2':
            malware_simulation()
        elif choice == '3':
            ddos_simulation()
        elif choice == '4':
            social_engineering_simulation()
        elif choice == '5':
            advanced_simulation()
        elif choice == '6':
            print("Thank you for using ThreatSimLab. Stay vigilant!")
            break
        else:
            print("Invalid selection. Please choose a number from 1 to 6.\n")

if __name__ == "__main__":
    main()
