# Component Showcase

This page exercises every themed component using real content about the
[Dracula theme](https://github.com/dracula) project, so visual regressions
are easy to spot during development.

## What is Dracula?

Dracula is a dark theme for code editors, terminals, and hundreds of other
applications, created by [Zeno Rocha](https://github.com/zenorocha). It
started as a single Sublime Text theme and has since grown into one of the
most widely ported color schemes in open source.

### Design goals

# A single color scheme, everywhere
## Consistency across every tool you use
### From the editor to the terminal
#### From the terminal to the browser
##### From the browser to your IDE plugins
###### Down to the smallest utility script

## The philosophy

Dracula follows a few simple rules, explained in **bold**, *italics*,
***bold italics***, and even ~~occasionally~~ always with a bit of
`inline code` for terms like `background`, `foreground`, and `selection`.

Read the [official spec](https://draculatheme.com/contribute) before
porting the theme to a new [application](https://draculatheme.com).

## Why people port it

- It looks good on every screen, day or night
- It is consistent across dozens of tools
    - Editors: VS Code, Vim, Sublime Text
    - Terminals: iTerm2, Alacritty, Windows Terminal
    - Browsers, IDEs, and even Slack

1. Pick a base application to port
2. Follow the official color specification
3. Submit the port for review
    1. Maintainers check contrast and accuracy
    2. Once approved, it ships on draculatheme.com

## In the maintainers' words

> Dracula is not just a theme, it's a community. Every port follows the
> same spec so that switching tools never means switching colors.

## The official palette

```python
palette = {
    "background": "#282A36",
    "current_line": "#44475A",
    "foreground": "#F8F8F2",
    "comment": "#6272A4",
    "cyan": "#8BE9FD",
    "green": "#50FA7B",
    "orange": "#FFB86C",
    "pink": "#FF79C6",
    "purple": "#BD93F9",
    "red": "#FF5555",
    "yellow": "#F1FA8C",
}
```

## Palette reference

| Name         | Hex       | Usage                  |
| ------------ | --------- | ----------------------- |
| Background   | `#282A36` | Editor background       |
| Current Line | `#44475A` | Selection / active line |
| Foreground   | `#F8F8F2` | Default text            |
| Comment      | `#6272A4` | Comments, muted text    |
| Purple       | `#BD93F9` | Keywords                |
| Pink         | `#FF79C6` | Operators                |
| Green        | `#50FA7B` | Strings                 |

## Notes for contributors

!!! note
    Every port must follow the [official spec](https://draculatheme.com/contribute) exactly — no custom colors.

!!! abstract
    tl;dr: fork the [contributing guide repo](https://github.com/dracula/contributing-guide), copy the closest existing port, swap the palette.

!!! info
    Dracula has 400+ official ports, from editors to hardware keyboards.

!!! tip
    Test your port against real code with syntax highlighting before submitting — flat colors alone can hide contrast issues.

!!! success
    Once merged, your port is listed on [draculatheme.com](https://draculatheme.com) and this `mkdocs` theme is one of them.

!!! question
    Not sure which repo to fork? Check the [ports list](https://draculatheme.com) for a project similar to yours.

!!! warning
    Don't rename the official color variables (`--purple`, `--cyan`, etc.) — themes and tooling depend on those names staying stable.

!!! failure
    A port that changes background/foreground contrast ratios below WCAG AA will be rejected in review.

!!! danger
    Never hardcode hex values in component CSS — always reference the palette variables, or the port breaks when the palette updates.

!!! bug
    Found a color mismatch against the spec? Open an issue on the [ports repo](https://github.com/dracula).

!!! example
    This very page is an example: it's built with `mkdocs-dracula-theme`, itself a Dracula port for MkDocs sites.

!!! quote
    "The most famous theme ever created and available everywhere." — [draculatheme.com](https://draculatheme.com)

!!! warning "Before you open a PR"
    Read `CONTRIBUTING.md` in the target repo — most ports have screenshot and structure requirements beyond just the colors.

## Footer

This page's footer is controlled by `theme.show_footer` in `mkdocs.yml`,
linking back to the [dracula/mkdocs](https://github.com/dracula/mkdocs)
repository unless disabled.
