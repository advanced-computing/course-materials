# Advanced Computing for Policy syllabus

- **Course Number:** [INAFU6659](https://vergil.columbia.edu/vergil/course/20251/74227)
- **Instructor:** [Aidan Feldman](https://www.sipa.columbia.edu/communities-connections/faculty/aidan-feldman), [alf2215@columbia.edu](mailto:alf2215@columbia.edu)
- **Teaching Assistant (TA):** [Roberto Zuniga Valladares](https://www.sipa.columbia.edu/communities-connections/faculty/roberto-zuniga-valladares), [rz2516@columbia.edu](mailto:rz2516@columbia.edu)
- **Semester and Year:** Spring 2025
- **Credits:** 3

## Meeting Dates/Times

- **Lecture:** Thursdays 9-10:50am, [IAB][IAB] room 402B
- **Lab, a.k.a. recitation:** Fridays 2:20-3:50pm, [IAB][IAB] room 402B
- [**Office Hours:**](https://calendar.google.com/calendar/embed?src=c_0f46e8283081fed502941bfac7501cd0b8b5cd26635c8f4546e313ef7403e5fa%40group.calendar.google.com&ctz=America%2FNew_York) Make sure you're signed in to your Columbia Google account to view. Also available by appointment.
- [**TA Office Hours**](https://calendar.app.google/7K6UZzfeRxyUaTnn6) By appointment only.

[IAB]: https://maps.app.goo.gl/Hg6dyuWcchZ2DmRB6

[Academic calendar](https://bulletin.columbia.edu/sipa/registration/academic-calendar/)

## Course Description

In [Computing in Context](https://computing-in-context.afeld.me/), students "explore\[d\] computing concepts and coding in the context of solving policy problems." Building off that foundation of Python fundamentals and data analysis, Advanced Computing for Policy goes both deeper and broader. The course covers computer science concepts like data structures and algorithms, as well as supporting systems like databases, cloud services, and collaboration tools. Over the semester, students will build a complex end-to-end data system. This course prepares students for more advanced data science coursework at SIPA, and equips them to do sophisticated data ingestion, analysis, and presentation in research/industry.

## Prerequisites

[Computing in Context (INAFU6006)](https://computing-in-context.afeld.me/). See [info about testing out](docs/testing_out.md).

## Communications

- Grades and assignments will be posted through [Courseworks](https://courseworks2.columbia.edu/courses/210480).
- Troubleshooting and other communications between class sessions will be through [Ed Discussions](https://courseworks2.columbia.edu/courses/210480/external_tools/37606?display=borderless) / GitHub, so that other students can respond and/or benefit from the answers.
  - Email is also an option, though please only use for questions that aren't appropriate for others to see.
  - The instructor/Reader will try to respond within 24 hours, 48 hours max, if someone else hasn't already.

## Grading

- [Attendance: 12%](#attendance)
- [Lab work](labs/): 24% (12 x 2% each)
- Reading responses: 20% (10 x 2% each)
- [Project](docs/project.md): 44%
  - Group work: 32% (divided into eight-ish parts, split to be determined)
  - Individual score: 12%

There will not be an exam.

Data visualizations must have good titles and axis labels.

### Assignment scoring details

- Late work: -5% per day
  - Communication with the instructor/TA is paramount. They are happy to be flexible with requests for extensions made _before the deadlines_.
  - Assignments can be turned in up to a week late, then they won't be accepted.
- Syntax errors: -10 points
- Incomplete Steps / Steps with logic errors: -2 to -5 points
- Unattempted Steps: -10 points

## Readings

See the details and links in the [schedule](#schedule) below. The readings will be finalized one week before they're due.

Books, which are either open access and/or will be placed on [Course Reserves](https://library.columbia.edu/services/reserves.html):

- [Article 19, Knodel, M., Uhlig, U., Oever, N. ten, & Cath, C. (2020). _How the Internet Really Works: An Illustrated Guide to Protocols, Privacy, Censorship, and Governance_ (Illustrated edition). No Starch Press.](https://clio.columbia.edu/catalog/15236654)
  - Strongly recommend [purchasing a physical copy](https://catnip.article19.org/#order).
- [Sweigart, A. (2025). _Automate the boring stuff with Python_ (3rd Edition). No Starch Press.](https://automatetheboringstuff.com/)
- [Wufka, M., & Canonico, M. (2023). _Overview of Cloud Computing_. Overleaf.](https://dc.arcabc.ca/islandora/object/dc%3A54375)

### Additional resources

It's likely that you will need to do reading beyond what is assigned to fill in gaps of understanding. If you're having trouble finding a resource, ask! [Resources from the Python class.](https://python-public-policy.afeld.me/en/columbia/resources.html)

### Responses

For each set of readings (which might include podcasts/videos), you will submit a response in [Ed](https://courseworks2.columbia.edu/courses/210480/external_tools/37606?display=borderless). This might be one or more of:

- A paragraph of reflection
- A list of questions
- A link to a notes doc
- A photo of some [sketchnotes](https://en.wikipedia.org/wiki/Sketchnoting)

Creativity is welcome. The response should do a few things:

- Demonstrate that you did the reading, speaking to / referencing / synthesizing all of them
  - More interested in "a-ha!" moments / how the readings relate to you, rather than a recap of the content.
- Indicate whether the material made sense to you
- Show the instructor/TA where gaps in understanding might be so that we can cover in lecture or subsequent readings
- Encourage discussion

After your initial post, you are encouraged to read and respond to others'.

You can find the rubric under the [Assignment](https://courseworks2.columbia.edu/courses/210480/assignments) in Courseworks.

## Schedule

| Week | Lecure date | Lecture topic(s)                                                  | Assignments due (at the start of lecture)                                     | [Lab](labs/) topic(s)                                          | [Lab](labs/) due (at the start of the Lab session) |
| ---- | ----------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------- |
| 1    | 1/23        | [Welcome; collaborating on code (GitHub)](lectures/lecture_01.md) | none                                                                          | [Computer setup; Git workflow](labs/lab_01.md)                 | none                                               |
| 2    | 1/30        | [Project/product management](lectures/lecture_02.md)              | [Readings](readings/week_02.md)                                               | [Jupyter, pandas, and visualization refresher](labs/lab_02.md) | none                                               |
| 3    | 2/6         | [Command line; dependency management](lectures/lecture_03.md)     | [Readings](readings/week_03.md), [Project Part 1](docs/project.md#part-1)     | [Project setup](labs/lab_03.md)                                | [Lab 2](labs/lab_02.md)                            |
| 4    | 2/13        | [Web development](lectures/lecture_04.md)                         | [Readings](readings/week_04.md)                                               | [Building an API](labs/lab_04.md)                              | [Lab 3](labs/lab_03.md)                            |
| 5    | 2/20        | [Automated testing](lectures/lecture_05.md)                       | [Readings](readings/week_05.md), [Project Part 2](docs/project.md#part-2)     | [Data profiling/quality](labs/lab_05.md)                       | [Lab 4](labs/lab_04.md)                            |
| 6    | 2/27        | [Organizing code](lectures/lecture_06.md)                         | [Readings](readings/week_06.md), [Project Part 3](docs/project.md#part-3)     | [Continuous integration](labs/lab_06.md)                       | [Lab 5](labs/lab_05.md)                            |
| 7    | 3/6         | [Databases](lectures/lecture_07.md)                               | [Readings](readings/week_07.md)                                               | [Databases](labs/lab_07.md)                                    | [Lab 6](labs/lab_06.md)                            |
| 8    | 3/13        | [Guest speaker; data warehousing](lectures/lecture_08.md)         | [Project Part 4](docs/project.md#part-4)                                      | [Data loading](labs/lab_08.md)                                 | [Lab 7](labs/lab_07.md)                            |
| 9    | 3/20        | none ([Spring Recess][recess])                                    | none                                                                          | none ([Spring Recess][recess])                                 | none                                               |
| 10   | 3/27        | [Data engineering (ETL)](lectures/lecture_10.md)                  | [Project Part 5](docs/project.md#part-5)                                      | [Data loading, continued](labs/lab_10.md)                      | [Lab 8](labs/lab_08.md)                            |
| 11   | 4/3         | [Data engineering, continued (pipelines)](lectures/lecture_11.md) | [Readings](readings/week_11.md), [Project check-in](docs/project.md#check-in) | TBD                                                            | [Lab 10](labs/lab_10.md)                           |
| 12   | 4/10        | Infrastructure / cloud computing                                  | [Readings](readings/week_12.md), [Project Part 6](docs/project.md#part-6)     | TBD                                                            | TBD                                                |
| 13   | 4/17        | Big data; algorithms                                              | [Readings](readings/week_13.md)                                               | TBD                                                            | TBD                                                |
| 14   | 4/24        | Privacy                                                           | [Readings](readings/week_14.md), [Project Part 7](docs/project.md#part-7)     | TBD                                                            | TBD                                                |
| 15   | 5/1         | [Presentations](docs/project.md#part-8)                           | [Project Part 8](docs/project.md#part-8)                                      | TBD                                                            | TBD                                                |

[recess]: https://registrar.columbia.edu/content/academic-calendar?acfy=49&acschool=18&acterm=6&field_event_type1_tid%255B%255D=23&keys=#!#e=9806

This is a new course; all of the above is subject to change. Things will be adjusted to the needs and interests of the students.

## Course Policies

### Attendance

Attending class (lectures and labs) is mandatory, but most importantly, important. Learning programming requires commitment from the part of the student and the skills are built out of practice. If you miss an experience in class, you miss an important learning moment and the class misses your contribution.

Missing class counts as an absence, regardless of the reason or notifying the instructor(s) beforehand. Missing more than 20 minutes of a class session will be treated as an absence. The first two absences are treated as "freebies", each subsequent absence will result in a 0.5% deduction from the overall grade.

If you do miss class, we trust that it's for a good reason. If you're sick, please use that freebie and stay home and rest.

You are responsible for getting caught up on what was covered in class. You may want to ask a classmate for notes.

You are expected to bring a laptop to each lecture and lab.

### Academic Integrity

Anything outside of:

- The provided course materials
- Group assignment members

are considered a "source". This includes:

- Other students
- Online resources
- Books
- Generative AI (ChatGPT, Copilot, Gemini, etc.)

If you are copying and pasting from a source, it must be cited. This doesn't need to be in a formal style like APA - a comment (and link, where applicable) is fine.

**If you / your group did most of the work yourself, it's ok. If most of the work was copied from elsewhere, it's plagiarism,** and will be reported. Other notes:

- For individually-submitted assignments, students are welcome to work with one another, as long as:
  - You indicate who you worked with
  - The submissions are different
- Students are more than welcome to share approaches and code snippets in the Discussions, so long as they aren't giving the full solution away.
- Generative AI tools can be incredibly useful, but the code they provide is often incomplete or wrong. Knowing enough about code to critically interpret their results can turn them from a crutch to a superpower.

#### SIPA Academic Integrity Statement

The School of International & Public Affairs does not tolerate cheating or plagiarism in any form. Students who violate the Code of Academic & Professional Conduct will be subject to the Dean's Disciplinary Procedures.

Please familiarize yourself with the proper methods of citation and attribution. The School provides some valuable resources online; we strongly encourage you to familiarize yourself with these various styles before conducting research. Cut and paste the following link into your browser to view the Code of Academic & Professional Conduct and to access useful resources on citation and attribution: [http://bulletin.columbia.edu/sipa/academic-policies/](http://bulletin.columbia.edu/sipa/academic-policies/)

Violations of the Code of Academic & Professional Conduct should be reported to the Associate Dean for Student Affairs.

### SIPA Disability Statement

SIPA is committed to ensuring that students registered with [Columbia University's Disability Services](https://health.columbia.edu/content/disability-services) (DS) receive the reasonable accommodations necessary to participate fully in their academic programs. If you are a student with a disability and have a DS-certified accommodation letter, you may wish to make an appointment with your course instructor to discuss your accommodations. Faculty provide disability accommodations to students with DS-certified accommodation letters, and they provide the accommodations specified in such letters. If you have any additional questions, please contact SIPA's DS liaison at [disability@sipa.columbia.edu](mailto:disability@sipa.columbia.edu) or 212-854-8690.
