# Website
Link to the Nube iO website
https://nubeio.github.io/rubix-ce-docs/

This website is built using [Docusaurus 2](https://docusaurus.io/), a modern static website generator.

### Installation

Build Test

```
Yarn
```

### Local Development

```
Yarn start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

### Build

```
Yarn build
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

## Generate PDF

To generate PDF from a local Docusaurus instance. You need to first build the site locally:

# Build the site
```bash
yarn build
```

# Serve built site locally
```bash
yarn serve
```

# Generate PDF from local Docusaurus instance
npx docusaurus-prince-pdf -u http://localhost:3000/rubix-ce-docs/docs/overview --include-index --output pdf/rubix-ce.pdf