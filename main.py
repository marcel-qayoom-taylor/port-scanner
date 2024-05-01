import sys

def main(parameter):
    # Access and print the parameter
    print("Received parameter:", parameter)

if __name__ == "__main__":
    # Check if a parameter was provided
    if len(sys.argv) > 1:
        # Extract the parameter from the command line arguments
        parameter = sys.argv[1]
        # Call the main function with the parameter
        main(parameter)
    else:
        print("No parameter provided.")