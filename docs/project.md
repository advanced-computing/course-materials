# Project

## Goals

As stated in the [course description](../README.md#course-description):

> Over the semester, students will build a complex end-to-end data system.

You'll be building a live dashboard, with all the infrastructure behind it:

- Automated data ingestion
- A database
- Web-based interactive data visualization

All of this will be in [the cloud](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/).

## Inspiration

- [Center for Disease Control (CDC) dashboards](https://www.cdc.gov/nssp/php/data-research/dashboards/index.html)
- [Chicago Region Transit Dashboard](https://experience.arcgis.com/experience/2aa35be601ed4e1aa1b1fcf2bf56cb2f/page/Home/)
- [Chicago Transit Authority Historical Bus Crowding](https://capacitydb.ctadataportal.com/)
- [Colorado Behavioral Health Administration (BHA) Performance Hub](https://bha.colorado.gov/data-and-reports/performance-hub)
- [Congestion Pricing Tracker](https://www.congestion-pricing-tracker.com/)
- [Johns Hopkins COVID map](https://coronavirus.jhu.edu/map.html)
- [New York Flu Tracker](https://nyshc.health.ny.gov/web/nyapd/new-york-state-flu-tracker)
- [New York Traffic Data Viewer (TDV)](https://www.dot.ny.gov/tdv)
- [NYPD TrafficStat](https://trafficsafetyforum.nypdonline.org/)
- [TransitMatters](https://dashboard.transitmatters.org/)
- [United States of Health](https://www.mckinsey.com/industries/public-sector/our-insights/us-public-health-dashboard)

## Expectations

### At all times

- All code is peer-reviewed, through [pair programming](pairing.md) and/or pull requests.
- All team members are contributing equal amounts.
- The Project leverages at least one [dataset that's regularly updated](data.md#datasets-that-are-regularly-updated).
- The code, documentation, and repository are clean, following good coding style and [other best practices](https://python-public-policy.afeld.me/en/columbia/assignments.html#coding-in-general).

### By the end

- The site doesn't need to [read like a blog post](https://computing-in-context.afeld.me/projects.html#requirements) necessarily, but it should explain what's going on.
- The site + codebase should be a polished portfolio piece.
- Data is being automatically updated.

## [Teams](../semesters/spring_2026/people.csv)

## Part 1

### Goals

Your group will pick an initial:

- Problem space
- Dataset

Part of this project is getting experience with automated data ingestion. Doing so is more interesting with data that changes regularly. You can incorporate additional datasets in the future.

### Steps

Do the following as a group:

1. Discuss what you'd like your project to focus on. Don't need to get _too_ specific yet.
1. Explore [datasets that are updated weekly (the more often, the better)](data.md#datasets-that-are-regularly-updated) and pick one.
1. Create a new notebook in [Google Colab](https://colab.research.google.com/).
1. Ensure you can load the data.
1. Narrow down on 1-3 research questions.
   - In other words, at the end of this project, what do you want to be able to show?
1. Draw an example visualization that you'd like to produce.
   - You can do so digitally or on a piece of paper.
   - Include a title, legend, and axes labels (where appropriate).
   - This is just a sketch; don't worry about the specific values.

### Proposal

You will then submit the following to the Discussion on [Ed](https://courseworks2.columbia.edu/courses/233896/external_tools/37606?display=borderless):

- **What dataset are you going to use?**
  - Please include a link.
- **What are your research question(s)?**
  - It should be _specific, and objectively answerable_ through the data available.
- **What's the link to your notebook?**
  - Go to Share -> General access -> LionMail -> Commenter.
- **What's your target visualization?**
  - Include a picture.
- **What are your [known unknowns](https://en.wikipedia.org/wiki/There_are_unknown_unknowns)?**
- **What challenges do you anticipate?**

Only one person from your group needs to submit. None of this is set in stone long term, it is just a starting place. It can all be changed later.

## [Lab 3](../labs/lab_03.md)

## Part 2

**Goal:** Get experience with an application development framework

### Steps

1. Using your dataset from [Part 1](#part-1):
   1. Create a [Streamlit](https://streamlit.io/) app.
   1. Deploy the app.
   1. Add a visualization.
      - You _can_ get fancy, but don't _have to_ at this stage. Get something simple working first.
1. Bring in a second relevant dataset. (This one doesn't need to be regularly updated.)
   - This can be shown on [a separate page](https://docs.streamlit.io/get-started/fundamentals/additional-features#pages) of your Streamlit app, or combined in a single visualization.
1. Add the names of the people on your team to your Streamlit app homepage.
1. Turn in the link to your live app via CourseWorks.

### Tips

- You can load data:
  - from a URL (preferred), either:
    - An API
    - A link to a CSV
  - from a file, checked into the repository
- Note the [Streamlit app resource limits](https://blog.streamlit.io/common-app-problems-resource-limits/).
- At this stage, feel free to [make the dataset small](https://python-public-policy.afeld.me/en/columbia/assignments/open_ended.html#reducing-data-size) to get it working.
- If the app is slow to reload, experiment with [caching](https://docs.streamlit.io/get-started/fundamentals/advanced-concepts#caching).

## Part 3

**Goal:** Get experience with unit testing

### Steps

Work on branches and submit pull requests for the chunks of work — you decide what the "chunks" are.

1. Without writing any code:
   1. Review your existing code.
      - What can be refactored into functions?
      - Where can we make our code [DRY](https://dzone.com/articles/is-your-code-dry-or-wet)?
   1. Decide what function you're going to create.
   1. Come up with test cases (inputs) and expected outputs.
      - This can be in a text file, doc, piece of paper, etc.
1. Then, as code:
   1. Write tests.
   1. Confirm they fail.
   1. Refactor your code into the function.
   1. Make the tests pass.
1. Repeat until you feel your code is well-organized and well-tested.
1. [Submit the links to the pull requests via CourseWorks.](https://courseworks2.columbia.edu/courses/233896/assignments)

### Outcome

As a result, your:

- "main" scripts (for [Streamlit pages](https://docs.streamlit.io/get-started/fundamentals/additional-features#pages) or otherwise)
- Functions

should be relatively short and easy to read.

This isn't a one-time thing; continue testing and refactoring as you continue with the Project.

## [Lab 6](../labs/lab_06.md)

## Part 4

### Retro

You will hold a team retrospective, with the goal of improving how your team works together. Since the groups are small, it can be fairly informal.

1. Schedule 45 minutes for the retro.
   - The retro needs to be done live/synchronous, not asynchronous.
1. [Read about retros.](https://www.atlassian.com/agile/scrum/retrospectives)
1. Decide who will be the Facilitator.
   - Optional: Get someone from outside the team.
1. Facilitator: Set up [EasyRetro](https://easyretro.io/). [Instructions.](https://www.youtube.com/watch?v=Yl6wV7EIRBw)
1. In the actual retro:
   1. Read the [Agile Prime Directive](https://retrospectivewiki.org/index.php?title=The_Prime_Directive) out loud.
   1. **5 minutes:** Individually write down "what went well" and "what could be better".
   1. **10-15 minutes:** Discuss what has gone well.
   1. **20-25 minutes:** Discuss what could be better.
   1. **5 minutes:** Document takeaways / action items.

### Analysis

1. Move your [Proposal](#proposal) to the Streamlit app as is.
   - [How to add text elements](https://docs.streamlit.io/develop/api-reference/text)
1. Revisit the Proposal.
   - Any new insights?
   - Anything you want to adjust?
1. Document any changes to the Proposal on the Streamlit page.
1. Proceed with the analysis.
   - If the majority of your code (to call APIs, etc.) is in modules/functions, it can be `import`ed from a Jupyter notebook. You can do exploratory analysis there, moving things to modules/Streamlit as you go.
   - You might not be able to fully answer the question(s) yet, but get as close as you can.

At this point, your project should be looking more like one of the [examples](#inspiration). Looking through the [Streamlit data elements](https://docs.streamlit.io/develop/api-reference/data) may be helpful.

### Submit

[Submit](https://courseworks2.columbia.edu/courses/233896/assignments) links to:

- The EasyRetro board
- Jupyter notebook(s), if any
- The (updated) Streamlit app

## Part 5

**Goal:** Understand how to work with a cloud-based database

### Notes

- A [service account](https://cloud.google.com/iam/docs/service-account-overview) has been created in your Project for you. It has been given read-only access to BigQuery.
- There are various things that can go wrong in these steps. **Don't wait until the last minute.**

### Steps

Do the following for your regularly-updated data source. Only do one for now — we'll do the rest in [Lab 10](../labs/lab_10.md).

1. Install [pandas-gbq](https://pandas-gbq.readthedocs.io/).
1. Load data.
   - Create a Python script that:
     1. Creates the table, if it doesn't exist
     1. Pulls data from your data source
     1. Copies the data to BigQuery using the appropriate [technique](../labs/lab_08.md#data-loading)
   - Since you'll be running the script locally, [authenticate with a user account](https://pandas-gbq.readthedocs.io/en/latest/howto/authentication.html#authenticating-with-a-user-account).
   - [How to write tables with pandas-gbq](https://pandas-gbq.readthedocs.io/en/latest/writing.html)
   - How will you know it worked as intended?
1. Have your app use BigQuery.
   1. Each team member will need to:
      1. [Create a service account key](https://cloud.google.com/iam/docs/keys-create-delete#iam-service-account-keys-create-console) as JSON. The service account is `streamlit@[project].iam.gserviceaccount.com`.
      1. Set up [secrets management](https://docs.streamlit.io/develop/concepts/connections/secrets-management) locally.
         - Make sure to **add `secrets.toml` to your `.gitignore`** so that you don't accidentally commit it to Git.
      1. [Copy the key information to your `secrets.toml` file.](https://docs.streamlit.io/develop/tutorials/databases/bigquery#add-the-key-file-to-your-local-app-secrets)
   1. Modify your app to [read data from BigQuery](https://pandas-gbq.readthedocs.io/en/latest/reading.html).
      - [Simplified example](../examples/bigquery/query.py)
   1. [Copy the secrets to your deployed app.](https://docs.streamlit.io/develop/tutorials/databases/bigquery#copy-your-app-secrets-to-the-cloud)
   1. Re-deploy.
1. [Submit the links via CourseWorks](https://courseworks2.columbia.edu/courses/233896/assignments) for:
   - The pull request(s)
   - The link to your live Streamlit app

## [Check-in][check-in]

- We'll do this once now, once [at the end](#final-check-in).
- This will be factored into an [individual score](../README.md#grading).

## [Lab 10](../labs/lab_10.md)

## [Lab 11](../labs/lab_11.md)

## Part 6

### Data flow

Visually map your data flow, end to end.

- What happens at each step?
- What can go wrong?
- Get granular
- Go all the way upstream. How does the data get collected/generated?
- You can use:
  - Paper
  - [Google Drawings](https://docs.google.com/drawings)
  - A fancier diagramming tool
    - Don't over-complicate this

### Submit

[Submit via CourseWorks:](https://courseworks2.columbia.edu/courses/233896/assignments)

- An image of / a link to your map
- Link(s) to:
  - Your pull request(s)
  - A successful run of the GitHub Action

## [Lab 13](../labs/lab_13.md)

## Part 7

**Goal:** Determine and prioritize TODOs

You'll do [this prioritization exercise](https://www.atlassian.com/team-playbook/plays/prioritization-matrix) as a group.

- This must be done synchronously.
- Look back at the [expectations](#expectations).
- The Prep can be done in the meeting itself.
- You can use paper/stickies or a digital template like [Miro's](https://miro.com/templates/simple-priority-matrix/)

[Submit a photo/link to the matrix via CourseWorks.](https://courseworks2.columbia.edu/courses/233896/assignments)

## Part 8

### Refinement

**Goal:** Meet the [expectations](#expectations)

Do tasks you came up with in the prioritization exercise in order of priority.

### Presentation

**Goal:** Force clarity of the project and code by having to show and explain them to others

Each group will do a presentation on their Project in class.

- 10-ish minutes
- Slides optional
- Everyone in the group should speak.
- Explain the initial [proposal](#proposal) and how it's evolved.
- Show the live app.
- Walk through the code.
- Talk through your findings.

## Final [check-in][check-in]

[check-in]: https://docs.google.com/forms/d/e/1FAIpQLSdUCkGB7mkkp5E0Lymko0VwZqFvShEsa0j7KKmkgRQNhM30xg/viewform?usp=header
