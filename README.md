![Capture](https://res.cloudinary.com/dhhax6yae/image/upload/v1691668693/Screenshot_2023-08-10_at_5.23.53_PM_u9qny4.png)

# AxisHR
---

`AxisHR` is your all-in-one solution to streamline and optimize your hiring process. In today's competitive job market, finding the perfect candidate efficiently and fairly is crucial. Our cutting-edge platform tackles the pain points that have long plagued HR professionals, transforming the way you evaluate job descriptions, screen CVs, conduct interviews, and communicate throughout the hiring journey.

Contents
---

* [Installation](#installation)
* [Tech-Stacks Used](#tech-stacks-used)
* [Features Added](#features-added)
* [Future Scope](#future-scope)
* [Snapshots](#snapshots)
* [Deployed Link](#deployed-link)

### Installation:
---
This guide will walk you through the steps to set up and run the application. Ensure you have a compatible version of Python installed (Python 3.6 or higher).

#### Method 1: Quick Setup
For a hassle-free installation, follow these steps:
1. Run the batch script on Windows:
```bat_setup.bat ```

2. Alternatively, if you are using a bash terminal, execute the following command:
```sh ./setup.sh```

#### Method 2: Manual Setup

#### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```
git clone https://github.com/gouravmohanty7070/LLM_Bankathon.git
```


#### Step 2: Setup Virtual Environment

To ensure a clean and isolated environment for your application, it's recommended to use a virtual environment. Here's how you can set it up:

```
cd LLM_Bankathon
python -m virtualenv venv
```
Activating the Virtual Environment
- On Windows:
```
venv\Scripts\activate
```

- On macOS and Linux:

```
source venv/bin/activate
```

#### Step 3: Install Dependencies
With the virtual environment activated, install the required dependencies using pip and the requirements.txt file:
```
pip install -r requirements.txt
```
#### Step 4: Setup .env
To run the LLMs we need to create a .env file based on the sample.env file and add our openai api key to it 

```
OPENAI_API_KEY = "{your_api_key}"
```

#### Step 5: Start the Application
Navigate to the "LLM" directory, which contains the application code:
```
cd LLM
```

Run the following command to start the application:
```
python manage.py runserver
```

#### Step 6: Access the Application
Open your web browser and go to http://127.0.0.1:8000/ 

### IMPORTANT
The login credentials are 
- Email: gourav@axisbank.com
- Password: 1234

### Tech-Stacks Used:
---

- Python
- LangChain
- SQL Database
- Django
- Javascript
- Microsoft Azure

### Features Added
---
<ol>
<li>Job Description Evaluation and Enhancement:
Analyzes job description effectiveness, suggests enhancements based on job title, and offers users the choice to retain the original version or incorporate suggested changes.
</li></br>
<li>Automated CV Screening and Ranking:
Automatically processes and analyzes multiple CVs in various formats, compares them to job description requirements, ranks and scores each CV based on alignment, ensuring efficient initial candidate evaluation.
</li></br>
<li>Email Notifications:
Automates email notifications to inform shortlisted candidates about the next steps in the hiring process, providing clear instructions and maintaining a professional communication channel.
</li></br>
<li>Customized Screening Questions:
Generates tailored screening questions for each candidate by considering the importance of both the job description and the candidate's CV, ensuring the interview process focuses on the most relevant aspects for each candidate.
</li></br>
<li>Collaborative HR Workspace:
Provides a centralized platform for HR teams to seamlessly collaborate, share insights, evaluations, and candidate progress updates, enhancing communication and decision-making within the team.
</ol>

### Future Scope
---
<ol>
<li>Open Source Model:
Transition to a complete open-source approach for enhanced security and quality control. Internal development will optimize costs while maintaining high standards.
</li></br>
<li>Automated Background Checks:
Integrate automated background checks to reduce HR workload, ensuring faster and more accurate processing. This mitigates human bias and enhances fairness in candidate assessments.
</li></br>
<li>Employee Referral System App:
Create a dedicated app for an effortless employee referral system. The app will manage reward points for successful referrals, addressing concerns for employees and HR. Customization will align the app with specific company needs.
</li></br>
<li>Social Media Crawler:
Introduce an advanced social media crawler to analyze candidates' online presence and extract CVs. This tool will streamline candidate selection, ensuring a comprehensive evaluation against job requirements.
</li></br>
</ol>

### Deployed Link 
---

[Deployed Link](http://52.255.177.160)

### Note 

Functionality for LLM_3 and LLM_4 have not been added to UI currently due to time constraints, one can run the code for the mentioned modules in their ide by calling the function with the required parameters and logging the information.
