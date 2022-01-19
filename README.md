#Bank Account Manager
This a simple bank account managers with ability to define and update bank accounts in two currency(USD, EUR).
Also we can create transactions between bank accounts.

##Development
- Install docker and docker-compose.
- Run `cp .env.sample .env` and fill `.env` file.
- Run `docker-compose -f docker-compose.dev.yml up --build`.
- The service is run under `0.0.0.0:8000` and update after each file changes.

##Deployment
- Install docker and docker-compose.
- Run `cp .env.sample .env` and fill `.env` file.
- Run `docker-compose -f docker-compose.prod.yml up --build`.
- The service is run under `yourserverip/domain`.

##Rest API Documents
- You can see api documentations under `/swagger` or `/redoc` urls.
- Also, the pdf file `rest_apis_doc.pdf` is in the root of project.

