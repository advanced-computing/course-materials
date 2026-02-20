# Lecture 4

---

## [Project clarifications](https://github.com/advanced-computing/course-materials/pull/139/changes)

- Dashboard
- Ensure you can load data

---

## Browser Developer Tools

Showing Chrome, but it's [similar in other browsers](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Tools_and_setup/What_are_browser_developer_tools#how_to_open_the_devtools_in_your_browser).

- Brief mention:
  - [Elements (HTML) panel](https://developer.chrome.com/docs/devtools/elements)
    - [View source](https://support.google.com/surveys/answer/6172725)
  - [Lighthouse](https://developer.chrome.com/docs/devtools/lighthouse)
  - [Device mode](https://developer.chrome.com/docs/devtools/device-mode)
- [Network panel](https://developer.chrome.com/docs/devtools/network/overview)

---

## HTTP

---

Remember [when we were working with APIs](https://computing-in-context.afeld.me/lecture-23/#api-calls-in-the-wild)?

```python
requests.get(url)
```

---

- [Status codes](https://http.cat/)
- [Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [Headers](https://developer.mozilla.org/en-US/docs/Glossary/HTTP_header)

---

## [Flask example](../examples/flask/)

Visit http://127.0.0.1:5000/echo.

---

## [cURL](https://curl.se/)

```sh
curl -I http://127.0.0.1:5000/echo
curl -X POST http://127.0.0.1:5000/echo
curl -X POST -d "hello" http://127.0.0.1:5000/echo
curl -i http://127.0.0.1:5000/echo > response.txt

curl 'http://127.0.0.1:5000/divide?numerator=5&denominator=2'
curl 'http://127.0.0.1:5000/divide?denominator=2&numerator=5'
curl 'http://127.0.0.1:5000/divide?numerator=5&denominator=0'
curl 'http://127.0.0.1:5000/divide?numerator=5&denominator=abc'
curl 'http://127.0.0.1:5000/divide?numerator=5'
```

---

### [wget](https://www.gnu.org/software/wget/)

Like cURL, but for downloading files.

---

## [Streamlit](https://docs.streamlit.io/)

---

## Reading response questions

### [Week 3](https://edstem.org/us/courses/89925/discussion/7586157)

#### Design responsibility

- It also raises an important question that the readings only briefly touch on: if users are largely unaware of how files actually work, **who bears responsibility for data loss, privacy breaches, or misuse**---users, designers, or institutions?

---

#### AI & the modern relevance of CLI

- Elements of the command line: the prompt, followed by a command, and an option reminds me of talking to an AI chatbot. **Is this the right way of understanding how it works, or are there differences between the two**? I guess one key difference is perhaps that your computer can't "talk back to you", but instead, runs your command, unlike a chatbot.
- The video mentioned that early interfaces prioritized making things easy for computers, not humans. **Will AI change this?** When we can talk to computers in natural language, will command lines become like Latin---something only specialists need?
- Does the **efficiency of the CLI still hold true for professionals whose main focus is policy analysis** rather than software engineering?

---

## Week 4

### Virtual environments

One thing that I'm still unsure of is **when to use the global environment versus activating my virtual environment**. I understand that virtual environments should be created and activated for each project - but **how many projects is too many? What if I forget which virtual environment is for which project?** Do I need to keep track of my Notes app?

---

### Jupyter Notebook vs. Streamlit

The power of Streamlit, which transforms python scripts into interatctive apps in a second, is amazing [...] However, since Jupyter notebook has similar functions, which is Python-friendly and shows output immediately, **I wonder which tools we should choose, what kind of differences are between these two.**

---

### Internet architecture

- Overall, I would benefit from a **quick review of the whole architecture** laid out in chapters 3 and 5, even though well illustrated it was a decent amount of new information.
- I am unsure what it is referring to by **"packets".**
