# FizzBuzz Application

As part of the candidates evaluation, the company asks the candidates to develop a FizzBuzz Application Deployer using Terraform.
There is no mandatory language for the application.

## Requirements

 - Terraform 0.12 (or higher)
 - python 3.8 (or higher)
 - zip 3.0

## Good to have - not mandatory

  - tfenv: manage terraform version usage

## How to Deploy

This project has a Makefile that helps the users to deploy the application:
```
make deploy
```

The owner of this project encourage everbody to take a look to Makefile and see the calls developed.

### Deleting the resources

The Makefile also has a call to destroy the resources created:
```
make destroy
```

## Output sample

The file `output.txt` has an example of the application running through lambda after deployed by terraform.


## Testing - not implemented

This project does not cover application tests as it was not mandatory in the requirements. However, some approachs were taken in the code in case someone wants to implement them:
- The code is commented
- The code is refactored
- Small functions helping the unit tests
