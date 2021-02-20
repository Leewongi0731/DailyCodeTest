# Programmers SQL 고득점 Kit

## SELECT-1([모든 레코드 조회하기](https://programmers.co.kr/learn/courses/30/lessons/59034))

```mysql
SELECT *
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID;
```

## SELECT-2([역순 정렬하기](https://programmers.co.kr/learn/courses/30/lessons/59035))

```mysql
SELECT NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC;
```

## SELECT-3([아픈 동물 찾기](https://programmers.co.kr/learn/courses/30/lessons/59036))

```mysql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS 
WHERE INTAKE_CONDITION = "Sick"
ORDER BY ANIMAL_ID;
```

## SELECT-4([어린 동물 찾기](https://programmers.co.kr/learn/courses/30/lessons/59037))

```mysql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS 
WHERE INTAKE_CONDITION != "Aged"
ORDER BY ANIMAL_ID;
```

## SELECT-5([동물의 아이디와 이름](https://programmers.co.kr/learn/courses/30/lessons/59403))

```mysql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID;
```

## SELECT-6([여러 기준으로 정렬하기](https://programmers.co.kr/learn/courses/30/lessons/59404))

```mysql
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC;
```

## SELECT-7([상위 n개 레코드](https://programmers.co.kr/learn/courses/30/lessons/59405))

```mysql
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1
```



---



## SUM, MAX, MIN-1([최댓값 구하기](https://programmers.co.kr/learn/courses/30/lessons/59415))

```mysql
SELECT DATETIME AS 시간
FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 1
```

## SUM, MAX, MIN-2([최솟값 구하기](https://programmers.co.kr/learn/courses/30/lessons/59038))

```mysql
SELECT MIN(DATETIME) AS 시간
FROM ANIMAL_INS
```

## SUM, MAX, MIN-3([동물 수 구하기](https://programmers.co.kr/learn/courses/30/lessons/59406))

```mysql
SELECT COUNT(ANIMAL_ID) AS count
FROM ANIMAL_INS
```

## SUM, MAX, MIN-4([중복 제거하기](https://programmers.co.kr/learn/courses/30/lessons/59408))

```mysql
SELECT COUNT( DISTINCT(NAME) ) AS count
FROM ANIMAL_INS 
WHERE NAME IS NOT NULL
```



---



## GROUP BY-1([고양이와 개는 몇 마리 있을까](https://programmers.co.kr/learn/courses/30/lessons/59040))

```mysql
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS count
FROM ANIMAL_INS 
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE
```

## GROUP BY-2([동명 동물 수 찾기](https://programmers.co.kr/learn/courses/30/lessons/59041))

```mysql
SELECT NAME, COUNT(NAME) AS COUNT
FROM ANIMAL_INS 
GROUP BY NAME
HAVING COUNT >= 2
ORDER BY NAME
```

## GROUP BY-3([입양 시각 구하기(1)](https://programmers.co.kr/learn/courses/30/lessons/59412))

```mysql
SELECT HOUR, COUNT(HOUR) AS COUNT
FROM (
    SELECT CAST( SUBSTRING(DATETIME FROM 11 FOR 3)  AS signed integer) AS HOUR
    FROM ANIMAL_OUTS
) c
WHERE HOUR >= 9 AND HOUR <= 19
GROUP BY HOUR
ORDER BY HOUR
```

## GROUP BY-4([입양 시각 구하기(2)](https://programmers.co.kr/learn/courses/30/lessons/59413))

```mysql
SELECT HOUR, COUNT(HOUR)-1 AS COUNT
FROM (
    (SELECT CAST( SUBSTRING(DATETIME FROM 11 FOR 3)  AS signed integer) AS HOUR FROM ANIMAL_OUTS)
    UNION ALL (SELECT 0 AS HOUR) UNION ALL (SELECT 1 AS HOUR) UNION ALL (SELECT 2 AS HOUR)
    UNION ALL (SELECT 3 AS HOUR) UNION ALL (SELECT 4 AS HOUR) UNION ALL (SELECT 5 AS HOUR)
    UNION ALL (SELECT 6 AS HOUR) UNION ALL (SELECT 7 AS HOUR) UNION ALL (SELECT 8 AS HOUR)
    UNION ALL (SELECT 9 AS HOUR) UNION ALL (SELECT 10 AS HOUR) UNION ALL (SELECT 11 AS HOUR)
    UNION ALL (SELECT 12 AS HOUR) UNION ALL (SELECT 13 AS HOUR) UNION ALL (SELECT 14 AS HOUR)
    UNION ALL (SELECT 15 AS HOUR) UNION ALL (SELECT 16 AS HOUR) UNION ALL (SELECT 17 AS HOUR)
    UNION ALL (SELECT 18 AS HOUR) UNION ALL (SELECT 19 AS HOUR) UNION ALL (SELECT 20 AS HOUR)
    UNION ALL (SELECT 21 AS HOUR) UNION ALL (SELECT 22 AS HOUR) UNION ALL (SELECT 23 AS HOUR)
) c
GROUP BY HOUR
ORDER BY HOUR
```



