# Lecture 4

---

🤪

---

## Will troubleshooting

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

Remember [when we were working with APIs](https://computing-in-context.afeld.me/lecture_22.html#api-calls-in-the-wild)?

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
```

---

### [wget](https://www.gnu.org/software/wget/)

Like cURL, but for downloading files.

---

## [Streamlit](https://docs.streamlit.io/)

---

Readings will be updated
