"""
A helper module that converts sql data to json objects

author: Devan Kavalchek
"""

from datetime import datetime, date

def jsonify_sql(data, columns):
    """
    Converts sql data into JSON format

    Parameters:
        data: SQL data retrieved with psycopg
        columns: A list of column names, in the same order as the data
    """
    result = []

    if len(data) == 0: # Check if there is no data
        return [] # Return an empty list
    else:
        for object in data:
            current = dict() # Create a hashmap for the current object to represent a json object

            for i in range(0, len(columns)): # Iterate the number of columns
                column = columns[i] # Get the current column
                value = object[i] # Get the current value

                if isinstance(value, (datetime, date)): # Check if the value is a datetime object
                    value = value.isoformat() # Parse the datetime object

                current[column] = value # Create a key-value pair in the hashmap, with the key
                                        # being the column and the value being the value

            result.append(current) # Add the hashmap to the array
        
        return result # Return the array of json objects