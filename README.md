# Website
Link to the Nube iO website
https://nubeio.github.io/rubix-ce-docs/

This website is built using [Docusaurus 2](https://docusaurus.io/), a modern static website generator.

### Installation

Build Test

```
yarn
```

### Local Development

```
yarn start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

### Build

```
yarn build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

### Deployment

Using SSH:

```
USE_SSH=true yarn deploy
```

Not using SSH:

```
GIT_USER=<Your GitHub username> yarn deploy
```

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.

## PDF page-format registry

PDF guides are built by `docs/Zone Controller Stack/pdf-toolkit/build.sh`. Page
size is an argument, and the CSS chain is:

```
anywair-brand.css      engine + skin — layout, colours, fonts. No page dimensions.
page-<size>.css        page size, margins, type scale, image scale — pick exactly one
```

**A5 output is built at A5. Nothing is ever shrunk to reach a format.**

### Supported formats

| Format | File | Trim (mm) | Margins (mm) | Column | Body | Use |
|---|---|---|---|---|---|---|
| A5 | `page-a5.css` | 148 × 210 | 15 / 13 / 14 / 13 | 122mm | 10pt | **Print deliverable** — saddle-stitched booklet |
| A4 | `page-a4.css` | 210 × 297 | 22 / 18 / 20 / 18 | 174mm | 11pt | Screen / desk reference only |

Every output filename ends in `-A4` or `-A5`. There are no unsuffixed PDFs —
nobody should have to open a file to find out what size it is.

```bash
pdf-toolkit/build.sh                 # all guides at A5 (default)
pdf-toolkit/build.sh --a4 --toc      # A4, with a Table of Contents page
```

### Adding a format

Copy `_page-template.css` to `page-<name>.css`, fill in the values, and add a
row above. No change to `anywair-brand.css` is needed. If a new format needs a
*rule* rather than a *value*, that rule belongs in `anywair-brand.css`.

### Floors — these do not scale

| Limit | Value | Why |
|---|---|---|
| Body text | **9pt min** | below this it fails as printed instruction material |
| Margins | **10mm min** | trimming tolerance on saddle-stitched booklets |
| Gutter side | **+3mm** | on the bound edge, or text disappears into the fold |
| Any image | **~40mm min** | screenshots with UI labels stop being legible |

When a format hits a floor, the answer is **less content per page, more
pages** — never smaller type.

Note: image tiers are percentages of the text column, but images inside table
cells and inside `.img-row` flex rows use absolute lengths — a percentage
there resolves against the cell/flex item, not the column, and collapses.

## Doc Generation from Golang to MD

For doc generation use `github.com/robertkrimen/godocdown`

```
Go to install github.com/robertkrimen/godocdown/godocdown
```

```
cd /home/aidan/code/go/module-core-rql/apirules
godocdown 
```

To replace `####` with `###`
```
sed -i -e 's/####/###/g' rql.md
```

Example 
```
cd /home/aidan/code/go/rubix-ce-docs/docs/rubix-ce/services
sed -i -e 's/####/###/g' rql.md
```
