Writeup

1.Set data structure is used to store the key value pairs and scard function is used to count the unique food items.

2.To extract the information from nutrition file which is a json file I have used nested loop and this information is decoded to get unique data values and pushed into set and extract the set and get the count using scard function which returns unique values.

3.In this program I have used sorted hash table which add the unique values in to hash set here Zincrby is used to push the values into hash which will gives the values in sorted order. I can extract the first five values using sorted order and Zrange function will give the first few elements with the maximum values.

4.Using the nested loop I have extracted the Nutrition JSON object and I have found the count of number of repetitions by pushing the value into the list.  I have pushed the outer ID into a different list to get the number of food items present. I have found the ratio to find the average.

5.Stored all the values into MyList13 and pushed nutrition values into MyHash9. Pushed nutrition tag name into the TagNameSet hash tables and inserted values of ID into MainColl.
