import boto3


def display_menu():
    print("What do you want to do?")
    print("1. Create new instance")
    print("2. Start instance")
    print("3. Stop instance")
    print("4. Terminate instance")


def create_ec2_instance():
    try:
        print("Creating EC2 instance")
        image_id = input("Enter the AMI ID: ")
        min_count = int(input("Enter the minimum count: "))
        max_count = int(input("Enter the maximum count: "))
        instance_type = input("Enter the instance type: ")
        key_name = input("Enter the key name: ")
        security_group_ids = input("Enter the security group IDs: ")
        user_data = input("Enter the user data: ")

        resource_ec2 = boto3.client("ec2")
        response = resource_ec2.run_instances(
            ImageId=image_id,
            MinCount=min_count,
            MaxCount=max_count,
            InstanceType=instance_type,
            KeyName=key_name,
            SecurityGroupIds=security_group_ids.split(","),
            UserData=user_data
        )

        instance_id = response['Instances'][0]['InstanceId']
        print("Instance created with ID:", instance_id)
    except Exception as e:
        print(e)


def start_ec2_instance():
    try:
        resource_ec2 = boto3.client("ec2")
        response = resource_ec2.describe_instances()
        instances = response["Reservations"]

        if not instances:
            print("No instances found.")
            return

        print("List of instances:")
        for idx, reservation in enumerate(instances):
            for instance in reservation["Instances"]:
                print(f"{idx + 1}. Instance ID: {instance['InstanceId']}")

        selected_instance = int(input("Enter the number of the instance you want to start: "))
        instance_id = instances[selected_instance - 1]["Instances"][0]["InstanceId"]

        print(resource_ec2.start_instances(InstanceIds=[instance_id]))

    except Exception as e:
        print(e)


def terminate_ec2_instance():
        try:
            resource_ec2 = boto3.client("ec2")
            response = resource_ec2.describe_instances()
            instances = response["Reservations"]

            if not instances:
                print("No instances found.")
                return

            print("List of instances:")
            for idx, reservation in enumerate(instances):
                for instance in reservation["Instances"]:
                    print(f"{idx + 1}. Instance ID: {instance['InstanceId']}")

            selected_instance = int(input("Enter the number of the instance you want to terminate: "))
            instance_id = instances[selected_instance - 1]["Instances"][0]["InstanceId"]

            confirm = input(f"Are you sure you want to terminate instance {instance_id}? (y/n): ")
            if confirm.lower() == "y":
                print(resource_ec2.terminate_instances(InstanceIds=[instance_id]))
            else:
                print("Termination canceled.")

        except Exception as e:
            print(e)


def stop_ec2_instance():
    try:
        instance_id = input("Enter the instance ID that you want to stop: ")
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.stop_instances(InstanceIds=[instance_id]))

    except Exception as e:
        print(e)


def describe_ec2_instance():
    # Implement this function to retrieve the instance ID of the running instance
    pass


def handle_user_choice(choice):
    if choice == "1":
        create_ec2_instance()
    elif choice == "2":
        start_ec2_instance()
    elif choice == "3":
        stop_ec2_instance()
    elif choice == "4":
        terminate_ec2_instance()
    else:
        print("Invalid choice. Please try again.")


def main():
    display_menu()
    choice = input("Enter your choice: ")
    handle_user_choice(choice)


if __name__ == "__main__":
    main()
