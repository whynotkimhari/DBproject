# DATABASE PROJECT 
<sub>this project is mid test in my IT004 class at UIT</sub>

## [PHASE 1a](https://github.com/whynotkimhari/DBproject/tree/main/Phần%201a)
This part describes the schema, spliting data to tables, relations among tables, and normalizing data before push it into code.<br/>

First, let's talk about how chaos the data is. Giving the [data]() a deep glance to see that some school_id may not similar to others, i.e the format is 'dddddddd' but some are 'ddddddd' (just 7 chars) or ''ddddddd' (yeah, i'm wrongly type. They have ' in there id)<br/>

Secondly, the data in each cell may contain a comma, so we need to eliminate it cause it is so hard to work with and may cause unpredictable wrong<br/>
Finally, you may find that some school_id in xlsx files are "ddd,ddd,dd" -> we need to fix it to "dddddddd"

Above 3 obstacles can be fixed by using xlsx such as Ctrl H, Ctrl 1, ...
```bash
The 2 below pics show that what are the tables' structure and relation.
```
![structure](https://github.com/whynotkimhari/DBproject/blob/main/schema.png)
![relation](https://github.com/whynotkimhari/DBproject/blob/main/schema2.png)

## [PHASE 1b](https://github.com/whynotkimhari/DBproject/tree/main/Phần%201b)
```bash
Creating schema following above structre
```

## [PHASE 2](https://github.com/whynotkimhari/DBproject/tree/main/Phần%202)
