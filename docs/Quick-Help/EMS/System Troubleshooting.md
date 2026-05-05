# EMS System SiteCheck

## Overview
The EMS System SiteCheck is a diagnostic checklist designed to help users identify and resolve issues within the Nube iO EMS system. It provides a comprehensive check of various components and configurations to ensure that the system is functioning correctly.

## Overview
Use this guide for quick on-site checks to identify power, network, sensor, and hardware issues before escalation. Checks are separated by role so the right person performs the right action safely.

Power supply unit (PSU) in this guide means the device providing low-voltage power to the gateway (typically a 24V power supply).

## Safety and Role Boundary
- Facilities Manager: visual inspection, status checks, simple resets, cable reseat, battery replacement, and evidence collection.
- Licensed Tradesperson (Electrician/Plumber): live electrical testing, rewiring, supply rectification, terminations, and meter/sensor plumbing-electrical rectification.
- If there is water ingress to the gateway, burn marks, or exposed conductors, isolate equipment and escalate immediately.

## SiteCheck Quick Triage

| Check | Symtom | Likely Cause | Action |
| --- | --- | --- | --- |
| Power Availability Check | Gateway LEDs OFF or router has no power | 24V power supply off/failed, disconnected power lead, or breaker off | Check breaker label/status, confirm 24V power supply is ON, reseat connectors, escalate to licensed electrician if unresolved |
| Battery Health Check | Micro-Edge not reporting or low battery alarm | Battery depleted or poor battery contact | Replace battery and recheck reporting |
| Network Link Check | No data even when gateway LEDs are ON | Ethernet/WAN issue, router offline, or no link | Check Ethernet cable and link lights, verify router/WAN status, reboot router |
| Hardware Condition Check | Visible water ingress, burn marks, or loose wiring | Physical damage or installation fault | Isolate equipment and escalate to licensed tradesperson |

## Facilities Manager Checks (Non-Invasive)

### Gateway (Rubix Compute)
| Check | Symtom | Likely Cause | Action |
| --- | --- | --- | --- |
| Gateway LED Check | No LEDs | Power not present | Check local breaker label/status, confirm 24V power supply is ON, confirm connectors are seated |
| Gateway Data Status Check | LEDs ON, no data | Network/router issue | Confirm Ethernet link lights, reboot router, verify WAN service status |
| Gateway Physical Condition Check | Physical damage | Port or enclosure fault | Photograph damage, isolate if unsafe, escalate |

### Router
| Check | Symtom | Likely Cause | Action |
| --- | --- | --- | --- |
| Router Power Check | No power | Adapter unplugged/failed | Check adapter is plugged in, verify outlet is active, swap with known-good adapter if available |
| Router WAN/Internet Check | No internet | WAN/ISP issue | Reboot router once, confirm WAN indicator, check known ISP outage |
| Router Ventilation Check | Overheating | Ventilation issue | Improve airflow, remove obstruction, monitor stability |

### Micro-Edge (LoRa Sensor)
| Check | Symtom | Likely Cause | Action |
| --- | --- | --- | --- |
| Micro-Edge Reporting Check | No data | Battery depleted or LoRa path issue | Replace battery, verify gateway is online, check for new obstructions |
| LoRa Signal/Antenna Check | Intermittent data | Weak signal | Reposition sensor/antenna within approved location |
| Data Accuracy Check | Incorrect data | Mapping or setup issue | Validate point mapping and configuration against commissioning notes |

## Licensed Tradesperson Checks (Electrician / Plumber)

### Electrical (Licensed Electrician)
| Check | Symtom | Likely Cause | Action |
| --- | --- | --- | --- |
| 24V Supply Voltage Check | Gateway/router still no power after basic checks | Failed 24V power supply (PSU), missing 24V feed, or wiring fault | Test supply voltage, polarity, and continuity; rectify feed/termination; replace failed 24V power supply |
| Electrical Damage Check | Burn marks or heat damage | Electrical fault/current event | Isolate circuit, replace damaged components, verify protective device coordination |
| Termination Integrity Check | Loose or failed terminations | Installation fault | Re-terminate wiring to standard, torque-check terminals, verify enclosure integrity |

### Meter/Sensor Plumbing-Electrical (Licensed Plumber or Electrician as required)
| Check | Symtom | Likely Cause | Action |
| --- | --- | --- | --- |
| Meter Orientation/Install Check | Incorrect water/flow readings | Sensor install/config issue | Verify meter orientation, installation condition, wiring pulse/config, then recommission |
| Ingress Protection Check | Water ingress at enclosure/device | Seal or gland failure | Replace compromised parts, reseal glands/enclosure, verify ingress protection |
| Field Device Wiring Check | Persistent no data from field device | Field wiring/device failure | Test loop/pulse/wiring path, rectify fault, replace failed field device |

## Visual Fault Identification

| Check | Symtom | Likely Cause | Action |
| --- | --- | --- | --- |
| Gateway LED Check | No LEDs (Gateway) | Power issue | Complete basic power checks, then escalate to licensed electrician if unresolved |
| Gateway Data Link Check | LEDs ON, no data | Network issue | Check Ethernet/router and reboot |
| Ethernet Link-Light Check | Ethernet light OFF | No network link | Reconnect or replace Ethernet patch cable |
| Router Internet Check | Router no internet | ISP/router issue | Reboot router and verify WAN/ISP |
| Micro-Edge Reporting Check | Micro-Edge no data | Battery / LoRa issue | Replace battery or reposition device |
| LoRa Signal Stability Check | Intermittent data | Signal issue | Improve LoRa path/relocate device |
| Reading Accuracy Check | Incorrect readings | Wiring/config/install issue | Verify wiring/install and recommission |
| Wiring Integrity Check | Loose wiring | Installation issue | Re-terminate and secure wiring |
| Water Ingress Check | Water damage | Ingress | Replace damaged device and reseal enclosure |
| Electrical Burn Mark Check | Burn marks | Electrical fault | Isolate immediately and replace damaged hardware |

## Escalate to Nube iO When
- Facilities Manager checks are complete and issue persists.
- Licensed tradesperson rectification is complete but telemetry is still missing/incorrect.
- Gateway and network are healthy but field devices still do not report.
- Repeated faults occur after rectification.

## Field Notes Template
Use this section when escalating:

- Site name:
- Date/time:
- Contact person:
- Gateway serial:
- Router model:
- Affected device(s):
- Symptoms observed:
- Facilities Manager checks completed:
- Licensed trade checks completed:
- Actions taken:
- Photos attached: