# LSOB-Toy-Applications

<h2> Setup Instructions </h2>
Outside of Python 3 installation, the only added dependency is the OAuth python library. Install using pip.

```pip install yahoo_oauth```

In order to make any requests, you'll need an authentication key from Yahoo. Head [here](https://developer.yahoo.com/apps/create/) and create an application for fantasy sports. You should get a long consumer key, and a shorter consumer secret. Copy the format of the oauth2_sample.json file, and create a file named 'oauth2.json' with your keypair placed in.

If you've set up your oauth2.json file correctly, when you run the application for the first time a webpage with a verification token will open. Agree, grab your verification code, and paste the code into the programs prompt. The yahoo_oauth library will take it from there, populating additional fields in oauth2.json (don't worry about what they mean).

![Verifier1](/verifier1.png?raw=true "Agree and get your code")

![Verifier2](/verifier2.png?raw=true "Pasted it here")

From here, you should be able to use the library as normal. For a cryptic and length explanation about all this authentication jazz, visit [their documentation page](https://developer.yahoo.com/fantasysports/guide/).

<h2> Examples </h2>
