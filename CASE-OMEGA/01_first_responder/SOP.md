# First Responder SOP — Case Omega

**Purpose:** Preserve safety, service continuity, and potential digital evidence during a suspected ransomware event.

## 1. Authority and safety
1. Confirm that the response is authorized by the hospital incident commander.
2. Prioritize patient safety and continuity of clinical care; coordinate with clinical leadership.
3. Do not independently power off, reboot, log out, or disconnect equipment unless an approved containment decision requires it.
4. Record who gave each instruction, the time, and the operational reason.

## 2. Initial actions
1. Record date/time, location, reporter, symptoms, affected departments, and visible ransom message.
2. Photograph screens and equipment in context before interacting with them, where safe and permitted.
3. Note whether devices are powered on, network-connected, logged in, or displaying alerts.
4. Isolate affected systems from the network only under the incident commander's direction. Prefer controlled network isolation over powering down.
5. Preserve volatile evidence where trained personnel and approved procedures are available.

## 3. Scene documentation
1. Assign a unique evidence ID to every item.
2. Photograph overview, mid-range, and close-up views; include a scale where useful.
3. Create a sketch showing room layout, devices, ports, cables, network equipment, and evidence IDs.
4. Record make/model, serial number, hostname, asset tag, location, state, and connections.
5. Maintain an activity log with exact time, person, action, and reason.

## 4. Evidence identification
Potential evidence includes workstations, servers, storage media, USB devices, firewall/VPN/DNS/DHCP logs, endpoint alerts, email gateway records, cloud identity audit logs, backups, and relevant network captures.

## 5. Collection and preservation
1. Obtain written authorization and define scope.
2. Use trained personnel and validated write-blocking/acquisition procedures where applicable.
3. Record tool name, version, settings, operator, start/end times, errors, and destination media.
4. Calculate SHA-256 hashes and independently verify them.
5. Seal evidence in tamper-evident packaging; restrict access and store securely.

## 6. Communications and handover
1. Maintain a contemporaneous incident and evidence log.
2. Transfer evidence only to an identified recipient after checking identity and authority.
3. Both parties sign the chain-of-custody entry.
4. Escalate suspected data exfiltration, patient-safety impact, or legal notification obligations to authorized leadership and counsel.

## 7. Prohibited actions
- Do not pay ransom or communicate with threat actors without authorized leadership and legal advice.
- Do not run unknown samples on production systems.
- Do not browse, alter, or disclose patient data beyond the authorized scope.
- Do not fabricate timestamps, hashes, screenshots, or collection claims.

**Training limitation:** This SOP is an academic template. Actual incident response must follow organizational policy, applicable law, and qualified expert direction.
