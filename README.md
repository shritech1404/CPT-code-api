
# CPT and HCPCS Code Search REST API

This Rest API made for medical code search (CPT & HCPCS). where you just have to give subset of description or procedure so it returns CPT or HCPCS code, matched procedure, category and matching score.


## API Reference

#### Get all codes

```http
  GET /code/procedure name
```

#### API 

```http
  GET https://cpt-code-search.herokuapp.com/code/procedure name
```

#### Example


```http
  GET https://cpt-code-search.herokuapp.com/code/cardiac catheterization procedure
```





## Usage/Examples (using python)

```python
import pandas as pd
import requests as rapi
import random
import json

def local_RestApi(searchs):
    lst,lst1,lst2,lst3,lst4,lst5 = [],[],[],[],[],[]
    for i in searchs:
        res = rapi.get(f'https://cpt-code-search.herokuapp.com/code/{i}')
        dt = json.loads(res.text)
        if dt['data']:
            lst.append(i)
            for j in dt['data']:
                lst1.append(j['score'])
            maximum = max(lst1)
            index = lst1.index(maximum)
            try:
                lst2.append(dt['data'][index])
            except:
                lst2.append(dt['data'][0])
    for k in lst2:
        lst3.append(k['CPTCode'])
        lst4.append(k['score'])
        lst5.append(k['matchedDescription'])
    df = pd.DataFrame()
    df['procedure'] = lst
    df['CPT_HCPCS_Code'] = lst3
    df['score'] = lst4
    df['api_procedure'] = lst5
    return df
}
```


## Authors

- [Shrikant Shejwal](https://github.com/shritech1404)

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shrikant-shejwal-930a4519b/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/)


## Installation

Install requirements with pip

```bash
  pip install -r requirements.txt
```
    
