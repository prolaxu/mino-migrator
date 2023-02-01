
# Mino Migrator

Simple tool  to migrate  chunk of data from one bucket to another in different minio servers.




## Installation

Install my-project with git

```bash
  git clone https://github.com/prolaxu/mino-migrator.git
  cd mino-migrator
  pip install requirements.txt
  
```

## Configuration 

Config server info on config.json

```bash
  {
    "from_bucket":{
        "endpoint":"127.0.0.1:9000",
        "access_key":"minioadmin",
        "secret_key":"minioadmin",
        "secure":false,
        "bucket":"yubasangh"
    },
    "to_bucket":{
            "endpoint":"127.0.0.1:9000",
            "access_key":"minioadmin",
            "secret_key":"minioadmin",
            "secure":false,
            "bucket":"testbucket"
    }
}
```
#### Note : You can also user different server as long as you have access. 😀

## Migrate 

Finally after all config change just run minio-migrator.py
```
    python minio-migrator.py
```


## Author

- [@prolaxu](https://www.github.com/prolaxu)

