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

## Fixtures
- In testing, `fixtures` helps set up the environment
- Often this means, creating a resource that will be used by more than one resource

### How do you create a `fixture` ?
- In `pytest`, we create fixture by writing a `function` with `decorator` `@pytest.fixture`
- What is a `decorator`? - `directive` placed just before the function defination

### How do you define and use a `fixture`?
1. Define a function with a fixture decorator; This function returns some value(resource) that will be used; For example:
    ```
        import pytest
        from survey import langauage_survey
        .....
        
        @pytest.fixture
        def language_survey():
            """....."""
            language = language_survey("question")
            return language # returning the resource
    ```

2. Pass this function name as parameter to the *test functions* that will use this `fixture`
    
    ```
        def test_store_single_response(language_survey):
            .........
                    
        def test_store_three_responses(language_survey):
            ....

3. When a parameter in a test function matches the name of a function with the @pytest.fixture decorator, the fixture will be run automatically and the return value will be passed to the test function.

### Short summary for using `fixture`
1. write a function that generates the resource that’s used by multiple test functions. 
2. Add the `@pytest.fixture` decorator to the new function, and 
3. add the name of this function as a parameter for each test function that uses this resource.


    ```


