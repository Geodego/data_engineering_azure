# Data Wrangling with Spark

## Table of Contents

## Functional Programming

### Introduction

One of the hardest parts of learning Spark is becoming familiar with the functional style of programming. Under the 
hood, Spark is written in a functional programming language called Scala.
- When you're programming with functional languages, you end up solving problems in a pretty different way than you would 
if you're using a general purpose language like Python.
- Although Spark is written in Scala, you can use it with other languages like Java, R, and even Python. 

Even when you're using the PySpark API, you'll see the functional programming influence of Scala. For example, in 
the last lesson, you saw a MapReduce problem that counted up the number of times a song was played.
- This code went through each record and spit out a tuple with the name of the song, and the number one.
- The tuples were shuffled and reduced to a sum of the ones that came with each song name.

If you're used to counting with For Loops and found that logic a little strange, it's because this was a functional 
approach to summing up songs

In the procedural style, you'd use a counter variable to keep track of the play count for each song. Then you'd iterate 
through all the songs, and increment the counter by one if the song name matched.

<img src="./0-images/chap2/procedural-functional.png" alt="procedural-functional.png" width=400 />

### Why use functional programming?

The core reason Spark uses functional programming is that functional programming is perfect for distributed systems.
- Functional programming helps minimize mistakes that can cripple an entire distributed system.
- Functional programming gets its name from the functions you saw in your algebra class. These functions are stricter 
than your average Python function because in math a function can only give you one answer when you give it an input. 
On the other hand, Python allows you to make some flexible, albeit complex, functions that depend on the input and 
other parameters.
- When you evaluate a mathematical function, you would never change the inputs of that function, but this is exactly 
what can happen in Python.

### Procedural Programming example
Consider a scenario where executing code updates a global variable to track the play count of a song. Running this code multiple times could yield varied outcomes. This illustrates a fundamental challenge:
- Identifying issues becomes straightforward in such a singular example. However, the complexity escalates when numerous 
machines execute code concurrently, especially if recalculations are necessary due to occasional problems with any of 
the machines.
- In the context of Python programming, the term "function" is frequently used to describe any code following a `def` 
keyword. However, a more precise terminology would differentiate between methods or procedures and true functions, 
indicating that what we often call functions may not adhere to the strict definition of pure functions.

### Pure functions analogy
Imagine your program is like a bread factory, and your function is a specific machine in your factory that makes 
sourdough bread. But since your factory needs to mass-produce bread at a large scale, you need to be a bit more careful.

One thing you'll need to avoid when designing your bread-maker is unintended side effects.
- After each loaf, your machine needs to leave the factory exactly the same as before it ran.
- If you don't, each machine could start interfering with the others.

For example, if running a single bread-maker made the entire factory one degree warmer, then running several of these 
machines all at once would start to heat up the room.

In distributed systems, your functions shouldn't have side effects on variables outside their scope, since this could 
interfere with other functions running on your cluster.
- Your bread making machine needs to get the ingredients without ruining them since other breadmakers will also need them.
- In distributed systems, you also need to be careful with how you design your functions. Whenever your functions run 
on some input data, it can alter it in the process. If your bread-making machine protects the input ingredients and 
doesn't cause any side effects, then you have a smooth and clean operation.

If you write functions that **preserve their inputs** and **avoid side effects**, these are called **pure functions**, 
and your spark code will work well at the scale of big data.

### Spark DAGs
Every Spark function makes a copy of its input data and never changes the original parent data. Because Spark doesn't 
change or mutate the input data, it's known as **immutable**. This makes sense when you have a single function. But what 
happens when you have lots of functions in your program?
- In Spark, you do this by chaining together multiple functions that each accomplish a small chunk of the work.
- You'll often see a function that is composed of multiple sub-functions
- In order for this big function to be peer, each sub function also has to be peer.

If seems that Spark would need to make a copy of the input data for each subfunction. If this was the case your Spark 
program would run out of memory pretty quickly. To avoid this issue, Spark uses a functional programming concept 
called **lazy evaluation**. Before Spark does anything with the data in your program, it first built step-by-step 
directions of what functions and data it will need. In Spark, this is called a **Directed Acyclic Graph (DAG)**. 
Once Spark builds the DAG from your code, it checks if it can procrastinate, waiting until the last possible moment to 
get the data. In Spark, these multi-step combos are called **stages**.

<img src="./0-images/chap2/spark_dag.png" alt="spark_dag.png" width=400 />

### Maps and Lambda Functions
one of the most common functions in Spark is Maps. Maps simply make a copy of the original input data, and transform 
that copy according to whatever function you put inside the map. You can think about them as directions for the data 
telling each input how to get to the output.

