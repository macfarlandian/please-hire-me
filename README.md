# please hire me
a Django app for building an online portfolio and resume.

The goal for this app is to enable the creation of an integrated portfolio/resume website that connects your projects with your jobs and education to tell the story of your career in a more holistic way than either a portfolio or resume can do on its own. 

When built out, it should also generate a more traditionally printable (PDF) and plaintext version of the resume from the data contained on the site, to eliminate the redundant labor of creating these documents manually. 

## TODO

* finalize models
* update models.py with final models
* create views for portfolio, project, resume, context
* build up a template collection for different display options

## Unresolved questions:
* "Context" and "Block" are confusing names. Propose **"Role"** and **"Section"** as replacements.
* Resume frontend should support a wide variety of combinations and groupings (e.g., many jobs, one org). As long as these don't require data beyond our models, OK to handle this in the view/template layer? 
* Implement tagging feature? 

## Data model

**Project**

Projects are the items in your portfolio. They can include zero or more Details, which are text bullets or multimedia items.

Attributes:

*	name
*	slug (url-safe version of name)
*	order
*	date
*	introduction
*	frontpage-summary
*	details (relationship to Details)
*	role (relationship to a Role)

**Detail**

Details are text bullets or multimedia items (photo/video) that can be attached to a Project to provide a fuller description of the Project.

Attributes: 

* name
* order
* description
* image file
* video url (handled by django-embed-video app)

**Role**

Roles are the jobs, degree programs, volunteer positions and other occupations that make up your career history. They serve a dual function. 

1. Roles can be linked to zero or more Projects. This link is bi-directional: the Projects serve as examples of your work in that Role, and the Role provides additional context for that Project.
2. Roles can be displayed in your resume by collecting them into one or more of the Sections that make up your resume (see below).

Attributes: 

* name
* slug
* order
* organization
* startdate
* enddate
* location
* introduction
* long-description
* projects (relationship to Projects)

*Your resume consists of a Resume Header followed by one or more Resume Sections. Descriptions follow.*

**Resume Header**

Relatively self-explanatory, yes? 

Attributes:

* name
* address
* phone
* email
* website
* linkedin
* twitter
* etc (catchall for whatever else you want to include)


**Resume Section**

Resume Sections can be standalone text (e.g., an 'Objective,' a list of 'Skills' or 'Publications,' etc.) or they can contain "collections" of Roles (e.g., an 'Education' section would include schools, 'Experience' would have jobs, etc.).

Attributes: 

* name
* description
* order
* collection (relationship to Roles)

## Testing Models
I've found it instructive so far to map the resume model to actual resumes to discover potential issues and better ways to adapt and abstract the model so it can support a wider range of frontend resume designs. 

Below are some (anonymized) examples, feel free to add your own. 

### Model: Resume
![resume](https://raw.github.com/macfarlandian/please-hire-me/master/docs/img/resume1.png)
![resume](https://raw.github.com/macfarlandian/please-hire-me/master/docs/img/resume2.png)
![resume](https://raw.github.com/macfarlandian/please-hire-me/master/docs/img/resume3.png)


### Model: Context
![context](https://raw.github.com/macfarlandian/please-hire-me/master/docs/img/context1.png)
![context](https://raw.github.com/macfarlandian/please-hire-me/master/docs/img/context2.png)
![context](https://raw.github.com/macfarlandian/please-hire-me/master/docs/img/context3.png)

## requirements
*	Python 2.7x
*	Django 1.5x

###django app dependencies
* django-embed-video
* django-grappelli
