# Big Data – Hadoop Assignment 2

**Students:** Mor Zorin and Noa Allouche

## Exercise 1 – Changing the Number of Reducers

| Counter | First run | Second run |
|---|---:|---:|
| Launched map tasks | 9 | 9 |
| Launched reduce tasks | 3 | 6 |
| Merged Map outputs | 27 | 54 |
| Output data files | 3 | 6 |
| Total files (including `_SUCCESS`) | 4 | 7 |

### Q1. How many files are there?

After the second run, there are six output data files (`part-00000` through `part-00005`) and one `_SUCCESS` file, seven files in total.

### Q2. Did the number of mappers change?

No. It remained 9 because the input files and input splits did not change.

### Q3. Did the number of reducers change?

Yes. It increased from 3 to 6.

### Q4. Did the number of output files change? Why?

Yes. The number of output data files increased from 3 to 6 because each reducer writes its own output file. The `_SUCCESS` file is a status marker, not a data file.

### Q5. What does the value of 'Merged Map outputs' represent, and how is it calculated?

It counts the intermediate map outputs merged by the reducers. In these runs, each reducer receives one partition from each of the nine mappers.

- First run: 9 × 3 = 27.
- Second run: 9 × 6 = 54.

## Exercise 2 – Case-Insensitive Word Count

### Q1. Is your change in the mapper or in the reducer?

The change is in the mapper. We convert each word to lowercase and remove trailing commas and periods using `word.lower().rstrip('.,')`. Empty tokens are skipped. This ensures that different forms of the same word are grouped under the same key before the reduce phase. The reducer remains unchanged.

### Q2. our code

The number of distinct output words decreased from 77,928 to 54,591.

## Exercise 3 – Top Three Most Frequent Words

### Q1. Is your change in the mapper or in the reducer?

The change is in the reducer. It calculates the total count of each word, sorts the results by count in descending order, and outputs only the first three entries. We use one reducer (`-numReduceTasks 1`) to obtain the global top three words rather than a separate top three from each partition. The mapper is unchanged from Exercise 2.

### Q2. our code

### Q3. Print the output of the MapReduce and put it on GitHub as an image.

| Word | Count |
|---|---:|
| the | 74,369 |
| and | 42,768 |
| of | 34,588 |

The output contains one data file and the `_SUCCESS` marker. All sorting and filtering are performed inside the Python MapReduce code, without external pipes, sorting, or filters.

<img width="747" height="132" alt="exercise3_output" src="https://github.com/user-attachments/assets/30cf0aa1-266d-4b9e-bba9-bebcaa07d106" />

