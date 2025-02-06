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
- _More to come_

## Teams

1. [Alexa](../people/alexachan.md) and [Giulio](../people/giulio.md)
1. [Angel](../people/angel.md) and [Krishna](../people/Krishna.md)
1. [Arnav](../people/arnav.md) and [Fred](../people/fred.md)
1. [Arshiya](../people/arshiya.md) and [Ijaz](../people/ijaz.md)
1. [Charlotte](../people/charlotte.md), [Hiro](../people/hiro.md), and [Sam](../people/sam.md)
1. Ibrahim and [Isaura](../people/isaura.md)
1. [Naga](../people/naga.md) and [Will](../people/willfrolich.md)

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

Using your dataset from [Part 1](#part-1), create and deploy a [Streamlit](https://streamlit.io/) app that includes a visualization. You _can_ get fancy, but don't _have to_ at this stage. Get something simple working first.

Then, bring in a second relevant dataset. This can be shown on [a separate page](https://docs.streamlit.io/get-started/fundamentals/additional-features#pages) of your Streamlit app, or combined in a single visualization.

Make sure the Streamlit app shows the names of the people in your team. You will turn in the link to your live app.
