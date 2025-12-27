# Aireview Mentor

A VS Code extension that helps you **review code** and **explain the part of the code you select** in a file. This extension connects to a Python backend hosted on Render to provide intelligent code explanations.

## Features

- Select a piece of code in any file and get an AI-powered explanation.
- Quickly review and understand complex code snippets.
- Right-click menu support for easy access.
- Connects seamlessly to a Python backend API for explanations.

> Example workflow:
> 1. Highlight the code snippet you want to understand.  
> 2. Right-click and select **Explain with AI**.  
> 3. View the explanation directly in VS Code.

## Requirements

- VS Code version 1.80.0 or higher.
- A running Python backend (hosted on Render) to process code explanations.
- Internet connection (to reach your backend API).

## Extension Settings

This extension does not currently add any custom settings.

## Known Issues

- Works best with Python, JavaScript, and Java code snippets.
- Explanations may be delayed if backend response is slow.

## Release Notes

### 1.0.0

Initial release: Explain selected code snippets via backend API.

### 1.0.1

Minor improvements and bug fixes.

### 1.1.0

Added support for more languages and better response formatting.

---

## Following extension guidelines

Make sure your extension follows the best practices for VS Code extensions:

* [Extension Guidelines](https://code.visualstudio.com/api/references/extension-guidelines)

## For more information

* [Visual Studio Code's Markdown Support](http://code.visualstudio.com/docs/languages/markdown)
* [Markdown Syntax Reference](https://help.github.com/articles/markdown-basics/)

**Enjoy reviewing your code smarter!**
