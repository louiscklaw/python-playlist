from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB


with Diagram("Grouped Workers", show=False, direction="TB"):
    ec2_array = [EC2("worker1"),
                  EC2("worker2"),
                  EC2("worker3"),
                  EC2("worker4"),
                  EC2("worker5")]
    ec2_array_1 = [EC2("worker1"),
                  EC2("worker2"),
                  EC2("worker3"),
                  EC2("worker4"),
                  EC2("worker5")]

    ELB("lb") >> ec2_array >>  RDS("events") >> ec2_array_1 >> ELB("lb1")
