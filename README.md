# Methods of Advanced Data Engineering


## Kaggle Authentication
Here kaggle is the dataset provider. For that we need to use their authentication to retrieve a data set.
Using this [link](https://www.kaggle.com/settings) you can download a kaggle.json and place it inside the `/project/kaggle.json`
directory.

**Filepath:** `/project/kaggle.json`

```
{
  "username":"par****a",
  "key":"dc5c*******************01"
}
```

## Give an execute permissions to the script file of the pipeline
```
chmod +x ./project/pipeline.sh
```

## Run pipeline
```
cd project && ./pipeline.sh
```

## Give an execute permissions to the script file of the test pipeline
```
chmod +x ./project/tests.sh
```

## Run test pipeline
```
cd project && ./tests.sh
```