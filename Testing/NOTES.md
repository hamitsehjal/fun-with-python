# Testing 
- Unit Test: Verifies that one specific aspect of a function's behavior is correct 
- Test Cases: Collection of *Unit Tests* that together proves that a function behaves as its supposed to be, withing the full range of situations you expect it to handle

### What's a good Test Case ?
- considers all possible kind of inputs a function could receive and,
- include tests to represent each of these situations

### How do you write a Test ?
- Call the function you want to test
- Make an *assertion** about it; what is a `assertion` ?
- An *assertion* is a claim about a condition
*Simple huh !!*

## Testing with `pytest`
1. The name of the `file` is important; it must start with `test_`; Why ??
2. When we ask `pytest` to run the tests we have written, it will look for any file that begins with `test_` and run all the tests inside the file

### Test functions
1. *test functions* should start with word `test` followed by an `_` i.,e `test_`; Why ??
2. Any function that starts with `test_` will be discoverd by `pytest`, and will run as part of the testing process
3. Test names should be longer and more descriptive than a typical function.

