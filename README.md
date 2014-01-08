# please hire me
A Django app for building an online portfolio and resume.

The goal for this app is to enable the creation of an integrated portfolio/resume website that connects your projects with your jobs and education to tell the story of your career in a more holistic way than either a portfolio or resume can do on its own. 

When built out, it should also generate a more traditionally printable (PDF) and plaintext version of the resume from the data contained on the site, to eliminate the redundant labor of creating these documents manually. 

## TODO

* ~~finalize models~~
* ~~update models.py with final models~~
* create views for portfolio, project, resume, context
* build up a template collection for different display options

## Unresolved questions:
* ~~"Context" and "Block" are confusing names. Propose **"Role"** and **"Section"** as replacements.~~
* Resume frontend should support a wide variety of combinations and groupings (e.g., many jobs, one org). As long as these don't require data beyond our models, OK to handle this in the view/template layer? 
* Implement tagging feature? 

## Data model

![ER diagram](https://raw2.github.com/macfarlandian/please-hire-me/master/docs/img/PleaseHireMeER.png "Entity-Relationship diagram")

**ResumeHeader**

Contact and social media information. For a portfolio/site with a single user, this will probably only have one row. 

Attributes:

* HeaderID: primary key
* Name: user's name, as it will appear on site and resume
* AddressStreet: street address, including unit number
* AddressCityStateZip: city, state, and postal abbreviation as formatted on resume
* Phone: phone number, as formatted on resume
* Email: email address
* Website: URL, excluding "http://"
* LinkedIn: URL, excluding "http://"
* Twitter: user handle without "at" symbol (e.g., "TwitterUser" or "twitteruser", not "@twitteruser")
* Other: catchall for whatever else you want to include

**ResumeSection**

A section can be standalone text (e.g., an 'Objective', a list of 'Skills' or 'Publications', etc.) or they can be a container for a "collection" of Roles (e.g., an 'Education' section would include schools, 'Experience' would have jobs, etc.).

Attributes: 

* SectionID: primary key
* HeaderID: foreign key to Header
* Name: title of the section, as it will appear on site and resume
* Order: integer indicating order within resume
* Roles: foreign keys to Roles to be collected in this section, if any
* Summary: additional text or html content to be displayed in this section


**Role**

Roles are jobs, degree programs, volunteer positions and other occupations that make up your career history. They serve a dual function. 

1. Roles can be linked to zero or more Projects. This link is bi-directional: the Projects serve as examples of your work in that Role, and the Role provides additional context for that Project.
2. Roles can be displayed in your resume by collecting them into one or more of the Sections that make up your resume.

Attributes: 

* RoleID: primary key
* Name: job title, degree program, or other position name
* Slug: URL-friendly Name
* Order: integer indicating order within Section
* Organization: institution where position was held or degree was obtained
* StartDate: approximate start date of role (YYYY-MM-DD)
* EndDate: approximate end date of role (YYYY-MM-DD)
* Location: location of role (e.g., "San Francisco, CA")
* Summary: short text description
* LongDescription: long text description

**Project**

Projects are items in your portfolio. They must exist within a Role, and can include zero or more Details, which are text bullets or multimedia items.

Attributes:

* ProjectID: primary key
* RoleID: foreign key to Role
* Name: project title
* Slug: URL-friendly Name
* Order: integer indicating order within Role
* Date: approximate completion date of project (YYYY-MM-DD)
* Summary: short text description
* IndexImage: uploaded image to appear on project list page
* LongDescription: long text description

**Detail**

Details are text bullets or multimedia items (photo/video) that can be attached to a Project to provide a fuller description of the Project.

Attributes: 

* DetailID: primary key
* ProjectID: foreign key to Project
* Name: title of detail, if any (this might be the alt text for an image)
* Order: integer indicating order within Project
* Description: text description
* Type: type of detail (enumerated: "Text", "Image", "Video")
* URL: excluding "http://"

**Tag**

Zero or more tags can be attached to Roles, Projects, or Details as desired.

Attributes: 

* TagID: primary key
* Value: the text of the tag (e.g., "infoviz", "UX", "peer-reviewed", "pro bono")
* FKType: type of object being tagged (enumerated: "Role", "Project", "Detail")
* FKID: ID of object being tagged (foreign key to RoleID, ProjectID, or DetailID)

*Your resume consists of a Resume Header followed by one or more Resume Sections. Descriptions follow.*

## Testing Models
I've found it instructive so far to map the resume model to actual resumes to discover potential issues and better ways to adapt and abstract the model so it can support a wider range of frontend resume designs. 

Below are some (anonymized) examples, feel free to add your own. 

### Model: Resume
![resume](https://raw2.github.com/macfarlandian/please-hire-me/master/docs/img/resume1.png)
![resume](https://raw2.github.com/macfarlandian/please-hire-me/master/docs/img/resume2.png)
![resume](https://raw2.github.com/macfarlandian/please-hire-me/master/docs/img/resume3.png)
![resume](https://raw2.github.com/macfarlandian/please-hire-me/master/docs/img/resume4.png)


### Model: Role
![context](https://raw2.github.com/macfarlandian/please-hire-me/master/docs/img/context1.png)
![context](https://raw2.github.com/macfarlandian/please-hire-me/master/docs/img/context2.png)
![context](https://raw2.github.com/macfarlandian/please-hire-me/master/docs/img/context3.png)
![context](https://raw2.github.com/macfarlandian/please-hire-me/master/docs/img/context4.png)

## requirements
* Python 2.7x
* Django 1.5x

###django app dependencies
* django-embed-video
* django-grappelli
