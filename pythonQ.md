## Q. What is GIL. How does it impact concurrency in Python? What kinds of applications does it impact more than others?

	GIL stands for Global Interpreter Lock. Implementations of Python like CPython has GIL built into it, some others don't have it. GIL is a mutex that prevents multiple native threads from executing Python bytecodes at once. This lock is necessary mainly because CPython's memory management is not thread-safe.(Thread-safe implies the code functions correctly during simultaneous execution by multiple threads.) GIL increases speed of single threaded programs and allows integration of C libraries that are not thread safe. But it doesn't allow python programs to take gull advantage of a multiprocessor environment. Works best with multithreaded programs which are i/o bound. Works worst with multithreaded applications which are bound by CPU. To overcome GIL's performance bottleneck in multiprocessor systems, we can use multiple instances of CPython interpreter process rather than going for multiple threads.


## Q. How do you iterate over a list and pull element indices at the same time?

Enumerate function
Example:
	cities = ["london", "new york", "delhi", "moscow"]
	for i, city in enumerate(cities):
		print i, city


## Q. So what is CPython

CPython is the original Python implementation. It is the implementation you download from Python.org. People call it CPython to distinguish it from other, later, Python implementations, and to distinguish the implementation of the language engine from the Python programming language itself.

The latter part is where your confusion comes from; you need to keep Python-the-language separate from whatever runs the Python code.

CPython happens to be implemented in C. That is just an implementation detail really. CPython compiles your python code into bytecode (transparently) and interprets that bytecode in a evaluation loop.

CPython is also the first to implement new features; Python-the-language development uses CPython as the base, other implementations follow.

What about Jython, etc.

Jython, IronPython and PyPy are the current 'other' implementations of the Python programming language; these are implemented in Java, C# and RPython (a subset of Python), respectively. Jython compiles your Python code to Java bytecode, so your Python code can run on the JVM. IronPython lets you run Python on the Microsoft CLR. And PyPy, being implemented in (a subset of) Python, lets you run Python code faster than CPython, which rightly should blow your mind. :-)

Actually compiling to C

So CPython does not translate your Python code to C by itself. It instead runs a interpreter loop. There is a project that does translate Python-ish code to C, and that is called Cython. Cython adds a few extensions to the Python language, and lets you compile your code to C extensions, code that plugs into the CPython interpreter.



## Q. How many ways can you append or concatenate strings? Which of these ways is fastest? Easiest to read?

	Print me the full pathname of every file in this directory tree.
		os.walk()
	
		#!/usr/bin/python
		import sys
		import os

		def listFiles(input_path):
			for root,dirs,files in os.walk(input_path,topdown=False):
				for name in files:
					print os.path.join(root, name)

		if __name__ == "__main__":
			if len(sys.argv) == 1:
				listFiles(".")
			else:
				listFiles(sys.argv[1])
			

## Q. What tools do you use for linting, debugging and profiling?

Linting is the process of running a program that will analyse code for potential errors. Lint was the name originally given to a particular program that flagged some suspicious and non-portable constructs (likely to be bugs) in C language source code. The term is now applied generically to tools that flag suspicious usage in software written in any computer language. Popular linting tools are flake8 and pylint. Flake 8 is simple and concise, pylint has more setup and is more comprehensive/judgemental. You can build it into your editor as well.

Debugging
pdb to step through the python code
Profiling
cProfile to get timing data for each function.


## Q. How do you swap two variables in python?

	a, b = b, a

	This uses the concept called tuple unpacking. In the Right hand side, we pack the two variables into tuple and we unpack it in the left hand in the reverse order.

Extended_ unpacking with *


## Q. How do you enforce ordering for a dictionary-style object?
	collections.Ordered Dictionary ?????????????????????????


## Q. What does maximum recursion depth error mean? How to mitigate the problem?



## Q. How does Python's list.sort work at a high level? Is it stable? What's the runtime?


## Q. What's the difference between a list, dictionary, and array in Python?


Q. What is monkeypatching? How can you do it in Python?


Q. What are some caveats to pickling? Marshaling?



Q. What's your preferred editor?


Q. Do arguments in Python get passed by reference or by value?


Q. Why are functions considered first class objects in Python?



Q. Give an example of filter and reduce over an iterable object


Q. Implement the linux whereis command that locates the binary, source, and manual page files for a command.


Q. What are list and dict comprehensions?


Q. What do we mean when we say that a certain Lambda expression forms a closure?


Q. What is the difference between list and tuple?



Q. Dictionary get function ???


Q. Loop and else construct


Q. with for opening and handling files


Q. try except else finallly



## Q.  __name__ variable


Q functions for unit testing testing in python	



Q. What is Code refactoring?


Q. access times for dictionaries and lists operations


Q. practice writing oop


## Q. default dict vs dict


## Q. How does Python's garbage collection work?


## Q. What is the difference between range and xrange? How has this changed over time?


