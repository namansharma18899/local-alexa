# local-alexa
Local Alexa
## Usage
-  docker build --tag local-alexa .
- docker run local-alexa
## Requirements
- Phase 1 Requirements: 
    Locally Running AI/ML Engines for prediction.
    Complete  Network Isolation for these models ( such that they can’t  exploit our data)
    An Open Source Audio Input Pipeline which sends the output to other services after proper validations. The Pipeline is isolated from network & that’s how we prevent our system from becoming a “Omnipresent Whistleblower”
    The Hearing Pipeline should only honor the input speech which contains a “Secret”  ex: Hello Aria, Hey Aria. Only if there is a secret then only we should play around with it.
    Pipeline which convert Audio Input -> Text -> Answer -> Audio Output

- Phase 2 Requirements: 
    Create and manage the local database of the user. For Example: Our app can have View Permissions to Users’s Excel or Sql file so we fetch queries around it. 
    “What were the sale numbers from the month of July
