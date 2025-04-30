# This script helps generate EC2 instance unique names 
# based on department names and a random alphanumerica suffix to aid in identification. 

import random
import string

#Function for generating a random string for a given length
def generate_unique_name(length=7):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

#Main Script
def main():
    print('Welcome to the EC2 Instance Name Generator!')
    
    num_instances = (input("How many EC2 instances do you need names for?")).strip()
    try:
        num_instances = int(num_instances)
        if num_instances <= 0:
            print('Invalid- Enter a positive number')
            return
    except ValueError:
        print('Input Invalid. Enter a number for instances')
        return

    department = str(input('Please state the name of the departmant(e.g., Marketing, Accounting, FinOps)'))

    acceptable_departments = ["Marketing", "Accounting", "FinOps"]
    if department not in acceptable_departments:
        print('Error, This department is not permitted to use the EC2 Name Generator!')
        return

    #Generate Unique Name for EC2 Instances
    print("\nGenerating instances names for the department:")
    for _ in range(num_instances):
        unique_id = generate_unique_name()
        EC2_instance_name = f"{department}-{unique_id}"
        print(EC2_instance_name)

if __name__ == "__main__":
    main()
