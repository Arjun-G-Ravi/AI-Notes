# Linear Algebra
Study of vectors and rules to manipulate them

# Vectors
vectors are mathematical objects that represent a quantity with both magnitude and direction. From an abstract standpoint, any object that supports vector addition and scalar mulitplication is a vector.

# System of Linear Equations
- 2 way to express it:
  - Row form: as A@x = b
  - Column form: as x1@col1 + x2@col2 + ... = b

- A@x is the combinations of the columns of A.

## Elimination method for solving system of linear eqns
- Using pivots, make the coefficient matrix upper triangular
- 0 cant be pivots, then exchange row

## Back substitution
- Take augmented matrix and do elimination to make it upper triangular
- Put them back in the original eqn to check
- Solve for the variables

# Note
- A matix @ vector -> linear combination of columns of matrix
- A vector @ matrix -> linear combination of rows of matrix

# Reference
- MIT Gilbert Strang class
- https://mml-book.github.io/