Let us try to understand this model in detail
A simple alexa based communication requires the following contents:
  I) Amazon Alexa console
  II) the backend code (AWS: Serverless-Application-Repository)
  III) the connection between these three the ARN (Amazon Resource Network)

Quick Set-up Instructions
  I) Create an account on Amazon Alexa Console
  II) Create your first mod with Instances and Utterances (preferred server N.virginia [us-east-1])
  III) Create a Serverless Application Repository specific to Node.js for implementing the speaking and listining interaction models of alexa 'alexa-sdk-core'.
  IV) Here aresome detailed steps to fetch this repository:
            -> 1. Go to AWS search serverless-application-repository
            -> 2. Click on Available Applications
            -> 3. search "alexa-skills-kit-nodejs-factskill"
  V) If you still couldn't find it then you stupid as fuck (just like me) here is the link: https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/create/app?applicationId=arn:aws:serverlessrepo:us-east-1:173334852312:applications/alexa-skills-kit-nodejs-factskill


Now Setting up of our Secondary Lambda function (Easy and Hard)
  I) Create a server from scratch
  II) Add the code from "Raw_Code.py"
  III) Test this on AWS (You will get errors)
  IV) This error will be because you do not have the required modules as this server is made from scratch
  V) Now add layers of the required modules as shown in this video: https://www.youtube.com/watch?v=mTYp4lTWMAw&t=306s
  VI) Lastly, don't act dumb like me replace his modules with the ones not found on cloudWatch OR directly load the Zip file of AnalyzeEastAfricanCredits. 
