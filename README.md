# Website
link to site
https://nubeio.github.io/rubix-ce-docs/

This website is built using [Docusaurus 2](https://docusaurus.io/), a modern static website generator.

### Installation

build test

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

## doc generation from golang to md

for doc generation use `github.com/robertkrimen/godocdown`

```
go install github.com/robertkrimen/godocdown/godocdown
```

```
cd /home/aidan/code/go/module-core-rql/apirules
godocdown 
```

to replace `####` with `###`
```
sed -i -e 's/####/###/g' rql.md
```

example 
```
cd /home/aidan/code/go/rubix-ce-docs/docs/rubix-ce/services
sed -i -e 's/####/###/g' rql.md
```