# dau-flask app

## CLI wrapper

```shell
dau() { urlenc=$(jq -rn --arg x "$*" '$x|@uri'); curl "https://$COMPOSE_TRAEFIK_HOSTNAME/$urlenc"; }
```

## Alfred workflow

Ask me
