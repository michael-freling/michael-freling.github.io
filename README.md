# GitHub pages

## Setup

These are pre requisites.

- [hugo](https://gohugo.io/installation/)
- [git-lfs](https://github.com/git-lfs/git-lfs/blob/main/INSTALLING.md)

## Development

### Add a content

```fish
> hugo new posts/(date +%Y-%m-%d)-$POST.md
```

### Preview

```fish
> make start
```

Open a browser and go to the link `localhost:1313`
