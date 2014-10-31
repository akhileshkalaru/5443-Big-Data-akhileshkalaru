 believe file size matters when we are processing the data but at the same time we need to make sure the data is much organized form making the conversion. Keeping this in mind the YAML to JSON conversion is the best. I have identified that there are pre built functions provided in Java for making the conversion.

```

private static String convertToJson(String yamlString) {
    Yaml yaml= new Yaml();
    Map<String,Object> map= (Map<String, Object>) yaml.load(yamlString);
 
    JSONObject jsonObject=new JSONObject(map);
    return jsonObject.toString();
}
```
 
Before writing the above code I will add the org.json and SnakeYAML libraries for making the conversion. After making the conversion of each line I will send the output to a file this will have some of the processing time for making the conversion.
 
I believe this will take much lesser time than any other conversion as the input file size is small and in the second case the file is very much organized.

After the Compression of the files:

| Type | Description                                  | Size    |Compressed size|   %   |
|------|----------------------------------------------|---------|---------------|------:|
| csv  |Comma seperated values                        | 484MB   |     59MB      | 87.8  |
| sql  |Structured Query Language (insert statements) | 467MB   |     60MB      | 87.1  |
| xml  |EXtensible Markup Language                    | 2.3GB   |     75MB      | 96.7  |
| yaml |Yet Another Markup Language                   | 771MB   |     61MB      | 92.0  |
a
