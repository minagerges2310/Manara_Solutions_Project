
# Scalable and Highly Available Web Application on AWS

This project demonstrates the deployment of a scalable and highly available web application on Amazon Web Services. The architecture is designed to handle variable traffic loads, ensure fault tolerance, and provide continuous monitoring and alerting.

## Architecture Diagram
The following diagram illustrates the cloud architecture for this project.

<img width="4988" height="1731" alt="Blank diagram - Page 1 (2)" src="https://github.com/user-attachments/assets/b8653ea6-80ad-4676-88bc-eb8fced2b2b7" />

This diagram shows the flow of user traffic through the Application Load Balancer to EC2 instances managed by an Auto Scaling Group, with monitoring provided by CloudWatch and SNS.

## Live Website
The application can be accessed via the Application Load Balancer's public DNS:
[Here](my-app-alb-297956185.us-east-1.elb.amazonaws.com)

Note: As this is a live demo, the instances may be scaled down or offline.

## Project Description
The core of this project is an Auto Scaling Group of EC2 instances running a simple Python Flask web application. An Application Load Balancer distributes incoming traffic across the instances in multiple Availability Zones, ensuring high availability. CloudWatch monitors the performance of these instances (e.g., average CPU utilization) and triggers alerts via SNS if predefined thresholds are breached, allowing for proactive scaling and issue resolution.

## Key Features
- High Availability: The use of an Application Load Balancer across multiple Availability Zones (AZs) ensures the application remains online even if one AZ fails.

- Scalability: The Auto Scaling Group automatically adds or removes EC2 instances based on demand (e.g., CPU load), ensuring optimal performance and cost-efficiency.

- Fault Tolerance: If an instance becomes unhealthy, the load balancer stops sending traffic to it, and the Auto Scaling Group replaces it with a new, healthy instance.

- Monitoring and Alerting: CloudWatch Alarms are configured to monitor key metrics. If an alarm is triggered, an SNS notification is sent to administrators via email.

- Automation: The `user data` script in the Launch Template automates the setup of the web server on each new EC2 instance.

## AWS Services Used
- Amazon EC2 (Elastic Compute Cloud): Provides the virtual server instances for the web application.

- Application Load Balancer (ALB): Distributes incoming web traffic across multiple EC2 instances.

- Auto Scaling Group (ASG): Automates the process of scaling the number of EC2 instances up or down.

- Amazon CloudWatch: Monitors the application's performance metrics and triggers alarms.

- Amazon SNS (Simple Notification Service): Sends notifications based on CloudWatch alarms.

- Amazon VPC (Virtual Private Cloud): Provides a logically isolated section of the AWS Cloud to launch resources.
 
- IAM (Identity and Access Management): An IAM Role was attached to the EC2 instances to provide secure, role-based access to other AWS services without needing to store credentials on the instance.

## Deployment Steps
The project was deployed using the AWS Management Console by following steps:

1. Networking Setup:

   - A VPC was created with public and private subnets across two Availability Zones.

   - A Security Group was configured to allow HTTP traffic (port 80) from the internet and SSH traffic from a trusted IP.

2. EC2 Launch Template:

   - An EC2 Launch Template was created, specifying the AMI (Amazon Linux 2023), instance type (t2.micro), and the security group.

   - The user data script was added to the template to automate the installation of Python, Flask, and the application code on instance launch.

3. Load Balancing and Scaling:

   - A Target Group was created to register healthy instances.

   - An internet-facing Application Load Balancer (ALB) was set up to distribute traffic to the Target Group.

   - An Auto Scaling Group (ASG) was configured to use the Launch Template, maintain a desired capacity of 2 instances, and automatically scale up to 4 instances if needed.

4. Monitoring and Notifications:

   - An SNS Topic was created with an email subscription to receive alerts.

   - A CloudWatch Alarm was set up to monitor the average     `CPUUtilization` of the Auto Scaling Group and trigger a notification to the SNS topic if the threshold (e.g., 70%) is breached.

