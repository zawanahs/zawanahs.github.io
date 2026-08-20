---
title: "Analytics for a Growing Tech Community, Women Devs SG (Part 2)"
description: "Building a dashboard to help a technical community understand its members, improve its events, and plan more intentional outreach."
published: 2026-08-19
category: builds
series: dashboard
tags: [analytics, requirements, dashboard]
draft: True
---

This is a continuation of [Part 1](https://zawanah.com/articles/wds-analytics-dashboard-part-1/) where I share the process of building an analytics dashboard for Women Devs SG. 

For this part of the series, I will share about building the data pipelines that will feed this dashboard. This means planning the data architecture for the dashboard. 

## Data Pipeline

There are 2 key considerations when I was planning for this:

**1. Data sources** - Where does the data live now? Is there a need for data migration to a central place that feeds into the dashboard? Will there be data cleansing or transformation needed and where is best to perform these? 

The data lives in Google Drive, and each event has its own folder that contains the registrations, attendance and feedback responses in Google Sheets or Google Form responses. 

Since most of the data live in Google Sheets, I decided to create a Master Google Sheet containing all the data that I need, which will then be sanitised (to exclude personally identifiable information), before being fed into the dashboarding tool. 

I had thought of a more future proof solution by having all future events have the registrations and attendance data in one sheet, but this would require a significant change in the existing processes and I prefer to minimise significant changes to existing processes until the dashboard has earned a more permanent place here. 

To create the Master sheet, I worked with Claude and Codex to generate the codes in JavaScript to first identify all event folders, and subsequently scrape all feedback data into google sheets.

![apps-script](image.png "Figure 1: Apps script Feedback Collector")

**2. Which dashboarding tool** - PowerBI? Tableau? Data Studio?

I am familiar with Power BI and Tableau, but since this dashboard is meant to be accessible to leads of WDS, they need to be able to access it easily and if I built the dashboard with my account, it would be stuck with me. Not to mention you need a PowerBI and Tableau licence to view it. 

Based on my research, the supposed next best option was Data Studio (formerly known as Looker Studio). Since it is a Google product, it would be seamless to feed data from the Master Google Sheet to Data Studio. 

## Challenges and Limitations

Any seasoned data or business analyst would know that there is no perfect data in this world. We simply extract as much useful insights as we can with what we have. 



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