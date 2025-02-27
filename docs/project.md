# Project

As stated in the [course description](../README.md#course-description):

> Over the semester, students will build a complex end-to-end data system.

This will incorporate:

- Automated data ingestion
- A database
- Web-based interactive data visualization

…all in the cloud. Essentially, we are building a live dashboard, with all the infrastructure behind it.

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

- All code is peer-reviewed, through [pair programming](pairing.md) and/or pull requests.
- All team members are contributing equal amounts.
- It leverages at least one [dataset that's regularly updated](data.md#datasets-that-are-regularly-updated).
- The site doesn't need to [read like a blog post](https://computing-in-context.afeld.me/projects.html#requirements) necessarily, but it should explain what's going on.
- _More to come_

## [Teams](project_teams.csv)

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

You will then submit the following to the Discussion on [Ed](https://courseworks2.columbia.edu/courses/210480/external_tools/37606?display=borderless):

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

## Part 2

### Goal

Get experience with an application development framework

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

### Goal

Get experience with unit testing

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
1. [Submit the links to the pull requests via CourseWorks.](https://courseworks2.columbia.edu/courses/210480/assignments)

### Outcome

As a result, your:

- "main" scripts (for [Streamlit pages](https://docs.streamlit.io/get-started/fundamentals/additional-features#pages) or otherwise)
- Functions

should be relatively short and easy to read.

This isn't a one-time thing; continue testing and refactoring as you continue with the Project.

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

At this point, your project should be looking more like one of the [examples](#inspiration).

### Submit

[Submit](https://courseworks2.columbia.edu/courses/210480/assignments) links to:

- The EasyRetro board
- Jupyter notebook(s), if any
- The (updated) Streamlit app
