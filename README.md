# Static Site Generator

A simple static site generator built in Python as part of the Boot.dev curriculum.

## Features

- Converts Markdown files into HTML pages
- Uses an HTML template for consistent page layout
- Copies static assets like CSS and images
- Supports recursive content generation
- Supports configurable base paths for deployment
- Deployable with GitHub Pages

## Project Structure

```text
.
├── content/        # Markdown content
├── docs/           # Generated site output
├── src/            # Python source code
├── static/         # Static assets
├── template.html   # HTML template
├── build.sh        # Production build script
```

## Run Locally

```python
python3 src/main.py
```

This builds the site into the `docs/` directory using the default base path `/`.

## Production Build

```bash
./build.sh
```

This builds the site for GitHub Pages using the repository base path.

## Deployment

This project is deployed using GitHub Pages from the `main` branch and the `docs/` directory.

Notes
This project was built for learning purposes and focuses on the core ideas behind static site generation.
