# 0x10-python-network_0

### Mandatory (7)

1. File: 0-body_size.sh - Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.
2. File: 1-body.sh - Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
3. File: 2-delete.sh - Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
4. File: 3-methods.sh - Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.
5. File: 4-header.sh - Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
6. File: 5-post_params.sh - Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
7. File: 6-peak.py, 6-peak.txt - Write a function that finds a peak in a list of unsorted integers.

- Prototype: def find_peak(list_of_integers):
- You are not allowed to import any module
- Your algorithm must have the lowest complexity (hint: you don’t need to go through all numbers to find a peak)
- 6-peak.py must contain the function
- 6-peak.txt must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)
- Note: there may be more than one peak in the list

### Advanced (3)

1. File: 100-status_code.sh - Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
2. File: 101-post_json.sh - Write a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
3. File: 102-catch_me.sh - Write a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.