After some initialization to use Spark in our notebook, we:
- Convert our log of songs which is just a normal Python list, and to a distributed dataset that Spark can use. This 
uses the special Spark context object, which is normally abbreviated to SC. The Spark context has a method parallelize 
that takes a Python object and distributes the object across the machines in your cluster, so Spark can use its 
functional features on the dataset.
- Once we have this small dataset accessible to Spark, we want to do something with it. One example is to simply convert 
the song title to a lowercase which can be a common pre-processing step to standardize your data.
- Next, we'll use the Spark function map to apply our converts song to lowercase function on each song in our dataset.
- You'll notice that all of these steps appear to run instantly but remember, the spark commands are using lazy 
evaluation, they haven't really converted the songs to lowercase yet. So far, Spark is still procrastinating to 
transform the songs to lowercase, since you might have several other processing steps like removing punctuation, Spark 
wants to wait until the last minute to see if they can streamline its work, and combine these into a single stage.
- If we want to force Spark to take some action on the data, we can use the collect Function which gathers the results 
from all of the machines in our cluster back to the machine running this notebook.
- You can use anonymous functions in Python, use this special keyword Lambda, and then write the input of the function 
followed by a colon, and the expected output. You'll see anonymous functions all over the place in Spark. They're 
completely optional, you could just define functions if you prefer, but there are best-practice, and small examples 
like these.

For more about the theory and origins of lambda functions, take a look at this [blog post](http://palmstroem.blogspot.com/2012/05/lambda-calculus-for-absolute-dummies.html). 
Why are lambda functions called "lambda" functions?

According to legend, the inventor of Lambda Calculus, Alonzo Church, originally used the wedge symbol `∧`
as part of his notation. But the typesetter transcribing his manuscript used `λ` instead. You can read more about it in 
the blog post.

### Distributed Data Stores
When we have so much data that we need distributed computing, the data itself often needs to be stored in a distributed 
way as well.

Distributed file systems, storage services, and distributed databases store data in a fault-tolerant way. So if a 
machine breaks or becomes unavailable, we don't lose the information we have collected.

Hadoop has a Distributed File System, HDFS, to store data. HDFS splits files into 64 or 128 megabyte blocks and 
replicates these blocks across the cluster. This way, the data is stored in a fault tolerant way and can be accessed in 
digestible chunks.

<img src="./0-images/chap2/distributed_data_stores.png" alt="distributed_data_stores.png" width=400 />

If you don't want to maintain your own cluster, most cloud computing platforms like AWS, Azure, and Google Cloud provide 
distributed file systems.

### SparkSession
The first component of each Spark Program is the SparkContext. The SparkContext is the main entry point for Spark 
functionality and connects the cluster with the application.

To create a SparkContext, we first need a SparkConf object to specify some information about the application such as 
its name and the master's nodes' IP address. If we run Spark in local mode, we can just put the string local as master.
```python
from pyspark import SparkContext, SparkConf

configure = SparkConf().setAppName("name").setMaster("IP address")
# in local mode use .setMaster("local")
sc= SparkContext(conf = configure)
```



To read data frames, we need to use Spark SQL equivalentof SparkContext, the SparkSession. Similarity to the SparkConf, 
we can specify some parameters to create a SparkSession. getOrCreate() for example, means that if you already have a 
SparkSession running, instead of creating a new one, the old one will be returned and its parameters will be modified to 
the new configurations.
```python
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("app name") \
    .config("config option", "config value") \
    .getOrCreate()
```

### Reading and Writing Data into Spark Data Frames

In the read_write_df.ipynb notebook we will go through an example of how to import and export data to and from Spark 
data frames using a dataset that describes log events coming from a music streaming service:
- Create a Spark session with parameters.
- Load a JSON file into a Spark data frame called `user_log`.
- Print the schema with the `printSchema` method.
- Try the `describe` method to see what we can learn from our data.
- Use the `take` method to grab the first few records.
- Save it into a different format, for example, into a CSV file, with the `write.save` method
- Use the `read.csv` method

In this video, we went through an example of how to load and save data frames from and to HDFS. If a file is stored in 
S3, you can use the same methods. When specifying the file path we just need to make sure that we are pointing to the 
S3 bucket that stores our target file.

If Spark is used in a cluster mode all the worker nodes need to have access to the input data source. If you're trying 
to import a file saved only on the local disk of the driver node you'll receive an error message similar to this:
```
AnalysisException: u'Path does not exist: 
file:/home/ubuntu/test.csv;'
```
Loading the file should work if all the nodes have it saved under the same path.