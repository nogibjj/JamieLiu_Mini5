```sql
INSERT INTO DrinksDB VALUES (
            'Germany', 
            300, 
            200, 
            150, 
            12.5);
```

```sql
SELECT * FROM DrinksDB;
```

```sql
UPDATE DrinksDB SET 
        beer_servings=320,
        spirit_servings=210, 
        wine_servings=160, 
        total_litres_of_pure_alcohol=13.0 
        WHERE country='Germany';
```

```sql
DELETE FROM DrinksDB WHERE country='Germany';
```

