#!/usr/bin/env python3
# https://docs.locust.io/en/stable/writing-a-locustfile.html

import os,sys
from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/")
