# Markdown Cheat Sheet 

---

## 1) Headings

```md
# H1
## H2
### H3
#### H4
##### H5
###### H6
```
Rendered:  
# H1
## H2
### H3
#### H4
##### H5
###### H6

---

## 2) Paragraphs & Line Breaks

- Blank line = new paragraph.  
- End a line with two spaces for a **line break**.

```md
First line␠␠
wraps to a new line.

New paragraph.
```

---

## 3) Emphasis

```md
*italics* or _italics_
**bold**
***bold italics***
~~strikethrough~~
`inline code`
```

---

## 4) Lists

**Unordered**
```md
- Item
  - Nested
- Item
* Also valid
```

**Ordered**
```md
1. First
2. Second
   1. Sub‑item
```

**Task List (GFM)**
```md
- [x] Done
- [ ] To do
```

---

## 5) Links & Images

```md
[link text](https://example.com "optional title")

![alt text](/path/to/img.png "optional title")

Autolink: <https://example.com>
```

Reference-style (helps reuse):
```md
[ChatGPT][gpt]

[gpt]: https://chat.openai.com
```

---

## 6) Code Blocks (Fenced)

Triple backticks, specify language for syntax highlighting:
```md
```python
def add(a, b):
    return a + b
```
```

Indent-based code (less common):
```md
    four leading spaces
```

---

## 7) Blockquotes

```md
> A single quote
>> Nested quote
```

---

## 8) Tables (GFM)

```md
| Column | Type | Notes |
|:------:|:----:|:------|
| id     | int  | centred with : |
| name   | str  | left by default |
```

Rendered:

| Column | Type | Notes |
|:------:|:----:|:------|
| id     | int  | centred with : |
| name   | str  | left by default |

**Multi‑line cells:** use `<br>` for line breaks inside a cell.

---


