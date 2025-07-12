#  Project Overview

**ThreatSimLab** is a Python-based, terminal-driven cybersecurity learning tool built to help users grasp common cyber threats through interactive simulations and actionable defense techniques. It's tailored for students, educators, and cybersecurity enthusiasts seeking practical insight into how attackers operate—and how to counter them effectively.

This tool explores a wide array of core cybersecurity topics, such as phishing, malware and ransomware attacks, distributed denial of service (DDoS), social engineering tactics, and more advanced techniques like brute-force password cracking. Each module simulates a threat scenario while clearly presenting best-practice defensive strategies in blue for improved readability and understanding.

**ThreatSimLab** is compatible with Kali Linux and other Linux distributions, as well as Windows systems running Python 3.

---

## Key Features

- Interactive Learning Modules: Choose from five major cybersecurity topics to explore.
- Realistic Attack Simulations: Understand attacker methods through safe, educational simulations.
- Clear Defense Guides: Each topic includes highlighted mitigation strategies in blue for emphasis.
- User-Friendly CLI: Simple menu-driven interface for easy navigation.
- Cross-Platform Compatibility: Runs on Kali Linux, Ubuntu, Windows, macOS with Python 3.
- Lightweight & Extensible: Easily extend modules or add new attack simulations.

---

## Breakdown
- Phishing Attacks: Simulate a phishing email and learn to spot scams.
- Malware & Ransomware: Demonstrate ransomware encrypting files.
- Distributed Denial of Service (DDoS): Simulate server overload by too many requests.
- Social Engineering: Simulate a pretexting phone call attack.
- Advanced Cybersecurity Topics: Brute-force password cracking simulation.

---

## How to Use ThreatSimLab on Kali Linux

**1. Prepare Kali Linux:**

Kali Linux typically comes with Python 3 pre-installed. Confirm by running:
```bash
python3 --version
```

**If not installed, install Python 3:**

```bash
sudo apt update
sudo apt install python3
```
---

**2. Save the Script:**

- Open a terminal.
- Create a new file:

```bash
nano ThreatSimLab.py
```

- Paste the entire script above into the editor.
- Save and exit (Ctrl+O, Enter, Ctrl+X).

---

3. Make the Script Executable (Optional):
chmod +x ThreatSimLab.py

4. Run the Tool:
python3 ThreatSimLab.py

Or if made executable:
./ThreatSimLab.py

5. Navigate the Menu:
Enter the number corresponding to the topic you want to learn.

Read the explanations, and understand the mitigation strategies.

Repeat for other modules or exit when done.




