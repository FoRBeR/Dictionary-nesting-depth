# Dictionary nesting depth

This function looks for the number of dictionaries in the longest branch. Returns the number of elements, excluding the base (passed to it) dictionary.
Also, if there is a list in the dictionary, the function takes into account the dictionaries in this list (This also works for a dictionary in a list nested in another list, etc.)

---

### Description of functions.

The `dicts_in_list()` function takes a list as an argument, returns a list of all dictionaries in the list, as well as in all nested lists (recursion is used).

The `dict_len()` function takes a dictionary as an argument. Returns a number indicating the nesting depth. For each dictionary inside the argument, the function is called recursively, for each list, the function described above is used.
