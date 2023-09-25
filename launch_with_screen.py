import tkinter as tk
from tkinter import messagebox
import boto3

def create_ec2_instance():
    try:
        image_id = image_id_entry.get()
        min_count = int(min_count_entry.get())
        max_count = int(max_count_entry.get())
        instance_type = instance_type_entry.get()
        key_name = key_name_entry.get()
        security_group_ids = security_group_ids_entry.get()
        user_data = user_data_entry.get()

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
        messagebox.showinfo("Success", f"Instance created with ID: {instance_id}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create GUI window
window = tk.Tk()
window.title("EC2 Instance Management")

# Create input fields
image_id_label = tk.Label(window, text="AMI ID:")
image_id_label.pack()
image_id_entry = tk.Entry(window)
image_id_entry.pack()

min_count_label = tk.Label(window, text="Minimum Count:")
min_count_label.pack()
min_count_entry = tk.Entry(window)
min_count_entry.pack()

max_count_label = tk.Label(window, text="Maximum Count:")
max_count_label.pack()
max_count_entry = tk.Entry(window)
max_count_entry.pack()

instance_type_label = tk.Label(window, text="Instance Type:")
instance_type_label.pack()
instance_type_entry = tk.Entry(window)
instance_type_entry.pack()

key_name_label = tk.Label(window, text="Key Name:")
key_name_label.pack()
key_name_entry = tk.Entry(window)
key_name_entry.pack()

security_group_ids_label = tk.Label(window, text="Security Group IDs (comma-separated):")
security_group_ids_label.pack()
security_group_ids_entry = tk.Entry(window)
security_group_ids_entry.pack()

user_data_label = tk.Label(window, text="User Data:")
user_data_label.pack()
user_data_entry = tk.Entry(window)
user_data_entry.pack()

# Create button to create EC2 instance
create_button = tk.Button(window, text="Create Instance", command=create_ec2_instance)
create_button.pack()

# Start the GUI event loop
window.mainloop()
