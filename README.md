This server validates identity cards / passports / etc via POST request. Request data example:
```
{
    "user_info": {
        "first_name": "Igor",
        "last_name": "Petrov"
    },
    "ic_image_uri": "https://www.aph.com/community/wp-content/uploads/2014/10/cut.jpg"
}
```

Please note, that if you want to run it yourself, you should set google cloud credentials in PATH:

```
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/key.json"
```
