---
sidebar_position: 5
---

# advanced

# running a simulation of rubix-stack on your PC

## install docker
To install docker go to docker [downloads](https://docs.docker.com/get-docker/) and the `select your OS` and install docker

## run
```
docker run -p 1659:1659 -p 1661:1661 -v rubix-volume:/data -e GITHUB_TOKEN=<GITHUB_TOKEN> --rm -it -d --privileged --name bios ghcr.io/nubeio/rubix-bios:1.11.0
```

this will install bios only
then you need to
* install assist by right click on supervisor
* then add a host and right-click install edge