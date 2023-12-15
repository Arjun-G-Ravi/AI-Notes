## Optimising the ML code

Whenever we are creating an algorithm, we have to make sure that it is efficient. It can be done by:
- Replace as many loops as possible by vectorisation.
- Use appropriate data structures <- CANT STRESS ENOUGH
- Unless you know exactly what you do, always prefer using popular libraries to writing your own scientific code. They have many methods implemented in the C programming language for maximum efficiency.
- If you need to iterate over a vast collection of elements, use generators that create a functionthat returns one element at a time rather than all the elements at once. This will be a massive gain in the memory department.
- Use the cProfile package in Python to find inefficiencies in your code.
- Use multiprocessing package to run computations in parallel. Multithreading sucks because of GIL.
- Compilation of python code with PyPy, Numba, Pytorch 2.0, etc
- The data should be meaniningful. It must be properly preprocessed also.