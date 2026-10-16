# Insta-Mass-Reporter
# Work in Progress...
# Instagram Browser Research

A Python and Playwright utility for observing browser network activity during manual Instagram interactions.

**Creator:** [deadbyte.dll](https://github.com/dream-reaper111)

## Overview

`research.py` launches a visible Chromium browser, opens a configured Instagram profile, and prints matching request and response information to the terminal.

Despite the repository name, the current script does not implement mass reporting or automatically submit reports.

## Features

- Visible Chromium browser.
- Persistent local browser profile.
- Configurable target username.
- Request method and URL logging.
- Response status code and URL logging.
- Manual browser interaction.
- Playwright Inspector through `page.pause()`.

## How It Works

1. Opens Chromium using a local profile directory.
2. Registers request and response event listeners.
3. Navigates to the configured Instagram profile.
4. Pauses for manual inspection and interaction.
5. Prints matching network events to the terminal.

The script filters events using an `instagram.com` substring check on URLs. This is a basic text filter, not strict hostname validation.

## Requirements

- Python 3 compatible with your installed Playwright version.
- Playwright Python package.
- Playwright Chromium browser.
- A graphical desktop environment.
- Internet connection.

## Installation

From the project directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install playwright
python -m playwright install chromium
```

On supported Linux systems, if browser dependencies are missing:

```bash
python -m playwright install-deps chromium
```

The dependency command may require administrator privileges.

## Configuration

Edit the `TARGET` variable in `research.py`:

```python
TARGET = "your_test_username"
```

Enter a username without `@` or a full profile URL.

Use your own test account or an account included in an authorized research scope.

## Usage

```bash
source .venv/bin/activate
python research.py
```

A browser window and Playwright Inspector will open.

Log in manually if needed. Use the Inspector’s Resume control when necessary to continue browser activity, then perform the authorized interaction you want to observe.

Watch the terminal for network events.

Example output:

```text
>> GET https://www.instagram.com/...
<< 200 https://www.instagram.com/...
```

- `>>` identifies an outgoing request.
- `<<` identifies an incoming response.
- Numbers such as `200` are HTTP response status codes.

Press `Ctrl+C` in the terminal to interrupt the script.

## Project Structure

```text
.
├── research.py
├── README.md
├── LICENSE
└── ig-research-profile/   # Created locally when the script runs
```

The browser profile directory is relative to the directory from which you launch the script.

## Browser Profile and Privacy

The persistent profile can retain cookies, login sessions, and other browsing data.

Do not publish or share this directory.

Although the script does not explicitly print request bodies or headers, logged URLs may contain sensitive query parameters or identifiers.

Before sharing output or screenshots, remove sensitive information.

Never publish:

- Session cookies.
- Authorization headers.
- CSRF tokens.
- Browser profile contents.
- Account recovery information.
- Unredacted sensitive network logs.

## Recommended .gitignore

Add these entries to `.gitignore`:

```gitignore
.venv/
__pycache__/
*.pyc

ig-research-profile/

.env
.env.*
!.env.example

logs/
*.har
```

## Current Limitations

- No automated reporting.
- No bulk account processing.
- No report-submission confirmation.
- No response-body or request-body logging.
- No built-in file export.
- No retry or navigation-error handling.
- No explicit browser cleanup block.
- URL filtering uses a substring match.
- Events are attached to the selected page, not every future tab.
- A graphical environment is required.
- `page.pause()` intentionally pauses execution for inspection.

## Troubleshooting

### Playwright Is Missing

Activate the virtual environment and install it:

```bash
source .venv/bin/activate
python -m pip install playwright
```

### Chromium Executable Is Missing

```bash
python -m playwright install chromium
```

### Browser Dependencies Are Missing

On a supported Linux distribution:

```bash
python -m playwright install-deps chromium
```

### The Script Appears Paused

The script calls:

```python
page.pause()
```

This opens Playwright Inspector and pauses execution intentionally. Use the Inspector controls to resume.

### No Network Events Appear

Confirm that:

- The page is generating new network activity.
- Execution has been resumed if paused.
- The activity is occurring in the page monitored by the script.
- Matching requests contain `instagram.com` in their URLs.

### Browser Profile Is Locked

Close another browser instance using `ig-research-profile` before starting the script again.

## Potential Improvements

These features are proposals and are not implemented:

- Command-line username configuration.
- Strict hostname filtering.
- URL query-parameter redaction.
- Optional sanitized JSON or CSV logging.
- Request counts and HTTP status summaries.
- Explicit navigation timeouts and error messages.
- Browser cleanup with `try/finally`.
- Browser-context event listeners for multiple tabs.
- Configurable output verbosity.
- Local mock pages for repeatable testing.

## Research Scope

Use this utility for manual learning, debugging, and authorized browser research.

Do not use it to coordinate abusive reporting, replay authenticated actions, or evade platform controls.

## License

See the repository’s `LICENSE` file for applicable terms.
