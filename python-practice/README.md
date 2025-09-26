

# This is README for python-practice

## JumbleWord related 

### How to run unit test
```
$ cd python-practice/
$ python -t ./TestJumbleWord.py
```

#### Output
    ✅ Large Paragraph Test Passed Successfully
    ok
    test_non_string_input (__main__.TestJumbleWord.test_non_string_input) ... ✅ Non-string input correctly raised TypeError
    ok
    test_paragraph (__main__.TestJumbleWord.test_paragraph) ... ✅ Paragraph Test: 'apple banana cherry' -> 'ppale naaanb yrehcr'
    ok
    test_single_character (__main__.TestJumbleWord.test_single_character) ... ✅ Single Character Test: 'a' -> 'a'
    ok
    test_two_characters (__main__.TestJumbleWord.test_two_characters) ... ✅ Two Characters Test: 'ab' -> 'ba'
    ok

    ----------------------------------------------------------------------
    Ran 8 tests in 0.002s

    OK