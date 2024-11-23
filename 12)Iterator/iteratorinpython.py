                                          Iterators in Python
                                          ====================
Why should WE use Iterators:
----------------------------------    
=>In modern days, we have a lot of data in our hands, and handling this huge amount of data creates problems for everyone
who wants to do some sort of analysis with that data.So, If you've ever struggled with handling huge amounts of data, and your
machine running out of memory, then WE use the concept of Iterators in Python.

=>Therefore, Rather than putting all the data in the memory in one step, it would be better if we could work with it in bits or some
small chunks, dealing with only that data that is required at that moment. As a result, this would reduce the load on our
computer memory tremendously. And this is what exactly the iterators do.

=> Therefore, you can use Iterators to save a ton of memory, as Iterators don't compute their items when they are generated,
but only when they are called upon
---------------------------------- ----------------------------------
=> lterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, str, and sets.
=> The iterator object is initialized using the iter() method. It uses the next() method for iteration.
=> Here iter() is used for converting Iterable object into Iterator object.
=> next() is used for obtaining next element of iterator object and if no next element then we get an exception called
Stoplteration.
=> On the object Of Iterator, we can't perform Indexing and Slicing Operations bcoz They supply the value on demand .

----------------------------------  ----------------------------------
s = 'Python'
itobj = iter(s)
while True:
    try:
        item = next(s) # Iterate by calling next
        print(item)
    except Stoplteration: # exception will happen when iteration will over
        break
-----------------------------------------
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
-----------------------------------------