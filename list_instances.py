#!/usr/bin/env python
import boto3
ec2 = boto3.resource('ec2')
print "Instance, State: ",
for instance in ec2.instances.all():
    print "Instance, State: ", instance.id, instance.state
