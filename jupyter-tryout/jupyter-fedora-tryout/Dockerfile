FROM python:3.11

RUN pip install playwright
RUN pip install nest_asyncio
RUN pip install jupyter
RUN pip install python-dotenv

RUN playwright install-deps & \
playwright install
