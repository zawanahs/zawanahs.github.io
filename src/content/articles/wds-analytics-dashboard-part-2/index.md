---
title: "Analytics for a Growing Tech Community, Women Devs SG"
description: "Building a dashboard to help a technical community understand its members, improve its events, and plan more intentional outreach."
published: 2026-08-19
category: builds
series: dashboard
tags: [analytics, requirements, dashboard]
draft: True
---

### planning data pipeline. 
considerations: 
- data sources, g sheet. considered api for meetup for registrations and attendees data but decided on using what is available first, also need to consider the frequency of use ofthe dashboard eg. if we are only revisiting the dashabord for decisions every 6 months, we don't ahve to use an api that gets live registration or attendee data as soon as available. 
- tools; data studio, powerbi, tableau. since the data source is sporadic in google sheets. it's easier to have the dashboard on a tool with easy integration. based on research, looker studio, so decided to go with this. 



### Streamlining the data across all event folders in WDS google folder. 
- apps script; some kinks eg. feedback form with just the g sheet and not the google forms. 

Minimise changing existing processes too much, so decided to use a script that extracts all the g forms data across all events and consolidate it into a master file. 

Considering PII, have to place the sanitised data in a separate google sheet, that looker studio takes from. 

### Building the dashboard 

back and forth with looker studio. 
pros: very easy to source directly from google sheets
cons: data calc limitations

found myself spending more time configuring the dashboard to calculate the field that i want and configuring the dashboard visuals to how i wanted it. 

waste of my time, and my brain is dying at each administrative workarounds i did. 

so i fabled it. 

in half a day i got the dashboard up.