---



## IS NULL-1([이름이 없는 동물의 아이디](https://programmers.co.kr/learn/courses/30/lessons/59039))

```mysql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
ORDER BY ANIMAL_ID ASC
```

## IS NULL-2([이름이 있는 동물의 아이디](https://programmers.co.kr/learn/courses/30/lessons/59407))

```mysql
SELECT ANIMAL_ID
FROM ANIMAL_INS 
WHERE NAME IS NOT NULL
ORDER BY ANIMAL_ID ASC
```

## IS NULL-3([NULL 처리하기](https://programmers.co.kr/learn/courses/30/lessons/59410))

```mysql
SELECT ANIMAL_TYPE, IFNULL(NAME, "No name") AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
```

## 



## JOIN-1([없어진 기록 찾기](https://programmers.co.kr/learn/courses/30/lessons/59042))

```mysql
SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME
FROM ANIMAL_INS INNER JOIN ANIMAL_OUTS ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
WHERE ANIMAL_INS.ANIMAL_ID > ANIMAL_OUTS.ANIMAL_ID
ORDER BY ANIMAL_INS.ANIMAL_ID
```

## JOIN-2([있었는데요 없었습니다](https://programmers.co.kr/learn/courses/30/lessons/59043))

```mysql
SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.NAME
FROM ANIMAL_INS INNER JOIN ANIMAL_OUTS ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
WHERE ANIMAL_INS.DATETIME > ANIMAL_OUTS.DATETIME
ORDER BY ANIMAL_INS.DATETIME
```

## JOIN-3([오랜 기간 보호한 동물(1)](https://programmers.co.kr/learn/courses/30/lessons/59044))

```mysql
SELECT ANIMAL_INS.NAME, ANIMAL_INS.DATETIME
FROM ANIMAL_INS LEFT JOIN ANIMAL_OUTS ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
WHERE ANIMAL_OUTS.ANIMAL_ID IS NULL
ORDER BY DATETIME
LIMIT 3
```

## JOIN-4([보호소에서 중성화한 동물](https://programmers.co.kr/learn/courses/30/lessons/59045))

```mysql
SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.ANIMAL_TYPE, ANIMAL_INS.NAME
FROM ANIMAL_INS INNER JOIN ANIMAL_OUTS ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
WHERE ANIMAL_INS.SEX_UPON_INTAKE != ANIMAL_OUTS.SEX_UPON_OUTCOME
```



---



## String, Date-1([루시와 엘라 찾기](https://programmers.co.kr/learn/courses/30/lessons/59046))

```mysql
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME in ( 'Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty' )
```

## String, Date-2([이름에 el이 들어가는 동물 찾기](https://programmers.co.kr/learn/courses/30/lessons/59047))

```mysql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS 
WHERE ANIMAL_TYPE = 'Dog' AND NAME LIKE '%el%' 
ORDER BY NAME
```

## String, Date-3([중성화 여부 파악하기](https://programmers.co.kr/learn/courses/30/lessons/59409))

```mysql
SELECT ANIMAL_ID, NAME, 
    CASE
        WHEN SEX_UPON_INTAKE LIKE '%Neutered%' OR SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O'
        ELSE 'X'
     END AS 중성화
FROM ANIMAL_INS
```

## String, Date-4([오랜 기간 보호한 동물(2)](https://programmers.co.kr/learn/courses/30/lessons/59411))

```mysql
SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.NAME
FROM ANIMAL_INS INNER JOIN ANIMAL_OUTS ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
ORDER BY DATEDIFF(ANIMAL_OUTS.DATETIME, ANIMAL_INS.DATETIME) DESC
LIMIT 2
```

## String, Date-5([DATETIME에서 DATE로 형 변환](https://programmers.co.kr/learn/courses/30/lessons/59414))

```mysql
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```

## 