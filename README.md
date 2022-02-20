## Meme Image Generator Api

I gave up on the discord on so im making an api for memes using python (Fastapi)

[Api Docs:](https://memegenapi.herokuapp.com/docs/)

URL = https://memegenapi.herokuapp.com/

Working Endpoints:

```
GET /api/abandon

Params:
    Text : str
```
```
GET /api/aborted

Params:
    Image : str (url)
```
```
GET /api/affect

Params:
    Image : str (url)
```
```
GET /api/armor

Params:
    Text : str
```

The api cant do any generating yet but those are the current endpoints.

If you look in the assets folder you will see a list of images/memes im gonna be using for this.


Example:

Url = `https://memegenapi.herokuapp.com/api/abandon/?text=I+like+light+themed+editors`
Response:

![](https://memegenapi.herokuapp.com/api/abandon/?text=I+prefer+light+themed+editors)
